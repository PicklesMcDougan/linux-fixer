#!/bin/python3
import sys
from time import sleep

def progress_bar():
    for i in range(21):
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
        sys.stdout.flush()
        sleep(.25)
    
progress_bar()
print ("\nProblems Resolved")
