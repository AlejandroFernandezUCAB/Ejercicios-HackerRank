#!/bin/python

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    repite = 0
    repiteAux = 0

    for j in ar:
        for k in ar:
            if( k == j):
                repiteAux = repiteAux + 1
        
        if( repiteAux > repite):
            repite = repiteAux
        repiteAux = 0

    return repite
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')
    print str(result)
    fptr.close()