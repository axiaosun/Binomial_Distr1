#!/usr/bin/env python3

#The ratio of boys to girls for babies born in Russia is 1.09 : 1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

import math

l, r = list(map(float, input().split(" ")))
prob = l/r

def factorial(n):
    n = int(n)
    return math.factorial(n)

def combinations(n, x):
    return factorial(n)/(factorial(x)*factorial(n-x))

def b(x, n, p):
    return combinations(n, x) * (p**x) * ((1-p)**(n-x))

print (round(sum([b(i, 6, prob/(1+prob)) for i in range(3,7)]), 3))
