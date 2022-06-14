# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:59:04 2022

@author: apmel
"""

#Write a recursive method that takes a string as argument and determines if the string has more vowels than consonants. 
#Test the method by asking the user to enter a string. Hint: Write your recursive method to first count vowels and consonants.



def number_of_vowels(string):
    vowels = ('a', 'e', 'i', 'o','u')
    #stop condition: checking if there is any letter in the string (is the string empty?)
    if not string: #similar to len(string) == 0
        return 0
    elif string[0].lower() in vowels:
        return 1 + number_of_vowels(string[1:])
    else:
        return number_of_vowels(string[1:])
        
    
def number_of_consonants(string):
    vowels = ('a', 'e', 'i', 'o','u')
    #stop condition: checking if there is any letter in the string (is the string empty?)
    if not string: 
        return 0
    elif string[0].lower() not in vowels:
        return 1 + number_of_consonants(string[1:])
    else:
        return number_of_consonants(string[1:])


def has_more_vowels(string):
    vowels = number_of_vowels(string)
    consonants = number_of_consonants(string)
    if vowels > consonants:
        return True
    else:
        return False


if __name__ == '__main__':   
    
    user_input = input("Please, enter a word: ")

    number_of_consonants(user_input)
    number_of_vowels(user_input)

    result = has_more_vowels(user_input)
    print(f'{result}, {user_input} does not have more vowels than consonants')


    