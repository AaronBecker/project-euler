
def euler9(target=1000):
    """http://projecteuler.net/index.php?section=problems&id=9
    
    Find the product of the Pythagorean triplet where a + b + c = 1000."""
    for x in xrange(1, target):
        for y in xrange(1, target):
            if x ** 2 + y ** 2 - (target - x - y) ** 2 == 0:
                return x * y * (target - x - y)

