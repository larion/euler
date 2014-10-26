#! /usr/bin/python

from math import log
from euler5 import primes

def euler6(k):
    """ Return the k-th prime number.

    >>> euler6(2)
    3
    >>> euler6(5)
    11
    >>> euler6(10)
    29
    """
    # For the upper bound see:
    # http://en.wikipedia.org/wiki/Prime-counting_function#Inequalities
    upper_bound = int(k*log(k*log(k))) if k >= 6 else 15
    prime_gen = primes(upper_bound)
    for _ in range(k-1): prime_gen.next()
    return prime_gen.next()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print euler6(10001)
