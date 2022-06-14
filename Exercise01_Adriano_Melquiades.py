# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 20:26:30 2022

@author: apmel
"""

'''
Create a recursive algorithm to compute the product of two positive integers, m and n, using only addition and subtraction. 
Implement the Java or Python code. Hint: You need subtraction to count down from m or n and addition to do the arithmetic 
needed to get the right answer. 
'''

def product(m, n):
    if m == 0 or n == 0:
        return 0
    #stop condition
    elif n == 1:
        return m
    else:
        return m + product(m, n - 1)        
    
    

if __name__ == '__main__':    
    m = int(input("Please, enter first number: "))
    n = int(input("Please, enter second number: "))
    
    result = product(m, n)

    print(result)