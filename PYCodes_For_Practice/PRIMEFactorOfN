#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 00:59:28 2018

@author: rocia
"""
'''

Find the largest Prime factor of a given Number

'''
import math

def primeFactor(n): 
    lst= []
    while n % 2 == 0: 
        n = n / 2 
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            lst.append(i)
            n = n / i 
    return (lst)

        
        
if __name__ == "__main__":
    N = 600851475143
    #N = int(input("Enter the number whose largest PrimeFactor must be found"))
    print(max(primeFactor(N)))