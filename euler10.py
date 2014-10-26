#! /usr/bin/env python

from euler5 import primes

def euler10():
    """ solve the tenth problem on Project Euler """
    return sum(primes(2000000))

print euler10()
