# Complete the function below.
#!/bin/python

import sys
import os

def jobOffers(scores, lowerLimits, upperLimits):
    x = 0
    y = 0
    aux = 0
    q = len(lowerLimits)
    array = []
    contador = 0
    while( x < len(lowerLimits)):
        contador = 0
        y = 0
        while(y < len(scores)):

            if ((scores[y] >= lowerLimits[x]) and (scores[y] <= upperLimits[x])):
                contador = contador + 1
                

            y = y+ 1   
        array.append( contador )        
        x =x+1
        
    return array 

if __name__ == "__main__":
    #f = open(os.environ['OUTPUT_PATH'], 'w')
    scores_cnt = 0
    scores_cnt = int(raw_input())
    scores_i = 0
    scores = []
    while scores_i < scores_cnt:
        scores_item = int(raw_input())
        scores.append(scores_item)
        scores_i += 1


    lowerLimits_cnt = 0
    lowerLimits_cnt = int(raw_input())
    lowerLimits_i = 0
    lowerLimits = []
    while lowerLimits_i < lowerLimits_cnt:
        lowerLimits_item = int(raw_input())
        lowerLimits.append(lowerLimits_item)
        lowerLimits_i += 1


    upperLimits_cnt = 0
    upperLimits_cnt = int(raw_input())
    upperLimits_i = 0
    upperLimits = []
    while upperLimits_i < upperLimits_cnt:
        upperLimits_item = int(raw_input())
        upperLimits.append(upperLimits_item)
        upperLimits_i += 1


    res = jobOffers(scores, lowerLimits, upperLimits)
