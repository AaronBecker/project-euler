
from bisect import bisect
from euler_util import sieve

def euler187(ub=10**8):
    """http://projecteuler.net/problem=187

    A composite is a number containing at least two prime factors. For example,
    15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

    There are ten composites below thirty containing precisely two, not
    necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

    How many composite integers, n < 108, have precisely two, not necessarily
    distinct, prime factors?
    """
    small_primes = sieve(int(ub ** 0.5))
    big_primes = sieve(ub/2)
    total = 0
    for x in range(len(small_primes)):
        total += bisect(big_primes, ub/small_primes[x]) - x
    return total
