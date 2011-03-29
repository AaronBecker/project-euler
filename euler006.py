
def euler6(upper_bound=100):
    """http://projecteuler.net/index.php?section=problems&id=6
    
    What is the difference between the sum of the squares and the square of
    the sums?"""
    sum_sq = sum([x * x for x in range(1, upper_bound+1)])
    sq_sum = sum(range(1, upper_bound+1)) ** 2
    return sq_sum - sum_sq

