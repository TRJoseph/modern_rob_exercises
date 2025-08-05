"""
Thomas Joseph
Exercise 4.2
Computes the end-effector configuration T in SE(3) of a RRRP SCARA robotic arm
"""

import numpy as np
import sys
from modern_robotics import FKinSpace, FKinBody


def solve():
    #matrix = np.array([list(map(float, line.strip().split())) for line in data])


    # angles of joints at zero configuration from angle 0 to angle n
    theta_list = [0, np.pi/2, -np.pi/2, 1]

    # this list holds each screw axis in the zero configuration in fixed frame representation
    Slist = np.array([[0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 1, 2, 0, 0], [0, 0, 0, 0, 0, 1]]).T

    # this list holds each screw axis in the zero configuration in the body frame representation
    BList = np.array([[0, 0, 1, -2, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1]]).T

    # M is the transformation matrix of the end effector frame
    M = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 2], 
                 [0, 0, 1, 1], 
                 [0, 0, 0, 1]])
    

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
