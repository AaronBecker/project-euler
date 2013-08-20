
odd_digits = set("13579")
def is_reversible(n):
    if n % 10 == 0: return False
    digit_sum = n + int(''.join(reversed(str(n))))
    return set(str(digit_sum)) <= odd_digits

def euler145(ub=10**9):
    """http://projecteuler.net/problem=145

    How many reversible numbers are there below one-billion?"""
    # FIXME: Brute force, very slow. A combinatoric approach
    # would be much faster.
    ub /= 10  # note that no length 9 solutions exist
              # (nor do length 5, but it's not worth skipping them)
    return sum(is_reversible(n) for n in xrange(ub))

