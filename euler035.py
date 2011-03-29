
from euler_util import sieve
from math import log10
import re

def cycles(x):
    yield x
    e = 10 ** int(log10(x))
    for i in range(int(log10(x))):
        ones = x % 10
        x = x/10 + ones*e
        yield x

primes = set([])
template = re.compile("[1379]+")
def cyclic_prime(x):
    if x > 9 and not template.match(str(x)):
        return False
    return all(y in primes for y in cycles(x))

def euler35(upper_bound=1000000):
    """http://projecteuler.net/index.php?section=problems&id=35

    Find the sum of all numbers less than one million, which are palindromic in
    base 10 and base 2."""
    global primes
    primes = set(sieve(upper_bound))
    return sum(cyclic_prime(x) for x in primes)

