#! /usr/bin/python

def fib():
    a = 1
    b = 1
    while a<=4000000:
        if a%2==0: yield a
        a, b = b, a+b

print [a for a in fib()]

print "---"

print sum(a for a in fib())

