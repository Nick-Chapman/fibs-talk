
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

import time

def seq():
    for i in range(1,41):
        a = time.time()
        answer = fib(i)
        b = time.time()
        print (i, answer, b-a)

def qfib(n):
    if n == 0: return 0
    if n == 1: return 1
    a,b = 0,1
    step = 1
    while (step < n):
        new = a + b
        step = step + 1
        a,b = b,new
    return b
