'''
Question Url: https://www.hackerrank.com/challenges/strong-password/problem
'''
# Program

import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    dig = up = lo = sp = 0
    count = 0
    for i in range(n):
        if password[i].isupper():
            up = 1
        if password[i].islower():
            lo = 1
        if password[i].isnumeric():
            dig = 1
        if password[i] in '!@#$%^&*()-+':
            sp = 1
    if up == 1:
        count += 1
    if lo == 1:
        count += 1
    if dig == 1:
        count += 1
    if sp == 1:
        count += 1
    final = 4 - count 
    if (n + final) >= 6: 
        return final
    else:
        ad =  6 - (n + final)
        final += ad
        return final

if __name__ == '__main__':

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)
    
    print(answer)
