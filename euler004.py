
from euler_util import is_palindrome

def euler4(upper_bound=1000):
    """http://projecteuler.net/index.php?section=problems&id=4
    
    Find the largest palindrome made from the product of two 3-digit numbers."""
    max_pal = 0
    for x in xrange(0,1000):
        for y in xrange(x,1000):
            if x * y > max_pal and is_palindrome(x * y):
                max_pal = x * y
    return max_pal

