
import itertools

def n_digit_powers(n):
    count = 0
    for exp in itertools.count(1):
        if len(str(n ** exp)) == exp: count += 1
        elif len(str(n ** exp)) < exp: return count

def euler63():
    """http://projecteuler.net/index.php?section=problems&id=63

    How many n-digit positive integers exist which are also an nth power?"""
    return sum(map(n_digit_powers, range(1, 10)))
