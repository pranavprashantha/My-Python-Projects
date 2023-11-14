'''
A square number is an integer 𝑛 which can be written as the square of another integer 𝑚. For example,
9 is a square number, because 9 = 32. The integer 8 is not a square number, because √8 = 2.82824 ...
is not an integer. All square numbers are positive, because the square of a negative integer is positive.
Zero is also considered a square number, because 02 = 0. It can be proved that any positive integer can
be written as the sum of four square numbers, where you are allowed to repeat squares in the set of
four. Here are a few examples

ChatGPT (GPT-3.5) was given the following prompt:

Write a Python function that takes as an argument a positive integer and returns a list of four numbers
that when squared add up to the positive integer of interest

The response is provided in the template program named sum_squares.py posted on Canvas and
zyBooks. Unfortunately, this code does not work for many numbers, and for very large numbers the
code is extremely slow. Modify the function named list_nums to produce correct output in a reasonable
amount of computational time. The function should take in as a parameter a positive integer and return
a list of four (4) numbers that when squared add up to the positive integer of interest. Please comment
out any input() statements before submitting. It's okay to have print() statements, but they will
be ignored. If your submitted code is faster than ChatGPT you will receive 1 bonus point.
'''
from time import time
import math

def list_nums(n):
    '''chatgpt solution'''
    for a in range(0, math.ceil(math.sqrt(n))):
        for b in range(a, math.ceil(math.sqrt(n))):
            for c in range(b, math.ceil(math.sqrt(n))):
                for d in range(c, math.ceil(math.sqrt(n))):
                    if a**2 + b**2 + c**2 + d**2 == n:
                        return [a, b, c, d]

# how to measure how long your function takes to run:
t1 = time() # get start time
print(list_nums(72272)) # run function
t2 = time() # get end time
print(f"This took {t2-t1} seconds") # print result
