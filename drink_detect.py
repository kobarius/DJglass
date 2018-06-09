import os
import glob
import random
import pickle
import numpy as np
from sklearn import model_selection, svm, metrics
from PIL import Image
from logging import getLogger, DEBUG, NullHandler

local_logger = getLogger(__name__)
local_logger.addHandler(NullHandler())
local_logger.setLevel(DEBUG)
local_logger.propagate = True

class DrinkDetector():
    def __init__(self,debug=False, logger=None):
        #self.drink_list = ("no_drink", "beer", "orange", "coke", "lemon-chu")
        self.drink_list = ("no_drink", "beer", "beer", "coke", "no_drink")
        self.logger=logger or local_logger
        self.debug=debug
        self.model_pickle_name = 'djglass_model.pickle'

    def setup(self):
        # load model
        self.model = pickle.load(open(self.model_pickle_name, 'rb'))
        self.logger.debug("finish load model")

    def train(self):
        data = [] # float 3*32*32
        label = [] # int
        for i in range(5):
            images = glob.glob(os.path.join("./img/train/",str(i), "*.jpg"))
            # read_img
            for img_name in images:
                h, s, v = Image.open(img_name).convert("HSV").split()
                np_h = np.asarray(h).flatten()
                np_s = np.asarray(s).flatten()
                np_v = np.asarray(v).flatten()
                img_np = np.hstack((np_h, np_s, np_v))
                norm_img = img_np / 255.
                data.append(norm_img)
                label.append(i)
                self.logger.debug(norm_img)
                self.logger.debug(norm_img.shape)

        # split date into train and test
        data_num = len(data)
        test_size = int(data_num/5)
        train_size = data_num-test_size
        data_train, data_test, label_train, label_test = model_selection.train_test_split(data, label, test_size=test_size, train_size=train_size)

        self.logger.debug(label)
        self.logger.debug("load data " + str(data_num))

        # define model and train
        clf = svm.SVC(kernel='rbf', C=len(self.drink_list))
        clf.fit(data_train, label_train)

        self.logger.debug("finish train")

        # test
        pre = clf.predict(data_test)
        ac_score = metrics.accuracy_score(label_test, pre)
        self.logger.debug(pre)
        self.logger.debug(ac_score)

        # save model
        pickle.dump(clf, open(self.model_pickle_name, 'wb'))


    def detect(self, img):
        '''
        input: img (numpyarray int8 32*32)
        output: {'id': drink_id(int), 'name': drink_name(str)}
        '''
        h, s, v = Image.fromarray(img).convert("HSV").split()
        np_h = np.asarray(h).flatten()
        np_s = np.asarray(s).flatten()
        np_v = np.asarray(v).flatten()
        img_np = np.hstack((np_h, np_s, np_v))
        norm_img = img_np.flatten()/255.
        self.logger.debug(norm_img)
        self.logger.debug(norm_img.shape)
        drink_id = self.model.predict([norm_img])[0]
        drink_name = self.drink_list[drink_id]
        return {'id': drink_id,'name': drink_name}

