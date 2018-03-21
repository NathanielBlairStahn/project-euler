"""Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

from functools import reduce

def gcd(a,b):
    """
    Returns the greatest common divisor of a and b,
    using the Euclidean algorithm.
    """
    #If b is 0, the gcd is a
    while b !=0:
        #Code from Wikipedia:
        # temp = b
        # b = a % b
        # a = temp
        
        #Better code:
        r = a % b #If a = qb+r, compute the remainder r
        a = b #Replace a with b
        b = r #Replace b with r
        #Note that if a<b, this code just swaps a and b

    return a

def lcm(a,b):
    """
    Returns the least common multiple of a and b,
    using the gcd function.
    """
    return a*b // gcd(a,b)

def smallest_multiple(numbers):
    """
    Returns the least common multiple of a list (or iterable) of numbers,
    by repeatedly calling lcm.
    """
    return reduce(lcm, numbers)

if __name__ == "__main__":
    print(smallest_multiple(range(1,21)))
