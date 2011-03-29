
pentagonals = set([])
def nth_pentagonal(n):
    return n*(3*n - 1)/2

def pentagonal_pair(x, y):
    return x - y in pentagonals and x + y in pentagonals

def euler44(upper_bound=5000):
    """http://projecteuler.net/index.php?section=problems&id=44

    Find the smallest pair of pentagonal numbers whose sum and difference is
    pentagonal"""
    global pentagonals
    pentagonals = set(nth_pentagonal(n) for n in xrange(1, upper_bound))
    return min(x - y for x in pentagonals for y in pentagonals if
            x > y and pentagonal_pair(x, y))

