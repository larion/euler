#! /usr/bin/python

from math import sqrt, ceil
import itertools

def primes(maxprime):
    """ generator that yields the primes under maxprime:

        >>> list(primes(20))
        [2, 3, 5, 7, 11, 13, 17, 19]
        """
    # sieve of eratosthenes
    nums = [True]*(maxprime+1)
    upto = ceil(sqrt(maxprime)) #we only need to check up to this number
    for n in range(2, maxprime+1):
        if not nums[n]: # not a prime, already filtered out
            continue
        yield n 
        if n <= upto:
            # filter out multiples of n
            for notprime in range(n,maxprime+1,n):
                nums[notprime] = False

def factorize(num):
    """ factorize a number, return the factorization as a list:

    >>> factorize(15) #15 = 2^0*3^1*5^1
    [0, 1, 1]
    >>> factorize(100) #100 = 2^2*3^0*5^2
    [2, 0, 2]
    >>> factorize(1250) #1250 = 2^1*3^0*5^4
    [1, 0, 4]
    """
    result = []
    for p in primes(num):
        result.append(0)
        while num % p == 0: #calculate exponent by repeated division
            num/=p
            result[-1]+=1
        if num == 1: #base case
            break
    return result

def lcm(*nums):
    """ return the least common multiple of an arbitrary list of numbers

    >>> lcm(2,3)
    6
    >>> lcm(100)
    100
    >>> lcm(10,100)
    100
    >>> lcm(*range(1,11))
    2520
    """
    factorization = []
    fact_list = []
    for num in nums:
        fact_list.append(factorize(num))
    maxlen = max([len(fact) for fact in fact_list]) 
    # the first maxlen primes will definitely be all under maxlen^2
    prime_bases = primes(maxlen**2) 
    for n in range(maxlen):
        max_exponent = 0
        for fact in fact_list:
            try:
                max_exponent = max(max_exponent, fact[n])
            except IndexError:
                pass
        factorization.append(max_exponent)
    return reduce(lambda x,y: x*prime_bases.next()**y, [1]+factorization)

def euler5(k):
    """ return the least common multiple of the first k natural
    numbers """
    return lcm(*range(1,k+1))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print "k=10"
    print euler5(10)
    print "k=20:"
    print euler5(20)
    print "k=100:"
    print euler5(100)
    print "k=1000:"
    print euler5(1000)
    print "k=2000:"
    print euler5(2000)
