#! /usr/bin/python

import math

C = 600851475143
p_factors = [1]

for factor in range(2, int(math.sqrt(C))):
    while not C % factor:
        C /= factor
        if p_factors[-1]!=factor:
            p_factors.append(factor)

print p_factors

print "---"

print p_factors[-1]
