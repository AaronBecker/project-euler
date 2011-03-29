from euler_util import sieve

def euler49():
    """http://projecteuler.net/index.php?section=problems&id=49

    Find arithmetic sequences, made of prime terms, whose four digits are
    permutations of each other."""
    primes = [prime for prime in sieve(10000) if prime > 999]
    prime_digits = [list(str(prime)) for prime in primes]
    for prime in prime_digits:
        prime.sort()
    prime_digits = [''.join(prime) for prime in prime_digits]
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            if prime_digits[i] != prime_digits[j]: continue
            if 2 * primes[j] - primes[i] not in primes: continue
            x = 2 * primes[j] - primes[i]
            k = list(str(x))
            k.sort()
            k = ''.join(k)
            if (k == prime_digits[i]):
                if primes[i] != 1487:
                    return str(primes[i]) + str(primes[j]) + str(x)
