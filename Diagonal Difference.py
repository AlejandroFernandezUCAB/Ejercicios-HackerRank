#!/bin/python

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(a):
    fila = 0
    columna = 0
    parte1 = 0
    parte2 = 0
    #Extrayendo la fila Parte 1
    while( fila < len(a) ):
        filaMatriz = a[ fila ]
        columna = 0
        while ( columna < len(filaMatriz) ):
            if fila == columna:
                parte1 = parte1 + filaMatriz[columna]
                print 'soy el centro' + str( filaMatriz[columna])
            columna = columna + 1
        fila = fila + 1

    fila = len(a) - 1
    fila2 = 0
    print 'soy fila' + str( fila)
    columna = 0
    #Extrayendo la fila Parte 2
    while( fila >= 0 ):
        filaMatriz = a[ fila ]
        columna = 0
        while ( columna < len(filaMatriz) ):
            if fila2 == columna:
                parte2 = parte2 + filaMatriz[columna]
                print 'soy el centro parte 2' + str( filaMatriz[columna] )
            columna = columna + 1
        fila2 = fila2 + 1
        fila = fila - 1

    return abs( parte1 - parte2 )  
            
    
if __name__ == '__main__':


    n = int(raw_input())

    a = []

    for _ in xrange(n):
        a.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(a)

    print (str(result) + '\n')
