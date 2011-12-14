
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
    """
    FIXME: docstring
    """
    return count_combinations(limit)
