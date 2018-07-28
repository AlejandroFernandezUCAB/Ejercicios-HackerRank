#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    escalera = n 
    piso = n
    habitacion = 1
    string = ""
    for y in range (n):
        for x in range(piso):
            #Si la suma de donde estoy parado mas la habitacion es igual a la hab full entonces 
            if (x + habitacion) >= (escalera):
                string = string + '#'    
            else:
                string = string + ' '
        habitacion = habitacion + 1        
        print string
        string = ""


if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
