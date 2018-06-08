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
    #pi.write(17,1)

    list0 = [aa,a,aa,a,aa,aa,a,f,f,g,e,e,d,c,c,d]
    list1 = [1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,]

    list2 = [aa,a,aa,a,aa,a,aa,a,aa,a,aa,a,aa,a,aa,a]
    list3 = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,]

    list4 = [a,a,a,d,d,d,a,b,c,d,e,f,g,aa,a,d]
    list5 = [1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,]
    
    while 1 :
        #for i in [0,300,380,460,540,640,720,1000] :
        #for i in [[a,1],[a,0],[a,1],[a,0],[a,1],[a,0]]
        #for i in [e,aa,d,g,a,c,a]:
        for i, j in zip( list4, list5 ):
            pi.hardware_PWM(18,128,i*1000)
            pi.write(17,j)
            print(i)
            time.sleep(0.125)
       # for j in [1,0,1,0,1,0,1]:
            #print(i)
            #time.sleep(0.25)

if __name__ == '__main__' :
    monotron();



