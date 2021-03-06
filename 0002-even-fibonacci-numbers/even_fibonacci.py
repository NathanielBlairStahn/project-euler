"""Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

def fib_recursive(n):
    """
    Returns the nth Fibonacci number using the naive recursive solution.
    This takes exponential time and space (BAD!).
    """
    if n<=1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_memoized(n, memo={}):
    """
    Returns the nth Fibonacci number using a memoized recursive solution.
    The memo is a dictionary (hashtable).
    This takes linear time and space.
    """
    if n <=1:
        return n

    if n not in memo:
        memo[n] = fib_memoized(n-1, memo) + fib_memoized(n-2, memo)

    return memo[n]

def fibonacci(n):
    """
    Returns the nth Fibonacci number using a for loop.
    This takes linear time and constant space.
    """
    if n==0:
        return 0

    f_previous = 0
    f_current = 1
    for i in range(1, n):
        f_next = f_current + f_previous
        f_previous = f_current
        f_current = f_next

    return f_current

def fibonacci_generator(upper_bound):
    """
    Generates all Fibonacci numbers less than upper_bound.
    """
    yield 0

    f_previous = 0
    f_current = 1
    while(f_current < upper_bound):
        yield f_current
        f_next = f_current + f_previous
        f_previous = f_current
        f_current = f_next

def even_fibonacci(n, upper_bound=float('inf')):
    """
    Generates all even Fibonacci numbers up to (and including) the n^th one.
    Indexing starts at 0, so n+1 numbers will be generated.
    """
    if n>=0:
        yield 0

    f_previous = 0
    f_current = 1
    #Every 3^rd Fibonacci number is even, so we need 3n Fibonacci numbers
    #to get n even ones:
    #0 1 2 3 4 5 6 7  8  9  10 11 12  13  14  15  16  17
    #0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1579
    #0     1     2       3        4           5
    # counter = 1
    # while(counter <= 3*n and f_current <= upper_bound)
    for i in range(3*n):
        if f_current % 2 == 0:
            yield f_current
        f_next = f_current + f_previous
        f_previous = f_current
        f_current = f_next

if __name__=="__main__":
    pass
