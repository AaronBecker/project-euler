
from itertools import count, dropwhile

def same_digits(x):
    return set(str(2*x)) == set(str(6*x)) == set(str(5*x)) == \
            set(str(4*x)) == set(str(3*x))

def euler52():
    """http://projecteuler.net/index.php?section=problems&id=52
    
    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
    contain the same digits in some order."""
    n = dropwhile(lambda x: not same_digits(x), count(1)).next()
    return n

