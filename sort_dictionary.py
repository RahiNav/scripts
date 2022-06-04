#!/bin/python3

import math
import os
import random
import re
import sys
import operator



if __name__ == '__main__':
    s = input()

#Find the all the unique instances of a list    
unique = []
    
for i in s:
    if i not in unique:
        unique.append(i)

#Count the frequency of the all the unique values in the given string
#create a dictionary called frequency which has letter:frequency
count = 0
frequency = {}

s1 = ''
for i in unique:
    for j in s:
        if i == j:
            count = count + 1
        else:
            continue  
    frequency[i] = count
    count = 0    

#sort the  frequency dictionary first by frequency (values) in descending order and then by keys in ascending order. When both match print. 
#Make a dictionary of this order
   
letter = ''
value = 0
final = {}

for i in sorted(frequency.values(),reverse=True):
    for j in sorted(frequency.keys(), reverse = False):
        if frequency[j] == i:
            letter = j
            value = i
            final[letter] = value
            
#get first three key:value of this dictionary
logo = dict(list(final.items())[:3])

#print result
for l,v in logo.items():
    print(l,v)          
            
