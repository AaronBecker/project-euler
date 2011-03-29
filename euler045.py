
def euler45(upper_bound=100000):
    """After 40755, what is the next triangle number 
    that is also pentagonal and hexagonal?"""
    triangles = set([n * (n + 1) / 2 for n in xrange(2, upper_bound)])
    pentangles = set([n * (3*n - 1) / 2 for n in xrange(2, upper_bound)])
    hexangles = set([n * (2*n - 1) for n in xrange(2, upper_bound)])
    least = min(x for x in triangles & pentangles & hexangles if x > 40755)
    print 'The next number after 40755 that is '\
            'triangular, pentagonal, and hexagonal is %d' % least
    return least
