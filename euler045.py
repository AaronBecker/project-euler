
def euler45(upper_bound=100000):
    """http://projecteuler.net/index.php?section=problems&id=45
    
    After 40755, what is the next triangle number that is also pentagonal and
    hexagonal?"""
    triangles = set([n * (n + 1) / 2 for n in xrange(upper_bound)])
    pentangles = set([n * (3*n - 1) / 2 for n in xrange(upper_bound)])
    hexangles = set([n * (2*n - 1) for n in xrange(upper_bound)])
    return min(x for x in triangles & pentangles & hexangles if x > 40755)
