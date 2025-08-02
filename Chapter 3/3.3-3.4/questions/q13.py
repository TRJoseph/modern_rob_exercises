"""
Thomas Joseph
Question 13 Modern Robotics
Computes the normalized screw axis representation S of the screw described by a unit vector s, located at p, with a pitch h
"""

import numpy as np
import sys, os, re
from modern_robotics import ScrewToAxis

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


def solve():
    # unit vector s in the direction of the screw axis
    s = np.array([1, 0, 0])
    # point p of the screw
    p = np.array([0, 0, 2])
    # pitch h of the screw 
    h = 1

    norm_rep = ScrewToAxis(p,s,h)

    print("Normalized screw axis representation S of the screw.")
    print(norm_rep)
    
    # optionally save to a file
    #np.savetxt("../data/output_q10.txt", R, fmt="%.4f")

def main():
    try:
        solve()
    except:
        print("Invalid input data format. Try Again")

if __name__ == "__main__":
    main()
