
from fractions import Fraction

def nth_e_expansion_digit(n):
    if n == 1: return 2
    if n % 3 == 0: return 2*(n/3)
    return 1

def nth_e_convergent(n):
    n, partial_sum = n-1, Fraction(nth_e_expansion_digit(n), 1)
    while n > 0:
        n, partial_sum = n-1, nth_e_expansion_digit(n) + 1/partial_sum
    return partial_sum

def euler65(term=100):
    """http://projecteuler.net/index.php?section=problems&id=65
    
    e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

    The first ten terms in the sequence of convergents for e are:
    2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
    The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

    Find the sum of digits in the numerator of the 100th convergent of the
    continued fraction for e.
    """
    return sum(int(d) for d in str(nth_e_convergent(term).numerator))

