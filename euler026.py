
import itertools

def cycle_length(x):
    """How long a recurring cycle does 1/x have?"""
    memo = {}
    remainder = 10
    for i in itertools.count():
        if remainder == 0:
            return 0
        elif remainder in memo:
            return i - memo[remainder]
        memo[remainder] = i
        remainder = 10*(remainder % x)

def euler26(upper_bound=1000):
    """Find the value of d < 1000 for which
    1/d contains the longest recurring cycle."""
    length, i = max([(cycle_length(i), i) for i in range(2, upper_bound)])
    print "1/%d has a cycle with length %d" % (i, length)
    return i

