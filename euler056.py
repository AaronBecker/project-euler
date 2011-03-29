
def digital_sum(x):
    return sum(int(d) for d in str(x))

def euler56():
    """http://projecteuler.net/index.php?section=problems&id=56
    
    Considering natural numbers of the form a^b, find the maximum digital sum.
    """
    return max(digital_sum(a**b) for a in xrange(100) for b in xrange(100))

