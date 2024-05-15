#!/bin/python3

import sys


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    a, b = 0, 1
    sum_even_fib = 0
    while b < n:
        if b % 2==0:
            sum_even_fib+=b
        a, b = b, a + b
    print(sum_even_fib)
       
