from euler_util import sieve_of_eratosthenes

def euler10(target=1000000):
    prime_sum = sum(sieve_of_eratosthenes(target))
    print "The sum of all primes less than %d is %d." % (target, prime_sum)
    return prime_sum

