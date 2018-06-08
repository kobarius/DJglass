# -*- coding: utf-8 -*-
import pigpio
import time


def monotron(drink_id) :
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

    list0a = [a,a,a,a,a,a,a,a,a,a,a,a,a]	# no_drink
    list0b = [0,0,0,0,0,0,0,0,0,0,0,0,0]	# no_drink
    list1a = [a,a,a,a,a,a,a,a,a,a,a,a,a]	# beer
    list1b = [0,0,0,0,0,0,0,0,0,0,0,0,0]	# beer
    list2a = [a,a,a,a,a,a,a,a,a,a,a,a,a]	# coke
    list2b = [0,0,0,0,0,0,0,0,0,0,0,0,0]	# coke

    if drink_id == 0:
       listxa = list0a
       listxb = list0b
    elif drink_id = 1 or drink_id = 2:
       listxa = list1a
       listxb = list1b
    elif drink_id = 2 :
       listxa = list2a
       listxb = list2b
    else
       listxa = list0a
       listxb = list0b

    while 1 :
        #for i in [0,300,380,460,540,640,720,1000] :
        for i,j in zip(listxa,listxb):
            pi.hardware_PWM(18,4,i*1000)
            pi.write(17,j)
            print(i)
            time.sleep(1)

if __name__ == '__main__' :

    for idx in [0, 1, 2, 3, 4]
    	monotron(idx);


