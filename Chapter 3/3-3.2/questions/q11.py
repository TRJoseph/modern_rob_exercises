"""
Thomas Joseph
Question 11 Modern Robotics
Computes the matrix exponential of a skew-symmetric matrix
"""

import numpy as np
import sys, os
from modern_robotics import MatrixExp3

DEBUG = True
INPUT_FILE = os.path.join(os.path.dirname(__file__), "../data/input_q11.txt")


def read_input():
    """Reads input from a file or standard input."""
    if INPUT_FILE:
        with open(INPUT_FILE, 'r') as f:
            data = f.read().strip().splitlines()
    else:
        data = sys.stdin.read().strip().splitlines()
    return data


def main():
    data = read_input()

    matrix = np.array([list(map(float, line.strip().split())) for line in data])

    if DEBUG:
        print("Input matrix S:")
        print(data)

    R = MatrixExp3(matrix)

    print("Matrix exponential of S (R):")
    print(R)

    # optionally save to a file
    #np.savetxt("../data/output_q10.txt", R, fmt="%.4f")

if __name__ == "__main__":
    main()
