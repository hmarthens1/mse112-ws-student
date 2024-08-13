#!/usr/bin/env python3
# encoding:utf-8
import sys
sys.path.append('/home/pi/mse112-ws/MasterPi/')
import time
import numpy as np
from math import sqrt
from ArmIK.InverseKinematics import *
from ArmIK.Transform import getAngle
from HiwonderSDK.Board import setBusServoPulse,getBusServoPulse, setPWMServoPulse, getPWMServoPulse

#The robot arm moves according to the angle calculated by inverse kinematics
ik = IK('arm')
#Set the connecting rod length


class ArmIK:
    servo3Range = (500, 2500.0, -90.0, 90.0) #Pulse width, angle
    servo4Range = (500, 2500.0, -90.0, 90.0)
    servo5Range = (500, 2500.0, -90.0, 90.0)
    servo6Range = (500, 2500.0, -90.0, 90.0)

    def __init__(self):
        self.setServoRange()

    def setServoRange(self, servo3_Range=servo3Range, servo4_Range=servo4Range, servo5_Range=servo5Range, servo6_Range=servo6Range):
        # Adapt to different servos
        self.servo3Range = servo3_Range
        self.servo4Range = servo4_Range
        self.servo5Range = servo5_Range
        self.servo6Range = servo6_Range
        self.servo3Param = (self.servo3Range[1] - self.servo3Range[0]) / (self.servo3Range[3] - self.servo3Range[2])
        self.servo4Param = (self.servo4Range[1] - self.servo4Range[0]) / (self.servo4Range[3] - self.servo4Range[2])
        self.servo5Param = (self.servo5Range[1] - self.servo5Range[0]) / (self.servo5Range[3] - self.servo5Range[2])
        self.servo6Param = (self.servo6Range[1] - self.servo6Range[0]) / (self.servo6Range[3] - self.servo6Range[2])

    def transformAngleAdaptArm(self, theta3, theta4, theta5, theta6):
        #Convert the angle calculated by inverse kinematics into the pulse width value corresponding to the servo
        servo3 = int(round((theta3) * self.servo3Param + (self.servo3Range[1] + self.servo3Range[0])/2))
        if servo3 > self.servo3Range[1] or servo3 < self.servo3Range[0]:
            logger.info('servo3(%s)Out of range(%s, %s)', servo3, self.servo3Range[0], self.servo3Range[1])
            return False

        servo4 = int(round(-(theta4) * self.servo4Param + (self.servo4Range[1] + self.servo4Range[0])/2))
        if servo4 > self.servo4Range[1] or servo4 < self.servo4Range[0]:
            logger.info('servo4(%s)Out of range(%s, %s)', servo4, self.servo4Range[0], self.servo4Range[1])
            return False

        servo5 = int(round((self.servo5Range[1] + self.servo5Range[0])/2 + (90-theta5) * self.servo5Param)) 
        if servo5 > self.servo5Range[1] or servo5 < self.servo5Range[0]:
            logger.info('servo5(%s)Out of range(%s, %s)', servo5, self.servo5Range[0], self.servo5Range[1])
            return False
        

        servo6 = int(round((theta6) * self.servo6Param + (self.servo6Range[1] + self.servo6Range[0])/2))
        if servo6 > self.servo6Range[1] or servo6 < self.servo6Range[0]:
            logger.info('servo6(%s)Out of range(%s, %s)', servo6, self.servo6Range[0], self.servo6Range[1])
            return False

        return {"servo3": servo3, "servo4": servo4, "servo5": servo5, "servo6": servo6}

    def servosMove(self, servos, movetime=None):
        #Drive servos 3, 4, 5, and 6 to rotate
        time.sleep(0.02)
        if movetime is None:
            max_d = 0
            for i in  range(0, 4):
                d = abs(getPWMServoPulse(i + 3) - servos[i])
                if d > max_d:
                    max_d = d
            movetime = int(max_d*1)
        setPWMServoPulse(3, servos[0], movetime)
        setPWMServoPulse(4, servos[1], movetime)
        setPWMServoPulse(5, servos[2], movetime)
        setPWMServoPulse(6, servos[3], movetime)
        
#         setPWMServosPulse(movetime, 4, 3,servos[0], 4,servos[1], 5,servos[2], 6,servos[3])

        return movetime

    def setPitchRange(self, coordinate_data, alpha1, alpha2, da = 1):
        #Given the coordinate_data and pitch angle ranges alpha1, alpha2, automatically find a suitable solution within the range
         #If there is no solution, return False, otherwise return the corresponding servo angle and pitch angle
         #The coordinate unit is cm, passed in as a tuple, for example (0, 5, 10)
         #da is the angle that increases each time when traversing the pitch angle
        x, y, z = coordinate_data
        if alpha1 >= alpha2:
            da = -da
        for alpha in np.arange(alpha1, alpha2, da):#Traversal solution
            result = ik.getRotationAngle((x, y, z), alpha)
            if result:
                theta3, theta4, theta5, theta6 = result['theta3'], result['theta4'], result['theta5'], result['theta6']               
                servos = self.transformAngleAdaptArm(theta3, theta4, theta5, theta6)
                # print("printing angles:\n")
                # print(servos)
                if servos != False:
                    return servos, alpha

        return False

    def setPitchRangeMoving(self, coordinate_data, alpha, alpha1, alpha2, movetime = None):
        #Given coordinates coordinate_data and pitch angle alpha, as well as the pitch angle range alpha1, alpha2, automatically find the solution closest to the given pitch angle and move to the target position
        #If there is no solution, return False, otherwise return the servo angle, pitch angle, and running time
        #Coordinate unit cm, passed in as a tuple, for example (0, 5, 10)
        #alpha is the given pitch angle
        #alpha1 and alpha2 are the range of pitch angles
        #movetime is the servo rotation time, in ms, if the time is not given, it is automatically calculated
        x, y, z = coordinate_data
        result1 = self.setPitchRange((x, y, z), alpha, alpha1)
        result2 = self.setPitchRange((x, y, z), alpha, alpha2)
        if result1 != False:
            data = result1
            if result2 != False:
                if abs(result2[1] - alpha) < abs(result1[1] - alpha): #choose the result that has the closest to correct alpha
                    data = result2
        else:
            if result2 != False:
                data = result2
            else:
                return False
        servos, alpha = data[0], data[1]
        movetime = self.servosMove((servos["servo3"], servos["servo4"], servos["servo5"], servos["servo6"]), movetime)
        return servos, alpha, movetime
 
if __name__ == "__main__":

    AK = ArmIK()

    # print(ik.getRotationAngle((18, 0, 0), 90))
    for i in range(3):
        # AK.setPitchRangeMoving((0, 22, 4),0,-180, 180,1000)
        # time.sleep(2)
        # AK.setPitchRangeMoving((0, 20, 4),0,-180, 180,1000)
        # time.sleep(2)
        # AK.setPitchRangeMoving((0, 18, 4),0,-180, 180,1000)
        time.sleep(2)
        AK.setPitchRangeMoving((-(ik.l2+ik.l3+ik.l4),0,ik.l1),0,-180,180,2000)