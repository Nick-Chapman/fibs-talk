
# code fragments used in the talk

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    else: return fib(n-1) + fib(n-2)

def seq():
    for i in range(1,38):
        answer = fib(i)
        print (i, answer)

import time

def seqTimed():
    for i in range(1,38):
        start = time.time()
        answer = fib(i)
        end = time.time()
        print (i, answer, end - start)

def qfib(n):
    if n == 0: return 0
    if n == 1: return 1
    a,b = 0,1
    step = 1
    while (step < n):
        new = a+b
        a = b
        b = new
        step = step + 1
    return b

def seq200():
    for i in range(1,201):
        answer = qfib(i)
        print (i, answer)
