# encoding: utf8
from euler_util import totient

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
def totient_permutation(n):
    # Since we're looking for a number with a totient as small as possible,
    # we can disregard numbers with small prime factors for speed, as they
    # will have the largest totients.
    for p in small_primes:
        if n % p == 0: return (2, n)
    t = totient(n)
    if sorted(str(n)) == sorted(str(t)):
        return (float(n)/t, n)
    return (2, n)

def euler70(ub=10**7):
    """http://projecteuler.net/index.php?section=problems&id=70

    Investigate values of n for which φ(n) is a permutation of n."""
    #TODO: this is still very slow. Optimize, using the knowledge that
    # the answer should be the product of two large primes.
    return min(totient_permutation(n) for n in xrange(2, ub))[1]
