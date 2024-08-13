#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/pi/mse112-ws/MasterPi/')
import time
import signal
import threading
import HiwonderSDK.Board as Board


# Turn off all motors
def MotorStop():
    Board.setMotor(1, 0) 
    Board.setMotor(2, 0)
    Board.setMotor(3, 0)
    Board.setMotor(4, 0)

start = True
#Close before processing
def Stop(signum, frame):
    global start

    start = False
    print('Closing...')
    MotorStop()  # Turn off all motors
    

signal.signal(signal.SIGINT, Stop)

if __name__ == '__main__':
    
    while True:
        Board.setMotor(1, 35)  #Set the speed of motor 1 to 35
        time.sleep(1)
        Board.setMotor(1, -60)  #Set the speed of motor 1 to 60
        time.sleep(2)
        Board.setMotor(1, 90)  #Set the speed of motor 1 to 90
        time.sleep(3)    
        
        if not start:
            MotorStop()  # Turn off all motors
            print('closed')
            break