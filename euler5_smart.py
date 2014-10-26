#! /usr/bin/python

from math import sqrt, ceil, floor, log

def primes(maxprime):
    """ generator that yields the primes under maxprime:

        >>> list(primes(20))
        [2, 3, 5, 7, 11, 13, 17, 19]
        """
    # sieve of Eratosthenes
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

def euler5(k):
    """ return the least common multiple of the first k natural
    numbers """
    upto = ceil(sqrt(k))
    prime_gen = primes(k)
    factorization = []
    current_p = prime_gen.next()
    while current_p <= upto:
        factorization.append(int(log(k,current_p)))
        current_p = prime_gen.next()
    factorization.append(1)
    for _ in prime_gen: factorization.append(1)
    prime_gen = primes(k**2) 
    return reduce(lambda x,y: x*prime_gen.next()**y, [1]+factorization)

print "k=10:"
print euler5(10)
print "k=20:"
print euler5(20)
print "k=100:"
print euler5(100)
print "k=1000:"
print euler5(1000)
print "k=2000:"
print euler5(2000)
