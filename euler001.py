
def euler1(upper_bound=1000):
    """http://projecteuler.net/index.php?section=problems&id=1
    
    Add all the natural numbers below 1000 that are multiples of 3 or 5"""
    fives = set(range(0, upper_bound, 5))
    threes = set(range(0, upper_bound, 3))
    return sum(fives | threes)

