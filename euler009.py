
def euler9(target=1000):
    """Find the product of the Pythagorean triplet where a + b + c = 1000."""
    for x in xrange(1, target):
        for y in xrange(1, target):
            if x**2 + y**2 - (target - x - y)**2 == 0:
                z = target - x - y
                print "%d^2 + %d^2 = %d^2" % (x, y, z)
                print "%d + %d + %d = %d" % (x, y, z, target)
                print "abc = %d" % (x * y * z)
                return x * y * z
    print "Triple not found.\n"
    return 0

