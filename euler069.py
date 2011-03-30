
from euler_util import sieve, factor

def totient(n):
    factors = factor(n)
    phi, last_f = 1, 1
    for f in factors:
        if f == last_f:
            phi *= f
        else:
            phi, last_f = phi*(f - 1), f
    return phi

primes = sieve(1000)
def euler69(upper_bound=1000000):
    """http://projecteuler.net/index.php?section=problems&id=69

    Find the value of n <= 1,000,000 for which n/totient(n) is a maximum."""
    # Note: here is the brute force approach:
    # return max(zip(map(lambda x: float(x)/totient(x),
    #           xrange(1, ub)), xrange(1, ub)))
    # to do this more cleverly, realize that we minimize phi(n) when n is a
    # product of the first n primes.
    value = 1
    for p in primes:
        value *= p
        if value > upper_bound: return value/p

