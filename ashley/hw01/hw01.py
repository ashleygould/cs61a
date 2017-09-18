#!/usr/bin/env python
"""cs61a H1"""


# Q1: 
from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = lambda x, y: sub(x, y)
    else:
        f = lambda x, y: add(x, y)
    return f(a, b)


# Q2: Two of Three
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return sorted([a, b, c])[-1]**2 + sorted([a, b, c])[-2]**2



# Q3: Largest Factor

# Write a function that takes an integer n that is greater than 1 and returns
# the largest integer that is smaller than n and evenly divides n.

# Hint: To check if b evenly divides a, you can use the expression a % b == 0,
# which can be read as, "the remainder of dividing a by b is 0."

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    if not isinstance(n, int) or n <= 1:
        raise ValueError('n must be integer greater than 1')
    factors = [x for x in range(1, n/2 + 1) if n % x == 0]
    return factors[-1]


# Q4:

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return True

def t():
    print '1'
    return

def f():
    print 'f'
    return



# Q5: Hailstone

# Pick a positive integer n as the start.
# If n is even, divide it by 2.
# If n is odd, multiply it by 3 and add 1.
# Continue this process until n is 1.
# 
# This sequence of values of n is often called a Hailstone sequence, Write a
# function that takes a single argument with formal parameter name n, prints out
# the hailstone sequence starting at n, and returns the number of steps in the
# sequence

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    if not isinstance(n, int) or n <= 1:
        raise ValueError('n must be integer greater than 1')

    # Using recursion:
    #def hail(n, counter=1):
    #    print(n)
    #    if n > 1:
    #        if n % 2 == 0:
    #            n = n/2
    #        else:
    #            n = n * 3 + 1
    #        return hail(n, counter + 1)
    #    return counter
    #return hail(n)
 
    # Using while loop:
    counter = 1
    print(n)
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n * 3 + 1
        counter += 1
        print(n)
    return counter


# Doctest
#   python H1.ashley.py
#   python H1.ashley.py -v
def _test():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
   _test()

