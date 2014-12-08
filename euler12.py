#! /usr/bin/env python

from euler5 import factorize
from itertools import count
from operator import mul

# TODO
#
# precalculate prime table
# use that T(n) = n*(n+1)/2 and that n and n+1 is always co-prime
#

def count_divisors(factorization):
    """ Count the number of divisors of a natural number based on its
    prime factorization.
    >>> count_divisors(factorize(10)) #1, 2, 5, 10
    4
    >>> count_divisors(factorize(7)) #1, 7
    2
    >>> count_divisors(factorize(1)) #1
    1
    >>> count_divisors(factorize(90)) # 1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90
    12
    """
    return reduce(mul, map(lambda x: x+1, factorization), 1)

def count_triangular_divisors(start):
    """ Generate the number of divisors of triangular numbers
    starting from the n-th one. Tn = n*(n+1)/2.
    >>> gen = count_triangular_divisors(1)
    >>> next(gen) #1: 1
    1
    >>> next(gen) #3: 1, 3
    2
    >>> next(gen) #6: 1, 2, 3, 6
    4
    >>> next(gen) #10: 1, 2, 5, 10
    4
    >>> next(gen) #15: 1, 3, 5, 15
    4
    >>> next(gen) #21: 1, 3, 7, 21
    4
    >>> next(gen) #28: 1, 2, 4, 7, 14, 28
    6
    """
    current = factorize(triangular(start))
    yield count_divisors(current)
    for n in count(start+1):
        # Use the fact that T(n) = (n+1)/(n-1) * T(n-1)
        higher = factorize(n+1) 
        lower = factorize(n-1)
        pad(0, current, lower, higher)
        current = [val_curr + higher[ind] - lower[ind] for ind, val_curr in enumerate(current)]
        #assert count_divisors(current) == count_divisors(factorize(triangular(n)))
        yield count_divisors(current)

def pad(padding, *args):
    """ Pad all the arguments to be the same length (which will be the
    length of the longest iterable). The value of padding will be used
    for the new cells. 
    >>> pad(0, [1,2,3], [1], [6, 9, 127, 4, 82])
    ([1, 2, 3, 0, 0], [1, 0, 0, 0, 0], [6, 9, 127, 4, 82])
    """
    maxlength = max([len(lst) for lst in args])
    for lst in args:
        while len(lst) != maxlength:
            lst.append(padding)
    return args

def triangular(n):
    """ Return the n-th triangular number. Tn = n*(n+1)/2. """
    return n*(n+1)/2

def euler12():
    """ Solve the 12th puzzle on Project Euler. """
    for n, divisor_count in enumerate(count_triangular_divisors(1), 1):
        # print "{!s}, {!s}: {!s}".format(n, triangular(n), divisor_count)
        if divisor_count > 500:
            return "{!s}: {!s}".format(n, triangular(n))

if __name__ == "__main__":
    import doctest; doctest.testmod()
    print euler12()
