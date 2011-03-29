
from euler_util import factorial

def euler15(n=20):
    """http://projecteuler.net/index.php?section=problems&id=15
    
    Starting in the top left corner in a 20 by 20 grid, how many routes
    are there to the bottom right corner?"""
    # simple combinatorics, 2n choose n
    return factorial(2*n) / (factorial(n) ** 2)

