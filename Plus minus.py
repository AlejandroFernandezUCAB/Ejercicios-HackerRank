#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positivos = 0
    negativos = 0
    ceros = 0
    for x in arr:
        if x > 0:
            positivos = positivos + 1
        elif x < 0:
            negativos = negativos + 1
        else:
            ceros = ceros + 1

    print format(positivos/len(arr), '.6f')
    print str(negativos/len(arr) )
    print str(ceros/len(arr))

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)