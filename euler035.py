
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
    global primes
    primes = set(sieve(upper_bound))
    prime_count = sum(cyclic_prime(x) for x in primes)
    print 'There are %d circular primes under %d' % (prime_count, upper_bound)
    return prime_count

