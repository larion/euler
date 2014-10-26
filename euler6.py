#! /usr/bin/python


def square_of_sum(n):
    """ return the square of the sum of the first n 
    natural numbers (i.e. (1+2+...+n)^2) """
    return (n*(n+1)/2)**2

def sum_of_squares(n):
    """ return the sum of squares for the first n natural
    numbers (i.e. 1^2 + 2^2 + ... + n^2) """
    if n==1: 
        return 1
    return n**3-2*sum_of_squares(n-1)-n*(n-1)/2

def euler6(n):
    """ returns the differrence between the sum of the squares
    and the square of the sum of the first n natural numbers """
    return square_of_sum(n)-sum_of_squares(n)

if __name__ == "__main__":
    print euler6(10)
    print euler6(100)
