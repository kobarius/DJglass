# -*- coding: utf-8 -*-
import pigpio
import time


def monotron() :
    a = 0
    b = 300
    c = 380
    d = 460
    e = 540
    f = 640
    g = 720
    aa = 1000
    # 音程をコントロール
    REF=3.3  # 5.p or 3.3
    pi = pigpio.pi()
    pi.set_mode(17,pigpio.OUTPUT) # volume
    pi.set_mode(18,pigpio.OUTPUT) # tone
    pi.write(17,1)
    while 1 :
        #for i in [0,300,380,460,540,640,720,1000] :
        for i in [b,c,d,e,f,g,aa]:
            pi.hardware_PWM(18,16,i*1000)
            print(i)
            time.sleep(1)

if __name__ == '__main__' :
    monotron();


