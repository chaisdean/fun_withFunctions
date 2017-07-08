import math
import numpy as np
from numpy import multiply, product
# Assignment: Fun with Functions
# Create a series of functions based on the below descriptions.
#
# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
#

# def odd_even(count):
#
#     for count in range(1,2000):
#         print count
#         if (count%2 == 0):
#             print("it's an even number!")
#         else:
#             print("it's an odd number!")
#
# print odd_even(2)


# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
#
# def multiply_something():
#     a =[2,4,10,16]
#     b = multiply(a, 5)
#     print b
#
# print multiply_something()

# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the number of 1's as the number in the original list. Here's an example:

def something_multiply(new_function):
    print new_function
    new_list = []
    for a in new_function:
        val_list = []
        for b in range(0,a):
            val_list.append(1)
        new_list.append(val_list)
    return new_list

c = something_multiply(multiply([2,4,5],3))
print c
