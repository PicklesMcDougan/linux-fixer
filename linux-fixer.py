#!/bin/python3
import sys
from time import sleep
from tqdm import trange
import argparse

def progress_bar():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--amount', type=int, default=42, help='Modify progress bar (Default: 42)')
    args = parser.parse_args()
    for i in trange(args.amount):
        sleep(.05)

progress_bar()
print ("\nProblems Resolved")
