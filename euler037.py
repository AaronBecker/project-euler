
from euler_util import sieve

primes = set([])
def is_truncatable(n):
    if n < 10: return False
    sn = str(n)
    for i in range(1,len(sn)):
        if int(sn[i:]) not in primes or int(sn[:i]) not in primes: return False
    return True;

def euler37(upper_bound=1000000):
    """http://projecteuler.net/index.php?section=problems&id=37
    
    Find the sum of all eleven primes that are both truncatable from left to
    right and right to left."""
    global primes
    primes = set(sieve(upper_bound))
    return sum(n for n in primes if is_truncatable(n))

