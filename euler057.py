
import itertools
from fractions import Fraction

def sqrt_two_expansion():
    partial_sum = Fraction(3, 2)
    while True:
        yield partial_sum
        partial_sum = 1 + 1/(partial_sum+1)

def euler57():
    """http://projecteuler.net/index.php?section=problems&id=57
    
    Investigate the expansion of the continued fraction for the square root of
    two."""
    generator = sqrt_two_expansion()
    return len(filter(lambda x: len(str(x.numerator)) > len(str(x.denominator)),
        itertools.islice(generator, 1000)))

