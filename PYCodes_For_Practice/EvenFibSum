#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 00:36:39 2018

@author: rocia
"""

'''

Find the sum of all the even numbers in the fibonacci series that do not exceed 4 million.

'''




def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

def compute():
    fiblst, sum  = [fib(2)], 0
    n = 3
    while fiblst[-1]<4000000:
        fiblst.append(fib(n))
        n += 1
        
    for x in fiblst:
        if x % 2 == 0:
            sum += x
    return sum

            
    
if __name__ == "__main__":
    print(compute())