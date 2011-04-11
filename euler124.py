
from euler_util import product, factor

def rad(n):
    return product(set(factor(n)))

def euler124(upper_bound=100000+1):
    """http://projecteuler.net/index.php?section=problems&id=124

    Determining the kth element of the sorted radical function."""
    return sorted(xrange(1, upper_bound), key=rad)[10000-1]

