#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/pi/mse112-ws-student/MasterPi/')
import time
import signal
import HiwonderSDK.mecanum as mecanum

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)
    


chassis = mecanum.MecanumChassis()

start = True
#Process before stopping
def Stop(signum, frame):
    global start

    start = False
    print('Turning off...')
    chassis.set_velocity(0,0,0)  # Turn off all motors
    

signal.signal(signal.SIGINT, Stop)

if __name__ == '__main__':
    # while start:

    # move left
    chassis.set_velocity(50,180,0)
    time.sleep(1)
    print("complete, now turning off motors\n")
    # chassis.set_velocity(0,0,0)  # Turn off all motors

    # move forward
    chassis.set_velocity(50,90,0)
    time.sleep(1)
    print("complete, now turning off motors\n")
    # chassis.set_velocity(0,0,0)  # Turn off all motors

    # move right
    chassis.set_velocity(50,0,0)
    time.sleep(2)
    print("complete, now turning off motors\n")
    chassis.set_velocity(0,0,0)  # Turn off all motors

    # chassis.set_velocity(50,0,0)
    # time.sleep(1)
    # chassis.set_velocity(50,270,0)
    # time.sleep(1)
    # chassis.set_velocity(50,180,0)
    # time.sleep(1)
    # chassis.set_velocity(0,0,0)  # Turn off all motors
    # print('已关闭')

        
