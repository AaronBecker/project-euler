
from euler_util import sieve
from itertools import combinations

primes = set(p for p in sieve(10**6) if p > 10 ** 5)
templates = list(combinations(range(6), 3))

def fill_template(base, template, number):
    base = list(base)
    for index in template:
        base[index] = number
    return int(''.join(base))

def test_templates(base, target=8):
    for template in templates:
        prime_substitutions = 0
        for i in range(10):
            if fill_template(str(base), template, str(i)) in primes:
                prime_substitutions += 1
        if prime_substitutions >= target:
            return fill_template(str(base), template, '1')
    return False

def euler51():
    """http://projecteuler.net/problem=51

    By replacing the 1st digit of *3, it turns out that six of the nine
    possible values: 13, 23, 43, 53, 73, and 83, are all prime.

    By replacing the 3rd and 4th digits of 56**3 with the same digit, this
    5-digit number is the first example having seven primes among the ten
    generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
    56773, and 56993. Consequently 56003, being the first member of this
    family, is the smallest prime with this property.

    Find the smallest prime which, by replacing part of the number (not
    necessarily adjacent digits) with the same digit, is part of an eight prime
    value family.
    """
    for p in sorted(primes):
        if test_templates(p):
            return test_templates(p)
