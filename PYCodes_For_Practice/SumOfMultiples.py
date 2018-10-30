#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 00:35:41 2018

@author: rocia
"""



'''

Find the sum of all the natural number multiples of 2 user inputs below 1000.

'''



import sys


def take_input():
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    if isvalid(a) and isvalid(b):
        return a,b
    else:
        sys.exit ("The entered numbers are Invalid. Please enter natural numbers below 1000")
        
def isvalid(a):
    if a<1000:
        return True
    else:
        return False


def compute_multiples(a, b):
    lst = [a,b]
    ret = []
    for x in lst:
        l = list(range(x,1000,x))
        ret += l
    return sum(set(ret))
        
            
            
    
if __name__ == "__main__":
    n1, n2 = take_input()
    print(compute_multiples(n1,n2))