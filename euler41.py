from euler_util import permutations

def is_prime(x):
    for i in xrange(2, int(x**0.5) + 1):
        if x % i == 0: return False
    return True

def euler41():
    """What is the largest n-digit pandigital prime?"""
    primes = []
    # note: sum(1..8) % 3 == sum(1..9) % 3 == 0, so 7 digits is the max
    for perm in permutations("1234567"):
        if is_prime(int(perm)):
            primes.append(int(perm))
    primes.sort()
    print 'The largest pandigital prime is %d' % primes[-1]
    return primes[-1]

