
def euler6(upper_bound=100):
    """What is the difference between the sum of the squares 
    and the square of the sums?"""
    sum_sq = sum([x * x for x in range(1, upper_bound+1)])
    sq_sum = sum(range(1, upper_bound+1)) ** 2
    result = sq_sum - sum_sq
    print "The difference between the sum of squares and the squared sum from 1 to %d"\
            " is %d" % (upper_bound, result)
    return result

