from euler_util import sieve


def euler7(n=10001):
    """http://projecteuler.net/problem=7

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10001st prime number?
    """
    # Find all primes less than some initial guess. If that doesn't provide
    # enough primes, try again with a bigger guess.
    primes, guess = [], 1000000
    while len(primes) < n:
        primes, guess = sieve(guess), guess * 2
    return primes[n - 1]
