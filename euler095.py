
def chain_length(n):
    curr = n
    members = []
    while divisor_sums[curr] < 10**6 and not curr in members:
        members.append(curr)
        curr = divisor_sums[curr]
    if curr == n: return len(members)
    return 0

def euler95(upper_bound=10**6):
    """http://projecteuler.net/problem=95

    The proper divisors of a number are all the divisors excluding the number
    itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As
    the sum of these divisors is equal to 28, we call it a perfect number.

    Interestingly the sum of the proper divisors of 220 is 284 and the sum of
    the proper divisors of 284 is 220, forming a chain of two numbers. For this
    reason, 220 and 284 are called an amicable pair.

    Perhaps less well known are longer chains. For example, starting with 12496,
    we form a chain of five numbers:

    12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

    Since this chain returns to its starting point, it is called an amicable
    chain.

    Find the smallest member of the longest amicable chain with no element
    exceeding one million.
    """
    global divisor_sums
    divisor_sums = [0]*upper_bound
    for i in xrange(1, upper_bound):
        for j in xrange(2*i, upper_bound, i):
            divisor_sums[j] += i
    chain_lengths = [chain_length(x) for x in xrange(upper_bound)]
    return chain_lengths.index(max(chain_lengths))
