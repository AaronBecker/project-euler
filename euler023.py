from euler_util import divisors

def euler23():
    """http://projecteuler.net/index.php?section=problems&id=23
    
    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers."""
    abundants = set([x for x in range(1, 28123) if sum(set(divisors(x))) > x])
    summables = set()
    for x in xrange(24, 28124):
        for a in abundants:
            if a > x/2:
                break
            if x-a in abundants:
                summables.add(x)
                break
    return sum(set(range(1, 28124)) - summables)

