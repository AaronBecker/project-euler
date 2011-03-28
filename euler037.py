
from euler_util import sieve

primes = set([])
def is_truncatable(n):
    if n < 10: return False
    sn = str(n)
    for i in range(1,len(sn)):
        if int(sn[i:]) not in primes or int(sn[:i]) not in primes: return False
    return True;

def euler37(upper_bound=1000000):
    """Find the sum of all eleven primes that are both truncatable from left to
    right and right to left."""
    global primes
    primes = set(sieve(upper_bound))
    trunc_primes = [n for n in primes if is_truncatable(n)]
    print 'The sum of truncatable primes is %d' % sum(trunc_primes)
    return sum(trunc_primes)

