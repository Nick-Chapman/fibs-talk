
# code fragments used in the talk

# original slow (exponential) version
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

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

# quick (linear) version; coded using a loop
def qfib(n):
    if n == 0: return 0
    if n == 1: return 1
    a,b = 0,1
    step = 1
    while (step < n):
        new = a+b
        a,b = b,new
        step = step + 1
    return b

# using fib to compute phi
phi = qfib(200) / qfib(199)

# quick (linear) version; coded using tail recursion
def tfibW (a,b,step):
    if step == 0: return b
    return tfibW (b, a+b, step-1)

def tfib(n):
    return tfibW(0,1,n-1)
