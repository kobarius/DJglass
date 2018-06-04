import time
import picamera
import picamera.array
import logging
from logging import getLogger, StreamHandler, Formatter

class Camera():
    def __init__(self, w=32, h=32, debug=False, logger=None):
        self.width = w
        self.height = h
        self.num = 0
        self.logger=logger
        self.debug=debug
        self.save_img = True

    def setup(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (self.width, self.height)
        if self.debug:
            self.camera.start_preview()
        if not self.logger:
            self.logger = getLogger("PICAMERA")
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
        with picamera.array.PiRGBArray(self.camera) as stream:
            self.camera.capture(stream, 'bgr')
            image = stream.array
            if self.save_img:
                # save image "img/djglass_cap_0001.jpg"
                img_name = "img/djglass_cap_" + ("0000" + str(self.num))[-4:]+ ".jpg"
                self.camera.capture(img_name)
                self.logger.debug("save image "+ img_name)
        self.num += 1
        return image


def main():
    CAPTURE_WIDTH = 32
    CAPTURE_HEIGHT = 32
    camera = Camera(CAPTURE_WIDTH,CAPTURE_HEIGHT)
    camera.setup()
    while True:
        img = camera.captureImg()
        time.sleep(1)

if __name__ == '__main__':
    main()
