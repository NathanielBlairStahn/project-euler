"""Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

def mults_3_and_5(n):
    """
    Returns a generator of the multiples of 3 and 5 that are less than n.
    """
    return (x for x in range(n) if x%3 == 0 or x%5 == 0)

if __name__=="__main__":
    print(sum(mults_3_and_5(1000)))
