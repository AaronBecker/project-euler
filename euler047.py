
import itertools
from euler_util import factor, memoized

@memoized
def distinct_factors(n):
    return len(set(factor(n))) - 1

def euler47():
    """http://projecteuler.net/index.php?section=problems&id=47

    Find the first four consecutive integers to have four distinct prime
    factors."""
    for i in itertools.count():
        if map(distinct_factors, [i+1, i+2, i+3, i+4]) == [4, 4, 4, 4]:
            return i+1

