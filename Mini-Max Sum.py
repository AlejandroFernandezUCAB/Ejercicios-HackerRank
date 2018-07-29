#!/bin/python

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minimo = 0
    maximo = 0
    aux = 0
    suiche = False
    for x in range(len(arr)):

        for y in range(len(arr)):
                
            if ( x != y ):
                aux = aux  + arr[y]
        
        if( suiche == False):
            minimo = aux
            maximo = aux
            suiche = True

        if( aux < minimo ):
            minimo = aux
        
        if( aux > maximo ):
            maximo = aux

        aux = 0 
    
    print str( minimo ) + " " + str( maximo )


if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())
    miniMaxSum(arr)