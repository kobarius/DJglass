#! /usr/bin/python3
# coding:utf-8
import argparse
import drink_detect
import time

# ログのライブラリ
import logging
from logging import getLogger, StreamHandler, Formatter

# loggerの設定
## loggerオブジェクトの宣言
logger = getLogger("DJGLASS")
## loggerのログレベル設定(ハンドラに渡すエラーメッセージのレベル)
logger.setLevel(logging.DEBUG)
## handlerの生成
stream_handler = StreamHandler()
## ログ出力フォーマット設定
handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(handler_format)
# loggerにhandlerをセット
logger.addHandler(stream_handler)
# loggerの設定終わり

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

    while True:
        img = cam.captureImg()
        #logger.debug(img)
        answer = dd.detect(img)
        logger.debug(answer)
        time.sleep(1)

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


