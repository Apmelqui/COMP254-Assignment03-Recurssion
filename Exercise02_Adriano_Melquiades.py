# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 17:15:58 2022

@author: apmel
"""

'''
Write a short recursive Java method that determines if a string s is a palindrome, that is, it is equal to its reverse. 
Examples of palindromes include 'racecar' and 'mom'. Test the method by asking the user to provide string entries to be checked. 
Hint: Check the equality of the first and last characters and recur 
(but be careful to return the correct value for both odd and even-length strings).
'''


def is_palindrome(string):
    #stop condition
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and is_palindrome(string[1:-1])



if __name__ == '__main__':
        
    user_input = input("Please enter a word: ")
    
    result = is_palindrome(user_input)
    
    if result == True:
        print(f'Yes, {user_input} is a palindrome')
    else:
        print(f'No, {user_input} is not a palindrome')
    
    
    