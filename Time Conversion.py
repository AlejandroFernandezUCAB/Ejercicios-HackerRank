#!/bin/python

from __future__ import print_function

import os
import sys
 
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #Transformando a numero
    numero = int( s[0] + s[1] )
    array = s.split(':')
    aux = numero
    if array[2][2] + array[2][3] == "PM":
        
        if numero != 12:
            numero = numero + 12
        
        array[0] = str(numero)
        
        array[2] = str(array[2][0]) + str(array[2][1])
        
    else:
        if numero == 12:
            array[0] = str(0) + str(0)
        array[2] = str(array[2][0]) + str(array[2][1])


    return str(array[0]) + ":" + str(array[1]) + ':' + str(array[2])

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = timeConversion(s)
    print( str(result) )
     
    #f.write(result + '\n')

    #f.close()
