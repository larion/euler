#! /usr/bin/python

import random
import time

from math import log, exp

NUMBER = "".join((
"73167176531330624919225119674426574742355349194934",
"96983520312774506326239578318016984801869478851843",
"85861560789112949495459501737958331952853208805511",
"12540698747158523863050715693290963295227443043557",
"66896648950445244523161731856403098711121722383113",
"62229893423380308135336276614282806444486645238749",
"30358907296290491560440772390713810515859307960866",
"70172427121883998797908792274921901699720888093776",
"65727333001053367881220235421809751254540594752243",
"52584907711670556013604839586446706324415722155397",
"53697817977846174064955149290862569321978468622482",
"83972241375657056057490261407972968652414535100474",
"82166370484403199890008895243450658541227588666881",
"16427171479924442928230863465674813919123162824586",
"17866458359124566529476545682848912883142607690042",
"24219022671055626321111109370544217506941658960408",
"07198403850962455444362981230987879927244284909188",
"84580156166097919133875499200524063689912560717606",
"05886116467109405077541002256983155200055935729725",
"71636269561882670428252483600823257530420752963450"))

def largest_product(number_str, prod_len):
    """ Take a (usually big) numeral number_str as a string and a number
    prod_len (the window width) and find the largest product made up of
    consecutive prod_len digits of number_str and return both the value of the
    product and the index of the first digit. This algorithm does that in O(n)
    time, where n is the length of the numeral. The naive algorithm takes O(nm)
    time where n is the length of the string and m the length of the window.
    >>> largest_product("119991111", 3) #9*9*9=729
    (729, 2)
    >>> largest_product("123456789", 2) #8*9=72
    (72, 7)
    >>> largest_product("4365610", 4)  #3*6*5*6=540
    (540, 1)
    >>> largest_product("43656100000000009988000", 4)  #9*9*8*8=5184
    (5184, 16)
    """ 
    digit_list = map(int, number_str)
    length = len(digit_list)
    assert prod_len < length
    first_window = digit_list[:prod_len]
    first_window_pos = filter(lambda x: x is not 0, first_window) # leave out the zeroes
    # This calculates the product of the first prod_len wide window 
    # (without the zeroes):
    val = reduce(lambda x,y: x*y, first_window_pos) 
    zero_count = first_window.count(0)
    # the index of the first and the last element in the window
    ind_left, ind_right = 0, prod_len-1 
    max_val = val 
    max_ind_left = ind_left
    while ind_right < length-1:
      # move window
      ind_right+=1 
      ind_left+=1
      right = digit_list[ind_right]
      left = digit_list[ind_left-1] # no longer in the window
      # update the count of zeroes inside the window
      if right == 0: 
          # Pretend it's a 1. This way we don't have to recalculate the product
          # and get linear performance.
          right = 1
          zero_count += 1
      if left == 0: 
          left = 1
          zero_count -= 1
      val = (val*right)/left
      if zero_count == 0 and max_val < val:
          max_val = val
          max_ind_left = ind_left
    return (max_val, max_ind_left)

def largest_product_naive(number_str, prod_len):
    """ Take a (usually big) numeral number_str as a string and a number
    prod_len (the window width) and find the largest product made up of
    consecutive prod_len digits of number_str and return both the value of the
    product and the index of the first digit.
    >>> largest_product_naive("119991111", 3) #9*9*9=729
    (729, 2)
    >>> largest_product_naive("123456789", 2) #8*9=72
    (72, 7)
    >>> largest_product_naive("4365610", 4)  #3*6*5*6=540
    (540, 1)
    >>> largest_product_naive("43656100000000009988000", 4)  #9*9*8*8=5184
    (5184, 16)
    """
    number = map(lambda x: int(x), number_str)
    products = ( (reduce(lambda x,y: x*y, number[i:i+prod_len]), i) 
            for i in range(len(number)-prod_len+1))
    return max(products, key=lambda x: x[0])

def euler8():
    """Solve the 8th puzzle on Project Euler."""
    return largest_product(NUMBER, 13)[0] # return the product

def benchmark():
    huge_number = [str(random.randrange(10)) for _ in range(10**6)]
    # let's make sure that we have a non-zero product:
    huge_number.extend([str(random.randrange(1,10)) for _ in range(200)]) 
    before = time.time()
    result = largest_product(huge_number, 200)
    after = time.time()
    print "Calculation took %f seconds (linear-time algorithm). Result: %d, %d"%(after-before, result[0], result[1])
    before = time.time()
    result = largest_product_naive(huge_number, 200)
    after = time.time()
    print "Calculation took %f seconds (naive algorithm). Result: %d, %d"%(after-before, result[0], result[1])

if __name__=="__main__":
    import doctest
    doctest.testmod()
    print euler8()
    benchmark()
