# coding=utf8
from euler_util import sieve

primes = sieve(1000)
def euler69(upper_bound=1000000):
    """http://projecteuler.net/index.php?section=problems&id=69

    Find the value of n <= 1,000,000 for which n/φ(n) is a maximum."""
    # Note: here is the brute force approach:
    # return max(zip(map(lambda x: float(x)/totient(x),
    #           xrange(1, ub)), xrange(1, ub)))
    # to do this more cleverly, realize that we minimize phi(n) when n is a
    # product of the first n primes.
    value = 1
    for p in primes:
        value *= p
        if value > upper_bound: return value/p

