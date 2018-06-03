#!/bin/bash/python3
import time
import picamera
import picamera.array
import argparse


class Camera():
    def __init__(self, w=32, h=32):
        self.width = w
        self.height = h
    def setup(self):
        self.camera = picamera.PiCamera()
        self.camera.start_preview()
        self.camera.resolution = (self.width, self.height)
    def captureImg(self):
        with picamera.array.PiRGBArray(self.camera) as stream:
            self.camera.capture(stream, 'bgr')
            image = stream.array
        return image

class DummyCamera():
    def __init__(self, w=32, h=32):
        self.width = w
        self.height = h
    def setup(self):
        pass
    def captureImg(self):
        #TODO read image file
        images = np.zeros([self.width, self.height])
        return image

def detectDrink(img):
    drink_id = 5
    drink_name = "beer"
    return {'id': drink_id,'name': drink_name}

def main(dummy = False):
    CAPTURE_WIDTH = 32
    CAPTURE_HEIGHT = 32
    if dummy:
        camera = DummyCamera(CAPTURE_WIDTH,CAPTURE_HEIGHT)
    else:
        camera = Camera(CAPTURE_WIDTH,CAPTURE_HEIGHT)
    camera.setup()
    while True:
        img = camera.captureImg()
        print(img)
        answer = detectDrink(img)
        print(answer)

if __name__ == '__main__':
    #TODO argparse debugmode , dummycamera
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    
    args = parser.parse_args()
    print(args.accumulate(args.integers))
    '''
    main()

