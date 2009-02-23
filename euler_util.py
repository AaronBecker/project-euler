
def count_factors(x):
    """Count the factors (not necessarily prime) of x"""
    factors = 2 # 1 and x
    for i in xrange(2, int(x**0.5) + 1):
        if x % i == 0:
            factors += 2
    return factors

def factorial(x):
    """Compute x!"""
    fac = 1
    for i in range(1, x+1):
        fac *= i
    return fac

# simple number theory functions modified from http://www.4dsolutions.net
def gcd(a,b):
   """Return greatest common divisor using Euclid's Algorithm."""
   while b:      
	a, b = b, a % b
   return a

def lcm(a,b):
   """Return lowest common multiple."""
   return (a*b)/gcd(a,b)

def GCD(terms):
   """Return gcd of a list of numbers."""
   return reduce(lambda a,b: gcd(a,b), terms)

def LCM(terms):
   """Return lcm of a list of numbers."""   
   return reduce(lambda a,b: lcm(a,b), terms)

# quick prime sieve from literateprograms.org
def sieve_of_eratosthenes(n):
    """Generate a list of the prime numbers [2, 3, ... m] where
    m is the largest prime <= n."""
    n = n + 1
    sieve = range(n)
    sieve[:2] = [0, 0]
    for i in xrange(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in xrange(i ** 2, n, i):
                sieve[j] = 0
    # Filter out the composites, which have been replaced by 0's
    return [p for p in sieve if p]

def factor(number):
    factors = [1]
    sqrt = int(number ** 0.5) + 1
    primes = sieve_of_eratosthenes(sqrt)
    index = 0 
    while primes[index] <= sqrt:
        prime = primes[index]
        while number % prime == 0:
            number /= prime
            factors.append(prime)
        index += 1
    factors.append(number)
    return factors

def is_pandigital(candidate):
    """Determine whether or not a number with n digits contains all the
    digits from 1 to n"""
    digits = [digit for digit in str(candidate)]
    for i in range(1, len(digits)+1):
        if not str(i) in digits: return False
    return True

