#! /usr/bin/python
from euler5 import primes
import itertools as it

p = set(primes(1000000))

def primelength(a, b):
    return len(list(
        it.takewhile(lambda n: n**2+a*n+b in p, it.count(0))
    ))

if __name__ == "__main__":
    a, b, length = max(
        it.starmap(
            lambda x, y: (x,y,primelength(x,y)),
            it.product(
                range(-999,1000,2),
                primes(1000)
            )
        ),
        key=lambda x: x[2]
    )
    print a*b
