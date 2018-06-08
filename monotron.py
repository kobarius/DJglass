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

    list0a = [aa, a,aa, a,aa,aa, a, f, f, g, e, e, d, c, c, d]	# no_drink tone
    list0b = [ 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0]	# no_drink vol
    list1a = [aa, a,aa, a,aa, a,aa, a,aa, a,aa, a,aa, a,aa, a]	# beer tone
    list1b = [ 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]	# beer vol
    list2a = [ a, a, a, d, d, d, a, b, c, d, e, f, g,aa, a, d]	# coke tone
    list2b = [ 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0]	# coke vol

    if drink_id == 0:
       listxa = list0a
       listxb = list0b
    elif drink_id == 1 or drink_id == 2:
       listxa = list1a
       listxb = list1b
    elif drink_id == 3 :
       listxa = list2a
       listxb = list2b
    else :
       listxa = list0a
       listxb = list0b

#    while 1 :
    for i,j in zip(listxa,listxb):
        pi.hardware_PWM(18,128,i*1000)
        pi.write(17,j)
        print(i)
        time.sleep(0.125)

if __name__ == '__main__' :

    for idx in [0, 1, 2, 3, 4] :
        print("id=",idx)
        for var in range(0,2):
            monotron(idx);


