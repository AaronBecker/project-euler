
import decimal

def euler80(limit=100):
    """http://projecteuler.net/index.php?section=problems&id=80

    It is well known that if the square root of a natural number is not an
    integer, then it is irrational. The decimal expansion of such square roots
    is infinite without any repeating pattern at all.

    The square root of two is 1.41421356237309504880..., and the digital sum of
    the first one hundred decimal digits is 475.

    For the first one hundred natural numbers, find the total of the digital
    sums of the first one hundred decimal digits for all the irrational square
    roots.
    """
    decimal.getcontext().prec = 110 # give a little leeway on precision
    def sqrt_sum(x):
        if x**0.5 == int(x**0.5): return 0
        val = lambda c: ord(c)-ord('0')
        s = str(decimal.Decimal(x).sqrt())
        return sum(val(c) for c in s[:101])-val('.')
    return sum(sqrt_sum(x) for x in xrange(limit+1))
    


