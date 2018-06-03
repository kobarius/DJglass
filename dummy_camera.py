import numpy as np
import logging
from logging import getLogger, StreamHandler, Formatter

class DummyCamera():
    '''
    same interface with "Camera"
    '''
    def __init__(self, w=32, h=32, debug=False, logger=None):
        self.width = w
        self.height = h
        self.logger=logger
        self.debug=debug
    def setup(self):
        if not self.logger:
            self.logger = getLogger("DUMMYCAMERA")
            self.logger.setLevel(logging.DEBUG)
            stream_handler = StreamHandler()
            if self.debug:
                stream_handler.setLevel(logging.DEBUG)
            else:
                stream_handler.setLevel(logging.INFO)
            handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            stream_handler.setFormatter(handler_format)
            self.logger.addHandler(stream_handler)
    def captureImg(self):
        #TODO read image file
        image = np.zeros([self.width, self.height])
        self.logger.debug("capture image")
        return image