
from euler_util import divisors

divisor_sums = []
def chain_length(n):
    curr = n
    members = []
    while divisor_sums[curr] < 10**6 and not curr in members:
        members.append(curr)
        curr = divisor_sums[curr]
    if curr == n: return len(members)
    return 0

def euler95(upper_bound=10**6):
    """http://projecteuler.net/index.php?section=problems&id=95
    
    Find the smallest member of the longest amicable chain with no element
    exceeding one million."""
    global divisor_sums
    divisor_sums = [0]*upper_bound
    for i in xrange(1, upper_bound):
        for j in xrange(2*i, upper_bound, i):
            divisor_sums[j] += i
    chain_lengths = [chain_length(x) for x in xrange(upper_bound)]
    return chain_lengths.index(max(chain_lengths))
