#! /usr/bin/python

def fibeven():
    a = 2
    b = 8
    while a<=4000000:
        yield a
        a, b = b, 4*b+a

print [a for a in fibeven()]

print "---"

print sum(a for a in fibeven())

