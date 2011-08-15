from itertools import permutations

def is_prime(x):
    for i in xrange(2, int(x**0.5) + 1):
        if x % i == 0: return False
    return True

def euler41():
    """http://projecteuler.net/index.php?section=problems&id=41

    What is the largest n-digit pandigital prime?"""
    primes = []
    # note: sum(1..8) % 3 == sum(1..9) % 3 == 0, so 7 digits is the max
    for perm in permutations("1234567"):
        val = int(''.join(perm))
        if is_prime(val):
            primes.append(val)
    return max(primes)

