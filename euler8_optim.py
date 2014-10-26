#! /usr/bin/python

#
# :) obviously an overkill, see euler8.py for a normal solution
#

def largest_product_optim(number_str, prod_len): #ugly but a little faster version
    """ This function takes a (usually big) numeral as a string 
    and a number prod_len (the window width). It finds the largest product 
    made up of consecutive n digits of the big number and returns the
    value of the product and the index of the first digit. This algorithm
    does that in O(n) time, where n is the length of the numeral. The naive
    algorithm takes O(nm) time where n is the length of the string and m the
    length of the window.
    >>> largest_product_optim("119991111", 3) #9*9*9=729
    (729, 2)
    >>> largest_product_optim("123456789", 2) #8*9=72
    (72, 7)
    >>> largest_product_optim("4365610", 4)  #3*6*5*6=540
    (540, 1)
    >>> largest_product_optim("43656100000000009988000", 4)  #9*9*8*8=5184
    (5184, 16)
    """ 
    # We will represent digit values and products as their prime factorization.
    # This way we can store very large numbers without losing precision. Also
    # we can use (vector) addition instead of (scalar) multiplication to calculate
    # products which is cheaper (at least for large n). For this we will need a
    # mapping from the first 9 digits to their prime factorization.
    primefactors = {
            0: None, 
            1: vector([0,0,0,0]),
            2: vector([1,0,0,0]),
            3: vector([0,1,0,0]),
            4: vector([2,0,0,0]),
            5: vector([0,0,1,0]),
            6: vector([1,1,0,0]),
            7: vector([0,0,0,1]),
            8: vector([3,0,0,0]),
            9: vector([0,2,0,0]),
            }
    # We will also need  a function to calculate numbers from their
    # factorization. Note that because all products are made up of the digits
    # 1,2,...,9 there can be no higher prime factor present.
    def factorproduct(factors):
        if factors is None:
            return 0
        if any(factors[n] != 0 for n in range(4)):
            return 2**int(factors[0]) * 3**int(factors[1]) * 5**int(factors[2]) * 7**int(factors[3])
        else:
            return 1

    fact_list = map(lambda x: primefactors[x], map(int, number_str))
    length = len(fact_list)
    assert prod_len < length
    # This calculates the product of the first prod_len wide window (pretend that
    # 0s are 1s):
    first_window = filter(lambda x: x is not None, fact_list[:prod_len]) # leave out the zeroes
    val = map(sum, zip(*first_window))
    zero_count = len([elem for elem in fact_list[:prod_len] if elem is None]) # number of zeroes in the first window
    # the index of the first and the last element in the window
    ind_left, ind_right = 0, prod_len-1 
    # A value of None will represent 0; note that factorproduct([0,0,0,0])==1
    best_val = factorproduct(val) if zero_count==0 else None
    best_ind_left = ind_left

    while ind_right < length-1: # main loop
      # move right edge and fetch the digits at the boundary
      ind_right+=1 
      right = fact_list[ind_right]
      left = fact_list[ind_left]
      # update the count of zeroes inside the window
      # and convert the numbers to their prime
      # factorization
      if right is None: # new zero in window
          # Pretend it's a 1. This way we don't have to recalculate the product
          # and get linear performance.
          right = primefactors[1] 
          zero_count += 1
      if left is None: # one less zero in the new window
          left = primefactors[1]
          zero_count -= 1
      ind_left+=1 # move left edge
      # update val:
      # i.e. val*=(right/left) if they were represented as integers
      val = val+right-left 
      if zero_count == 0 and best_val < factorproduct(val):
          best_val = factorproduct(val)
          best_ind_left = ind_left
    if best_val is None: 
        best = 0
    else: #found at least one non-zero product
        best = best_val
    return (best, best_ind_left)
