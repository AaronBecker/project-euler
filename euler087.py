
from euler_util import sieve

def count_combinations(limit):
    primes = sieve(int(limit ** 0.5))
    squares = [p ** 2 for p in primes if p ** 2 < limit]
    cubes = [p ** 3 for p in primes if p ** 3 < limit]
    fourths = [p ** 4 for p in primes if p ** 4 < limit]
    results = set()
    for s in squares:
        for c in cubes:
            for f in fourths:
                if s + c + f < limit:
                    results.add(s + c + f)
    return len(results)


def euler87(limit=50000000):
    """http://projecteuler.net/problem=87

    The smallest number expressible as the sum of a prime square, prime cube,
    and prime fourth power is 28. In fact, there are exactly four numbers
    below fifty that can be expressed in such a way:

    28 = 2**2 + 2**3 + 2**4
    33 = 3**2 + 2**3 + 2**4
    49 = 5**2 + 2**3 + 2**4
    47 = 2**2 + 3**3 + 2**4

    How many numbers below fifty million can be expressed as the sum of a prime
    square, prime cube, and prime fourth power?
    """
    return count_combinations(limit)
