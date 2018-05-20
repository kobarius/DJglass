# -*- coding: utf-8 -*-

import wiringpi2 as w
import time

def MCP3008(channel)
    register = 0x80
    buff=(1 << 16) + (register<<8)+(channel<<12)
    buff=buff.to_bytes(3,byteorder='big')
    w.wiringPiSPIDataRW(0,buff)
    return (((buf[1]&3)*256)+buff[2])

def telmin():
    REF=3.3  # 5.p or 3.3
    mode=1
    w.wiringPiSetup()
    w.wiringPiSPISetup(0,1000000)
    w.pinMode(0,1)
    w.pinMode(2,1)
    w.pinMode(1,2)
    #w.softPwmCreate(1,0,100)
    w.softPwmCreate(2,0,100)

    w.digitalWrite(0,1)
    
    while 1:
        data1 = MCP3008(1)
        data7 = MCP3008(7)
        time.sleep(0.01)
        data11 = int(data1)-860;
        w.softPwmWrite(2,data11)
        data71 = int(((data7/20)*5.8)-225)
        w.pwmWrite(1,data71*10)
        print('%4.2f'%data11,'%4.2f'%data71,'%.2f'%(data1/1024*REF),"volt",'%.2f'%(data7/1024*REF),"volt")

if __name__ == '__main__' :
	telmin();


