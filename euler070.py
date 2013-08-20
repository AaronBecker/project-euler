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
    """http://projecteuler.net/problem=70

    Euler's Totient function, φ(n) [sometimes called the phi function], is used
    to determine the number of positive numbers less than or equal to n which
    are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all
    less than nine and relatively prime to nine, φ(9)=6.  The number 1 is
    considered to be relatively prime to every positive number, so φ(1)=1.

    Interestingly, φ(87109)=79180, and it can be seen that 87109 is a
    permutation of 79180.

    Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n
    and the ratio n/φ(n) produces a minimum.
    """
    #TODO: this is still very slow. Optimize, using the knowledge that
    # the answer should be the product of two large primes.
    return min(totient_permutation(n) for n in xrange(2, ub))[1]
