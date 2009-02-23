from euler_util import sieve_of_eratosthenes, is_pandigital

def euler41():
    """What is the largest n-digit pandigital prime?"""
    for prime in sieve_of_eratosthenes(10 ** 9).reverse():
        if is_pandigital(prime):
            print 'The largest pandigital prime is %d' % prime
            return prime
    return 0

