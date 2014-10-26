#! /usr/bin/python

import itertools
from math import sqrt

# With some algebra:
#   a + b - (ab/1000) = 500
# a and b is an integer so ab must be divisible by 1000

def euler9():
    for result in itertools.count(501):
        # suppose a + b = result
        for a in range(result-1, 1, -1):
            b = result-a
            if (a*b)%1000:
                continue
            lhs = a + b - (a*b/1000) 
            if lhs < 500:
                continue
            elif lhs == 500:
                return (a, b, int(sqrt(a**2+b**2)))
            #elif lhs > 500:
            #    break

if __name__=="__main__":
    variables = euler9()
    print "a={!s}, b={!s}, c={!s}".format(*variables)
    product = reduce(lambda x,y: x*y, variables)
    print "a*b*c={!s}".format(product)
    


