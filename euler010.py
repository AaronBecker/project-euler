from euler_util import sieve

def euler10(target=1000000):
    """http://projecteuler.net/index.php?section=problems&id=10
    
    Calculate the sum of all the primes below two million."""
    return sum(sieve(target))

