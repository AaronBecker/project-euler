
def euler9(target=1000):
    """http://projecteuler.net/problem=9
    
    A Pythagorean triplet is a set of three natural numbers, a<b<c, for
    which a^2 + b^2 = c^2.

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    for x in xrange(1, target):
        for y in xrange(1, target):
            if x**2 + y**2 - (target-x-y)**2 == 0:
                return x*y*(target-x-y)

