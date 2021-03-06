"""Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

import numpy as np
from functools import reduce
from collections import Counter, OrderedDict

#Implementation of OrderedCounter from Python Docs:
#https://docs.python.org/3/library/collections.html#collections.OrderedDict
#This will be used to store the prime factors of an integer in increasing order,
#with the value associated with each prime key being the prime's multiplicity
#in the factorization.
class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    #This returns the string representation
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    #This is for pickling
    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

def prime_factorization(n):
    """
    Finds the prime factorization of the integer n.
    Returns a dictionary where the keys are the prime factors,
    and the values are the multiplicities of the factors.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")

    factors = OrderedCounter()
    dividend = n
    #sqrtn = np.sqrt(n)

    #Factor out as many 2's as possible, counting them as we go.
    while dividend%2 == 0:
        dividend //= 2
        factors[2] += 1

    #Factor out each odd number from 3 up to sqrt(n) as many times
    #as possible, counting them as we go. Stop if the quotient reaches 1.
    #
    #Since we're visiting potential divisors in increasing order,
    #any composite number will have already been factored out
    #by the time we reach it because it is a product of smaller
    #primes, so we know that if we find a number d that divides n,
    #then d must be prime.
    d = 3 #d is a potential divisor
    while dividend > 1 and d*d <= n:
        while dividend%d == 0:
            dividend //= d
            factors[d] += 1
        d += 2

    #Catch the final factor > sqrt(n) if it exists.
    #Note that n can have at most one prime factor greater than sqrt(n).
    #Once we have divided out all primes <= sqrt(n), the resulting quotient
    #is either 1 (if n has no divisors > sqrt(n), in which case we're done)
    #or is a prime number greater than sqrt(n) (which may be n itself),
    #in which case we add it to the list of factors, with multiplicity 1.
    if dividend > 1:
        factors[dividend] = 1

    #Return the factors as an ordered dictionary
    return factors

def sieve_of_eratosthenes(n):
    """
    Returns an array of booleans indicating whether each integer from
    0 to n (inclusive) is prime, using the sieve of Eratosthenes algorithm. 

    The required space is (obviously) O(n), and the runtime is (surprisingly!)
    O(n * loglog(n)), by adding up the following:

    -Time n to initialize the array.
    -Time sqrt(n) to visit each of the first sqrt(n) elements of the array.
    -For each prime p <= sqrt(n), we touch n/p elements of the array.

    Thus the runtime is:
    n + sqrt(n) + n/2 + n/3 + n/5 + n/7 + ... + n/p_sqrt(n)
    = sqrt(n) + n * (1 + 1/2 + 1/3 + 1/5 + 1/7 + ... + 1/p_sqrt(n)),
    where the sum is over primes from 2 up to the largest prime <= sqrt(n).
    The series of reciprocal primes diverges as loglog(n), so the runtime is
    sqrt(n) + n * loglog(sqrt(n)) = O(n * loglog(n)).
    """
    #indices are 0 to n
    is_prime = [True for _ in range(n+1)]

    #Assumes n >= 1 (otherwise, what's the point?)
    is_prime[0] = False
    is_prime[1] = False

    #Note: I could optimize this like the above function to strike out
    #multiples of 2 first, then increment by 2 to iterate over odd numbers.
    k = 2
    while k*k <= n:
        if is_prime[k]:
            for m in range(2, n//k + 1):
                is_prime[k*m] = False
        k += 1

    return is_prime

def primes_up_to(n):
    """
    Returns a list of primes <= n, using the sieve of Eratosthenes.
    """
    is_prime = sieve_of_eratosthenes(n)
    return [p for p in range(n+1) if is_prime[p]]

def prime_factors(n):
    """
    Returns a list of prime factors of n, without taking
    multiplicity into account.
    """
    #First find all primes up to sqrt(n)
    sqrtn = int(np.sqrt(n))
    primes = primes_up_to(sqrtn)
    factors = [p for p in primes if n % p == 0]

    #Now, we are missing at most one prime factor since
    #n can have at most one prime factor > sqrt(n).
    #We will repeatedly divide by primes in our list of prime
    #factors if possible -- if the result ever gets below sqrt(n),
    #then there is no missing prime factor; if the result remains
    #above sqrt(n) and we can't divide any more, then we have found
    #a missing prime factor, so we add it to the list.
    factor = n
    remaining = factors

    while factor > sqrtn and len(remaining) > 0:
        product = reduce(lambda a,b: a*b, remaining)
        factor = factor // product
        remaining = [p for p in factors if factor % p == 0]
        print(product, factor, remaining)

    if factor > sqrtn:
        factors.append(factor)

    return factors

if __name__=="__main__":
    factors = prime_factorization(600851475143)
    print(factors)
    print(list(factors.keys())[-1])

    factors = prime_factors(600851475143)
    print(factors)
    print(factors[-1])
