#!/usr/bin/python3
#coding=utf8
import sys
sys.path.append('/home/pi/mse112-ws/MasterPi/')
import time
import signal
import numpy as np
import pandas as pd
import HiwonderSDK.Sonar as Sonar
import HiwonderSDK.Board as Board
from ArmIK.Transform import *
from ArmIK.ArmMoveIK import *

AK = ArmIK()

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


HWSONAR = Sonar.Sonar()

distance_data = []
servo_init()

while True:
    

    dist = HWSONAR.getDistance() / 10.0


    distance_data.append(dist)

    if len(distance_data) > 5:
        distance_data.pop(0)

    distance = np.mean(distance_data)

    print("Distance measured:\n")
    print(distance)

