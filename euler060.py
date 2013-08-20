
from euler_util import sieve, is_prime

def concat_prime(p1, p2):
    if not is_prime(int(str(p1)+str(p2))): return False
    if not is_prime(int(str(p2)+str(p1))): return False
    return True

def concat_primes(n, primes):
    for p in primes:
        if not concat_prime(n, p): return False
    return True

def euler60():
    """http://projecteuler.net/problem=60

    The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
    primes and concatenating them in any order the result will always be prime.
    For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of
    these four primes, 792, represents the lowest sum for a set of four primes
    with this property.

    Find the lowest sum for a set of five primes for which any two primes
    concatenate to produce another prime.
    """
    primes = sieve(10000)  # turns out 10k is enough for a set of 5.
    for p1 in primes:
        for p2 in primes:
            if p2 <= p1 or not concat_prime(p1, p2): continue
            for p3 in primes:
                if p3 <= p2 or not concat_primes(p3, [p1, p2]): continue
                for p4 in primes:
                    if p4 <= p3 or not concat_primes(p4, [p1, p2, p3]): continue
                    for p5 in primes:
                        if p5 <= p4 or not concat_primes(p5, [p1, p2, p3, p4]): continue
                        return sum([p1, p2, p3, p4, p5])

    
