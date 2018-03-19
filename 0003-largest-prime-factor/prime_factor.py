"""Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

import numpy as np
from functools import reduce
from collections import defaultdict, OrderedDict

def prime_factorization(n):
    """
    Finds the prime factorization of n.
    Returns a dictionary where the keys are the prime factors,
    and the values are the multiplicities of the factors.
    """
    if n == 0:
        return {}

    factors = defaultdict(int)
    dividend = n
    #sqrtn = np.sqrt(n)

    #Factor out as many 2's as possible.
    while dividend%2 == 0:
        dividend //= 2
        factors[2] += 1

    #Factor out each odd number from 3 up to sqrt(n)
    #as many times as possible. Since we're visiting potential
    #divisors in increasing order, any composite number d will
    #have already been factored out by the time we reach it because
    #it is a product of smaller primes, so we know that
    #if d divides n, then d must be prime.
    d = 3
    while dividend > 1 and d*d <= n:
        while dividend%d == 0:
            dividend //= d
            factors[d] += 1
        d += 2

    #Catch the final factor > sqrt(n) if it exists.
    #Note that n can have at most one prime factor greater than sqrt(n).
    #Once we have divided out all primes <= sqrt(n), the resulting factor
    #is either 1 (if n has no divisors > sqrt(n), in which case we're done)
    #or is a prime number greater than sqrt(n) (which may be n itself),
    #in which case we add it to the list of factors, with multiplicity 1.
    if dividend > 1:
        factors[dividend] = 1

    return OrderedDict(sorted(factors.items(), key=lambda t:t[0]))

def prime_sieve(n):
    """
    Returns the sieve of Eratosthenes up to n,
    a list of booleans indicating whether each number from
    0 to n is prime.

    The required space is (clearly) n, and the runtime is (surprisingly!)
    n * loglog(n), by adding up the following:

    -Time n to initialize the array.
    -Time sqrt(n) to visit each of the first sqrt(n) elements of the array.
    -For each prime p <= sqrt(n), we touch n/p elements of the array.

    Thus the runtime is:
    n + sqrt(n) + n/2 + n/3 + n/5 + n/7 + ... + n/p_sqrt(n)
    = sqrt(n) + n * (1 + 1/2 + 1/3 + 1/5 + 1/7 + ... + 1/p_sqrt(n)),
    where the sum is over primes from 2 up to the largest prime <= sqrt(n).
    The series of reciprocal primes diverges as loglog(n), so the runtime is
    sqrt(n) + n * loglog(sqrt(n)) = O(n * loglog(n))
    """
    #indices are 0 to n
    is_prime = [True for _ in range(n+1)]

    #Assumes n >= 1 (otherwise, what's the point?)
    is_prime[0] = False
    is_prime[1] = False

    k = 2
    while k*k <= n:
        if is_prime[k]:
            for m in range(2, n//k + 1):
                is_prime[k*m] = False
        k += 1

    return is_prime

def get_primes(n):
    """
    Returns a list of primes <= n, using the sieve of Eratosthenes.
    """
    is_prime = prime_sieve(n)
    return [p for p in range(n+1) if is_prime[p]]

def prime_factors(n):
    """
    Returns a list of prime factors of n.
    600851475143
    """
    #First find all primes up to sqrt(n)
    sqrtn = int(np.sqrt(n))
    primes = get_primes(sqrtn)
    factors = [p for p in primes if n % p == 0]

    # #If we found none, then n must be prime, hence is its only prime factor
    # if len(factors) == 0:
    #     factors.append(n)
    # else:

    #Otherwise, we are missing at most one prime factor since
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
    factors = prime_factors(600851475143)
    print(factors[-1])
