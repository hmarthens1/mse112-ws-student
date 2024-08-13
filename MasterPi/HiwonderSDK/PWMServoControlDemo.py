#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/pi/mse112-ws-student/MasterPi/')
import time
import signal
import threading
import HiwonderSDK.Board as Board

start = True
#Before closing
def Stop(signum, frame):
    global start

    start = False
    print('Closing...')

signal.signal(signal.SIGINT, Stop)

def servo_init():
    Board.setPWMServoPulse(1, 2500, 300) # Set the pulse width of Servo 1 to 2500 and the running time to 1000 milliseconds
    time.sleep(1)
    Board.setPWMServoPulse(3, 1000, 300) 
    time.sleep(1)
    Board.setPWMServoPulse(4, 2000, 1000) 
    time.sleep(1)
    Board.setPWMServoPulse(5, 2100, 1000) 
    time.sleep(1)
    Board.setPWMServoPulse(6, 1500, 1000) 




if __name__ == '__main__':

    servo_init()
    
    while True:
  
        if not start:
            Board.setPWMServoPulse(2, 1500, 1000) # Set the pulse width of Servo 1 to 1500 and the running time to 1000 milliseconds
            time.sleep(1)
            print('closed')
            break
    
    
        