
def goes_to_89(n):
    sum_sq = n
    while sum_sq != 1 and sum_sq != 89:
        sum_sq = sum(int(d)*int(d) for d in str(sum_sq))
    return True if sum_sq == 89 else False

def euler92(upper_bound=10000000):
    """http://projecteuler.net/index.php?section=problems&id=92
    
    Investigating a square digits number chain with a surprising property."""
    return len(filter(goes_to_89, xrange(1, upper_bound)))

