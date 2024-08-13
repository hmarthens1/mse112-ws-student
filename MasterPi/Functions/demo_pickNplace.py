#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/pi/mse112-ws/MasterPi/')
import cv2
import time
import Camera
import threading
import logging
import yaml_handle
from ArmIK.Transform import *
from ArmIK.ArmMoveIK import *
import HiwonderSDK.Sonar as Sonar
import HiwonderSDK.Board as Board
from CameraCalibration.CalibrationConfig import *


if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)

AK = ArmIK()
HWSONAR = Sonar.Sonar() #ultrasonic sensor


lab_data = None
def load_config():
    global lab_data, servo_data
    
    lab_data = yaml_handle.get_yaml_data(yaml_handle.lab_file_path)

    
def servo_init():


    Board.setPWMServoPulse(1, 2500, 300) # Set the pulse width of Servo 1 to 2500 and the running time to 1000 milliseconds
    time.sleep(0.5)
    Board.setPWMServoPulse(3, 800, 500) 
    time.sleep(0.5)
    Board.setPWMServoPulse(4, 2000, 500) 
    time.sleep(0.5)
    Board.setPWMServoPulse(5, 2100, 500) 
    time.sleep(1)
    Board.setPWMServoPulse(6, 1500, 500)
    time.sleep(1)
    Board.setPWMServoPulse(6, 1500, 500) 


# initial position
def initMove():
    servo_init()

def setBuzzer(timer):
    Board.setBuzzer(0)
    Board.setBuzzer(1)
    time.sleep(timer)
    Board.setBuzzer(0)


count = 0
_stop = False
color_list = []
get_roi = False
__isRunning = False
detect_color = 'None'
start_pick_up = False
start_count_t1 = True
obstacle = False
distance = 0

#Variable reset
def reset():
    global _stop
    global count
    global get_roi
    global color_list
    global detect_color
    global start_pick_up
    global __target_color
    global start_count_t1
    global obstacle
    global distance


    obstacle = False
    distance = 0
    count = 0
    _stop = False
    color_list = []
    get_roi = False
    __target_color = ()
    detect_color = 'None'
    start_pick_up = False
    start_count_t1 = True

# app initialization call
def init():
    load_config()
    initMove()

# app starts gameplay call
def start():
    global __isRunning
    reset()
    __isRunning = True


# app stops gameplay calling
def stop():
    global _stop
    global __isRunning
    _stop = True
    __isRunning = False


# app exit gameplay call
def exit():
    global _stop
    global __isRunning
    _stop = True
    # set_rgb('None')
    __isRunning = False
    print("ColorSorting Exit")


def move():
    global _stop
    global get_roi
    global unreachable
    global __isRunning
    global obstacle
    global distance
    
    #coordinates for pick and place
    coordinate = {
        'place':   (-18, globals()['distance'], 1),
        'pick': (0, globals()['distance'],  0),
    }

    while True:
        if __isRunning and not obstacle:
                
                initMove()
                
                # Pick
                print("Pick and Place Start\n")
                if not __isRunning:
                    continue

                # Pick
                print("Pick and Place Start\n")

                Board.setPWMServoPulse(1, 2000, 500) # open claws
                time.sleep(2.5)

                result = AK.setPitchRangeMoving((coordinate['pick'][0], coordinate['pick'][1], coordinate['pick'][2]), -90, -90, 0) # Run to above the coordinates of the corresponding color
                if result == False:
                    unreachable = True
                    print("Unreachable\n")
                else:
                    unreachable = False
                    time.sleep(result[2]/1000) #If the specified location can be reached, get the running time

                if not __isRunning:
                    continue

                AK.setPitchRangeMoving((coordinate['pick']), -90, -90, 0, 500)  # pick from the corresponding coordinate
                time.sleep(0.5)

                if not __isRunning:
                    continue


                Board.setPWMServoPulse(1, 1500, 500) # closed paw
                time.sleep(1.5)

                if not __isRunning:
                    continue

                # end of Pick


                AK.setPitchRangeMoving((0, 6, 18), 0,-90, 90, 1500)
                time.sleep(1.5)

                
                # Place

                result = AK.setPitchRangeMoving((coordinate['place'][0], coordinate['place'][1], coordinate['place'][2]), -90, -90, 0) # Run to above the coordinates of the corresponding color
                if result == False:
                    unreachable = True
                    print("Unreachable\n")
                else:
                    unreachable = False
                    time.sleep(result[2]/1000) #If the specified location can be reached, get the running time

                if not __isRunning:
                    continue

                AK.setPitchRangeMoving((coordinate['place']), -90, -90, 0, 500)  # pick from the corresponding coordinate
                time.sleep(1.5)

                if not __isRunning:
                    continue

                Board.setPWMServoPulse(1, 1800, 500) # open claws
                time.sleep(1.5)

                if not __isRunning:
                    continue

                # end of Place

                initMove()


                
                time.sleep(1.2)

                __isRunning = False

                print("Pick and Place end\n")

                initMove()

                obstacle = False

                if not __isRunning:
                    continue

                


#Run child thread
th = threading.Thread(target=move)
th.setDaemon(True)
th.start()


if __name__ == '__main__':
    init()
    start()

    distance_data = []
    Threshold = 15

    while True:
        # th.join()
        # Ultrasonic sensor measurements
        dist = HWSONAR.getDistance() / 10.0

        distance_data.append(dist)

        if len(distance_data) > 5:
            distance_data.pop(0)

        distance = np.mean(distance_data)

        if distance <= Threshold:
            obstacle = True

            print("Distance to obstacle:\n")
            print(distance)
            print("Reached obstacle!\n")
            time.sleep(0.5)
        else:
            obstacle = False
        time.sleep(0.03)



