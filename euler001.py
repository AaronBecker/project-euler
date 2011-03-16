
def euler1(upper_bound=1000):
    """Add all the natural numbers below 1000 that are multiples of 3 or 5"""
    fives = set(range(0, upper_bound, 5))
    threes = set(range(0, upper_bound, 3))
    union_sum = sum(fives | threes)
    print "The sum of the multiples of 3 and 5 under %d is %d\n" %\
        (upper_bound, union_sum)
    return union_sum

