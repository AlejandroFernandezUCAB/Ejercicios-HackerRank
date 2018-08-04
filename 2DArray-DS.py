#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    j = 0
    k = 0
    sumaAlta = 0
    sumaAux = 0
    suiche = True
    #Columna
    while ( j < 6):
        
        arrK = arr[j]
        k=0

        while( k < 6):
            #Procesamiento
            if( (j+2 < len(arr)) and (k+2) < len(arrK)):
                sumaAux = arr[k][j] + arr[k][j+1] + arr[k][j+2]
                sumaAux = arr[k+1][j+1] + sumaAux
                sumaAux = arr[k+2][j] + arr[k+2][j+1] + arr[k+2][j+2] + sumaAux

                if(suiche == True):
                    sumaAlta = sumaAux
                    suiche = False
                elif (sumaAlta < sumaAux ):
                    sumaAlta = sumaAux

            k = k+1

        j = j+1

    return sumaAlta

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)
    print( result )
    #fptr.write(str(result) + '\n')

    #fptr.close()
