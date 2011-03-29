
def square_sum(n):
    return sum(d*d for d in map(int, str(n)))

def iterated_square_sum(n):
    sum_sq = n
    while sum_sq != 1 and sum_sq != 89:
        sum_sq = square_sum(sum_sq)
    return True if sum_sq == 89 else False

def euler92(upper_bound=10000000):
    """http://projecteuler.net/index.php?section=problems&id=92
    
    Investigating a square digits number chain with a surprising property."""
    # note: the maximum square sum for numbers under 10M is 567
    memo = map(iterated_square_sum, xrange(1, 568))
    return len(filter(lambda x: memo[square_sum(x)-1], xrange(1, upper_bound)))

