#!/usr/bin/env python3
# encoding: utf-8
# Inverse kinematics of a 4-DOF robot: Given the corresponding coordinates (X, Y, Z) and pitch angle, calculate the rotation angle of each joint
# 2020/07/20 Aiden
import logging
from math import *

# CRITICAL, ERROR, WARNING, INFO, DEBUG
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class IK:
    # Count the servos from bottom to top
    # Count the servos from bottom to top
    l1 = 8.0    #The distance from the center of the robot chassis to the center axis of the second servo is 8cm
    l2 = 6.0  #The distance from the second servo to the third servo is 6cm
    l3 = 6.20    #The distance from the third servo to the fourth servo is 6.2cm
    l4 = 10.00    


    def __init__(self, arm_type): #According to different types of clamps, adapt parameters
        self.arm_type = arm_type


    def setLinkLength(self, L1=l1, L2=l2, L3=l3, L4=l4):
        # Change the connecting rod length of the robot arm to adapt to robots of the same structure with different lengths
        self.l1 = L1
        self.l2 = L2
        self.l3 = L3
        self.l4 = L4


    def getLinkLength(self):
        # Get the current setting of the connecting rod length
        return {"L1":self.l1, "L2":self.l2, "L3":self.l3, "L4":self.l4}

    def getRotationAngle(self, coordinate_data, Alpha):
        # Given the specified coordinates and pitch angle, return the angle that each joint should rotate. If there is no solution, return False
         # coordinate_data is the coordinates of the end of the gripper. The coordinate unit is cm. It is passed in as a tuple, for example (0, 5, 10)
         # Alpha is the angle between the holder and the horizontal plane, in degrees

         # Let the end of the gripper be P(X, Y, Z), the coordinate origin be O, the origin is the projection of the gimbal center on the ground, and the projection of point P on the ground is P_
         # The intersection point of l1 and l2 is A, the intersection point of l2 and l3 is B, the intersection point of l3 and l4 is C
         # CD is perpendicular to PD, CD is perpendicular to the z-axis, then the pitch angle Alpha is the angle between DC and PC, AE is perpendicular to DP_, and E is on DP_, CF is perpendicular to AE, and F is on AE
         # Angle representation: For example, the angle between AB and BC is expressed as ABC

        X, Y, Z = coordinate_data
        theta6 = degrees(atan2(X, Y))
 
        P_O = sqrt(X*X + Y*Y) #P_distance to origin O
        CD = self.l4 * cos(radians(Alpha))
        PD = self.l4 * sin(radians(Alpha)) #When the pitch angle is positive, PD is positive, when the pitch angle is negative, PD is negative
        AF = P_O - CD
        CF = Z - self.l1 - PD
        AC = sqrt(pow(AF, 2) + pow(CF, 2))
        if round(CF, 4) < -self.l1:
            logger.debug('Height below0, CF(%s)<l1(%s)', CF, -self.l1)
            return False
        if self.l2 + self.l3 < round(AC, 4): #The sum of two sides is less than the third side
            logger.debug('Cannot form a connecting rod structure, l2(%s) + l3(%s) < AC(%s)', self.l2, self.l3, AC)
            return False

        #Looking for theta4
        cos_ABC = round((pow(self.l2, 2) + pow(self.l3, 2) - pow(AC, 2))/(2*self.l2*self.l3), 4) #Law of Cosines
        if abs(cos_ABC) > 1:
            logger.debug('Cannot form a connecting rod structure, abs(cos_ABC(%s)) > 1', cos_ABC)
            return False
        ABC = acos(cos_ABC) #Inverse trigonometry to find radians

        if CF > 0:
            zf_flag = 1
        else:
            zf_flag = -1
        
        theta4 = round(zf_flag*(180.0 - degrees(ABC)),4)

        #Find theta5
        CAF = acos(AF / AC)
        cos_BAC = round((pow(AC, 2) + pow(self.l2, 2) - pow(self.l3, 2))/(2*self.l2*AC), 4) #Law of Cosines
        if abs(cos_BAC) > 1:
            logger.debug('Cannot form a connecting rod structure, abs(cos_BAC(%s)) > 1', cos_BAC)
            return False

        theta5 = round(degrees(zf_flag*(CAF - acos(cos_BAC))),5)

        #Find theta3
        theta3 = round(Alpha - (theta5 + theta4),5)


        return {"theta3":theta3, "theta4":theta4, "theta5":theta5, "theta6":theta6} # Returns the angle dictionary if there is a solution
            
if __name__ == '__main__':
    ik = IK('arm')
    #ik.setLinkLength(L1=ik.l1 + 1.30, L4=ik.l4)
    # print('Connecting rod length:', ik.getLinkLength())
    print(ik.getRotationAngle((0, 0, ik.l1+ik.l2+ik.l3+ik.l4), 90))