#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    
    i = 0
    puntosA = 0
    puntosB = 0
    
    for i in range(0,3):
        print i 
        if ( a[i] > b[i]):
            puntosA = puntosA + 1
        if ( a[i] < b[i]):
            puntosB = puntosB + 1
    
    return [ puntosA, puntosB ]
                        
        
if __name__ == '__main__':


    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    result = solve(a, b)

    print (' '.join(map(str, result)))
    print ('\n')

