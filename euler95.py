from euler_util import divisors

def euler95(upper_bound=10**6):
    """Find the smallest member of the longest amicable
    chain with no element exceeding one million."""
    divisor_sums = [sum(divisors(x)) for x in range(upper_bound)]
    for x in range(upper_bound):
        pass
