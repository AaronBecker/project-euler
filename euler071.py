
from fractions import Fraction
from math import floor, ceil

def euler71(limit=1000000):
    """http://projecteuler.net/index.php?section=problems&id=71

    Consider the fraction, n/d, where n and d are positive integers. If nd and
    HCF(n,d)=1, it is called a reduced proper fraction.

    If we list the set of reduced proper fractions for d  8 in ascending order
    of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
    5/7, 3/4, 4/5, 5/6, 6/7, 7/8

    It can be seen that 2/5 is the fraction immediately to the left of 3/7.

    By listing the set of reduced proper fractions for d <= 1,000,000 in
    ascending order of size, find the numerator of the fraction immediately to
    the left of 3/7.
    """
    fracs = set()
    for denom in xrange(2, limit + 1):
        num_guess = denom * 3.0 / 7.0
        fracs.add(Fraction(int(floor(num_guess)), denom))
        fracs.add(Fraction(int(ceil(num_guess)), denom))
    fracs = sorted(fracs)
    return fracs[fracs.index(Fraction(3, 7)) - 1]
    
