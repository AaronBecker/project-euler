
from euler_util import sieve

def euler10(target=2000000):
    """http://projecteuler.net/problem=10

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    """
    return sum(sieve(target))

