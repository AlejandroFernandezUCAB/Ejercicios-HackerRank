#!/bin/python

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    retorno = 0
    for x in ar:
        print x
        retorno = retorno + x
    return retorno

if __name__ == '__main__':


    ar_count = int(raw_input())

    ar = map(long, raw_input().rstrip().split())

    result = aVeryBigSum(ar)

    print (str(result) + '\n')
