"""
Thomas Joseph
Question 12 Modern Robotics
Computes the se(3) matrix corresponding to a twist V
"""

import numpy as np
import sys, os, re
from modern_robotics import VecTose3

DEBUG = True

script_name = os.path.basename(__file__)  # e.g., 'q12_matrix_exp.py'

match = re.search(r"q(\d+)", script_name, re.IGNORECASE)
question_num = match.group(1) if match else "xx"  # fallback

# input file name
INPUT_FILE_NAME = f"../data/input_q{question_num}.txt"
OUTPUT_FILE_NAME = f"../data/output_q{question_num}.txt"

INPUT_FILE_PATH = os.path.join(os.path.dirname(__file__), INPUT_FILE_NAME)


def read_input():
    """Reads input from a file or standard input."""
    try:
        if INPUT_FILE_PATH:
            with open(INPUT_FILE_PATH, 'r') as f:
                data = f.read().strip().splitlines()
        else:
            data = sys.stdin.read().strip().splitlines()
        return data
    except:
        print(f"No input file: input_q{question_num} found.")
        return None

[[0,1,0,0],[-1,0,0,3],[0,0,1,-1],[0,0,0,1]]

def solve(data):
    # The se(3) representation of a matrix is simply the skew symmetric matrix of the angular velocity and the linear velocity vector (zeros in extra spaces to make it in R^4)
    vectorList = []
    for line in data:
        value = line.strip().split()
        vectorList.append(float(value[0]))

    vector = np.array(vectorList)
    se_3_rep = VecTose3(vector)

    print("Matrix se(3) representation of V:")
    print(se_3_rep)
    
    # optionally save to a file
    #np.savetxt("../data/output_q10.txt", R, fmt="%.4f")

def main():
    data = read_input()

    if data is None:
        return
    
    if DEBUG:
        print("Input matrix S:")
        print(data)

    try:
        solve(data)
    except Exception as e:
        print("Invalid input data format. Try Again")

if __name__ == "__main__":
    main()
