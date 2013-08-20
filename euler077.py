
import itertools
from euler_util import sieve, memoized

primes = sieve(10000)

@memoized
def ways_limit(n, limit):
    if n < 0: return 0
    if n == 0: return 1
    return sum(ways_limit(n-p, p) for p in primes if p<=limit)


def ways(n): return ways_limit(n, n)


def euler77(target=5000):
    """http://projecteuler.net/problem=77

    It is possible to write ten as the sum of primes in exactly five different
    ways:

    7 + 3
    5 + 5
    5 + 3 + 2
    3 + 3 + 2 + 2
    2 + 2 + 2 + 2 + 2

    What is the first value which can be written as the sum of primes in over
    five thousand different ways?
    """
    for i in itertools.count(1):
        if ways(i) > 5000: return i
