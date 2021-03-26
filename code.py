
# code fragments used in the talk

def fib(n):
    if n < 2: return n
    else: return fib(n-1) + fib(n-2)

def sequence():
    for i in range(1,35):
        answer = fib(i)
        print (i, answer)

import time

def timed_sequence():
    for i in range(1,35):
        start = time.time()
        answer = fib(i)
        end = time.time()
        print (i, answer, end - start)

import math
phi = (math.sqrt(5)+1)/2

def qfib(n):
    if n < 2: return n
    else:
        a, b, i  = 0, 1, 1
        while (i < n):
            c = a + b
            a, b, i = b, c, i+1
        return b

def sequence200():
    for i in range(1,201):
        answer = qfib(i)
        print (i, answer)
