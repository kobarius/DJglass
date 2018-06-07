#! /usr/bin/python3
# coding:utf-8
import argparse
import drink_detect
import time
import threading

# ログのライブラリ
import logging
from logging import getLogger, StreamHandler, Formatter

# loggerの設定
logger = getLogger("DJGLASS")
logger.setLevel(logging.DEBUG)
stream_handler = StreamHandler()
handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(handler_format)
logger.addHandler(stream_handler)

# Drink ID (global)
global_drink_id = 0


def cameraThread(cam, dd):
    global global_drink_id 
    while True:
        img = cam.captureImg()
        #logger.debug(img)
        answer = dd.detect(img)
        global_drink_id = answer["id"]
        logger.debug(answer)
        time.sleep(1)


def djThread():
    global global_drink_id 
    while True:
        logger.debug("DJ change music" + str(global_drink_id))
        time.sleep(3)



def main(dummy = False, debug = False):
    # setup camera
    CAPTURE_WIDTH = 32
    CAPTURE_HEIGHT = 32
    if dummy:
        import dummy_camera
        cam = dummy_camera.DummyCamera(CAPTURE_WIDTH,CAPTURE_HEIGHT, debug=debug)
    else:
        import camera
        cam = camera.Camera(CAPTURE_WIDTH,CAPTURE_HEIGHT, debug=debug)
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
    #TODO
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
        stream_handler.setLevel(logging.DEBUG)
    else:
        stream_handler.setLevel(logging.INFO)
    main(debug=args.debug, dummy=args.dummycamera)

