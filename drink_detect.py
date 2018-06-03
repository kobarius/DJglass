import sklearn
import numpy as np

class DrinkDetector():
    def __init__(self):
        pass

    def setup(self):
        # TODO
        pass

    def detect(self, img):
        '''
        input: img (numpyarray int8 32*32)
        output: {'id': drink_id(int), 'name': drink_name(str)}
        '''
        # TODO impliment drink detector
        drink_id = 5
        drink_name = "beer"
        return {'id': drink_id,'name': drink_name}
