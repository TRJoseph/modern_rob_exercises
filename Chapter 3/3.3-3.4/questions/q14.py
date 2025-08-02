"""
Thomas Joseph
Question 14 Modern Robotics
Computes the homogeneous transformation matrix T corresponding to the matrix exponential of an input matrix in se(3)
"""

import numpy as np
import sys, os, re
from modern_robotics import MatrixExp6

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


def solve(data):
    matrix = np.array([list(map(float, line.strip().split())) for line in data])

    homogen_mat = MatrixExp6(matrix)
    homogen_mat[np.abs(homogen_mat) < 1e-5] = 0  # Set tiny values to 0

    print("homogeneous transformation matrix T:")
    print(homogen_mat)
    
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
    except:
        print("Invalid input data format. Try Again")

if __name__ == "__main__":
    main()
