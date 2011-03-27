
from itertools import count, dropwhile

def same_digits(x):
    return set(str(2*x)) == set(str(6*x)) == set(str(5*x)) == \
            set(str(4*x)) == set(str(3*x))

def euler52():
    """Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
    contain the same digits in some order."""
    n = dropwhile(lambda x: not same_digits(x), count(1)).next()
    print 'The smallest integer x, such that 2x, 3x, ..., 6x all have',
    print 'the same digits is %d' % n
    return n

