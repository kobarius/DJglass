# -*- coding: utf-8 -*-

import wiringpi2 as w
import time



def monotron() :
     # 音程をコントロール
     REF=3.3  # 5.p or 3.3
     w.wiringPiSetup()
     w.pinMode(0,1)
     w.pinMode(1,2)
     w.digitalWrite(0,1)
     while 1 :
         for i in [0,300,380,460,540,640,720,1000] :
             w.pwmWrite(1,i)
             print(i)
             time.sleep(0.5)
         w.digitalWrite(0,0)


if __name__ == '__main__' :
	monotron();


