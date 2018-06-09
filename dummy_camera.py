import numpy as np
import logging
from logging import getLogger, DEBUG, NullHandler

local_logger = getLogger(__name__)
local_logger.addHandler(NullHandler())
local_logger.setLevel(DEBUG)
local_logger.propagate = True

class DummyCamera():
    '''
    same interface with "Camera"
    '''
    def __init__(self, w=32, h=32, debug=False, logger=None):
        self.width = w
        self.height = h
        self.logger=logger or local_logger
        self.debug=debug

    def setup(self):
        self.logger.debug("finish setup")

    def captureImg(self):
        #TODO read image file
        image = np.random.randint(0, 255, [self.width, self.height, 3], dtype=np.uint8)
        self.logger.debug("capture image")
        return image
