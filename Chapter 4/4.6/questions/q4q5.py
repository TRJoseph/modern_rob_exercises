"""
Thomas Joseph
Modern Robotics Chapter 4 Assignment Question 4 and Question 5
Computes the end-effector configuration T in SE(3) given L=1 and joint variables theta
"""

import numpy as np
import sys, os, re
from modern_robotics import FKinSpace, FKinBody

def solve():
    #matrix = np.array([list(map(float, line.strip().split())) for line in data])
    np.set_printoptions(suppress=True, precision=3)
    # angles of joints at zero configuration from angle 0 to angle n
    theta_list = [-np.pi/2, np.pi/2, np.pi/3, -np.pi/4, 1, np.pi/6]

    # this list holds each screw axis in the zero configuration in fixed frame representation
    Slist = np.array([[0,0,0,0,0,0],[0,1,1,1,0,0],[1,0,0,0,0,1],[0,0,1,1-np.sqrt(3),0,0],[-1,0,0,0,0,-(2+np.sqrt(3))],[0,1,1+np.sqrt(3),2+np.sqrt(3),1,0]])

    # this list holds each screw axis in the zero configuration in the body frame representation
    BList = np.array([[0,0,0,0,0,0],[0,1,1,1,0,0],[1,0,0,0,0,1],[0,2.732,3.732,2,0,0],[2.732,0,0,0,0,0],[0,-2.732,-1,0,1,0]])

    # M is the transformation matrix of the end effector frame
    M = np.array([[1,0,0,2+np.sqrt(3)],[0,1,0,0],[0,0,1,1+np.sqrt(3)],[0,0,0,1]])

    # returns the end effector configuration based on known joint positions
    EE_Pos_Space = FKinSpace(M, Slist, theta_list)

    EE_Pos_Body = FKinBody(M, BList, theta_list)

    print("End-effector configuration T in SE(3) from space coords:")
    print(EE_Pos_Space)
    print("End-effector configuration T in SE(3) from body coords:")
    print(EE_Pos_Body)
    
    # optionally save to a file
    #np.savetxt("../data/output_q10.txt", R, fmt="%.4f")

def main():
    try:
        solve()
    except:
        print("Invalid input data format. Try Again")

if __name__ == "__main__":
    main()
