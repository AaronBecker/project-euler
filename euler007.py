from euler_util import sieve_of_eratosthenes

def euler7(n=10001):
    """http://projecteuler.net/index.php?section=problems&id=7
    
    Find the 100001st prime."""
    # Find all primes less than some initial guess. If that doesn't provide enough
    # primes, try again with a bigger guess
    guess = 1000000
    primes = []
    while len(primes) < n:
        primes = sieve_of_eratosthenes(guess)
        guess *= 2
    return primes[n-1]

