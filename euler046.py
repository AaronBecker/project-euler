from euler_util import sieve

def euler46():
    """http://projecteuler.net/index.php?section=problems&id=46
    
    What is the smallest odd composite that cannot be written as the sum of a
    prime and twice a square?"""
    double_squares = [2*n*n for n in range(1000)]
    primes = set(sieve(10 ** 6))
    for n in range(2, 10 ** 6):
        found = False
        for ds in double_squares:
            if ds > n: break
            if n-ds in primes:
                found = True
                break
        if not found and n % 2 == 1: return n
