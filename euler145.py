
odd_digits = set("13579")
def is_reversible(n):
    if n % 10 == 0: return False
    digit_sum = n + int(''.join(reversed(str(n))))
    return set(str(digit_sum)) <= odd_digits

def euler145(ub=10**9):
    """http://projecteuler.net/index.php?section=problems&id=145

    How many reversible numbers are there below one-billion?"""
    # Brute force, very slow
    return sum(is_reversible(n) for n in xrange(ub))

