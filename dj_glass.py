#! /usr/bin/python3
# coding:utf-8
import time
import threading
import argparse
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO

import drink_detect
from monotron import monotron

# root rogger setting
logger = getLogger()
formatter = Formatter('%(asctime)s %(name)s %(funcName)s [%(levelname)s]: %(message)s')
handler = StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(DEBUG)

# Drink ID (global)
global_drink_id = 0


def cameraThread(cam, dd):
    global global_drink_id 
    while True:
        img = cam.captureImg()
        answer = dd.detect(img)
        global_drink_id = answer["id"]
        logger.info(answer)
        time.sleep(1)


def djThread():
    global global_drink_id 
    while True:
        monotron(global_drink_id)
        logger.debug("DJ change music" + str(global_drink_id))



def main(dummy = False, debug = False):
    # setup camera
    CAPTURE_WIDTH = 32
    CAPTURE_HEIGHT = 32
    if dummy:
        import dummy_camera
        cam = dummy_camera.DummyCamera(CAPTURE_WIDTH, CAPTURE_HEIGHT, debug=debug)
    else:
        import camera
        cam = camera.Camera(CAPTURE_WIDTH, CAPTURE_HEIGHT, debug=debug)
    cam.setup()
    
    # setup drink detector
    dd = drink_detect.DrinkDetector(debug=debug)
    dd.setup()

    # setup DJ
    #TODO

    # make camera thread
    # camera thred set global_drink_id
    camera_thread = threading.Thread(target=cameraThread, args=([cam, dd]))


    # make DJ thread
    # DJ thread get global_drink_id
    dj_thread = threading.Thread(target=djThread)


    camera_thread.start()
    dj_thread.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action="store_true",  help='debug mode switch')
    parser.add_argument('--dummycamera', action="store_true" ,help='dummy camera mode switch')
    args = parser.parse_args()
    # set logging handler level
    if args.debug:
        handler.setLevel(DEBUG)
    else:
        handler.setLevel(INFO)
    main(debug=args.debug, dummy=args.dummycamera)

