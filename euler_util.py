
import sys

def trim(docstring):
    """Format a docstring for presentation."""
    # See http://www.python.org/dev/peps/pep-0257/
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxint
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxint:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)

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

def gcd(a,b):
   """Return greatest common divisor using Euclid's Algorithm."""
   while b:      
	a, b = b, a % b
   return a

def lcm(a,b):
   """Return least common multiple."""
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
    m is the largest prime <= n. Takes O(n) space."""
    n = n + 1
    sieve = range(n)
    sieve[:2] = [0, 0]
    for i in xrange(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in xrange(i ** 2, n, i):
                sieve[j] = 0
    # Filter out the composites, which have been replaced by 0's
    return [p for p in sieve if p]
sieve = sieve_of_eratosthenes

factor_primes = []
factor_primes_max = 0
def factor(number):
    """ Return a list of prime factors of n"""
    global factor_primes, factor_primes_max
    factors = [1]
    sqrt = int(number ** 0.5) + 1
    if sqrt > factor_primes_max:
        factor_primes_max = max(sqrt, 2*factor_primes_max)
        factor_primes = sieve_of_eratosthenes(factor_primes_max)
    index = 0 
    while index < len(factor_primes) and factor_primes[index] <= sqrt:
        prime = factor_primes[index]
        while number % prime == 0:
            number /= prime
            factors.append(prime)
        index += 1
    if number > 1:
        factors.append(number)
    return factors

def expmod(x, n, m):
    """ Compute x**n mod m"""
    result = 1
    while n > 0:
        if n % 2 != 0:
            result, n = (result*x) % m, n - 1
        x, n = (x**2) % m, n/2
    return result

import random
def probably_prime(n):
    """Do a probabalistic primality test using the Miller-Rabin algorithm."""
    if n < 3: return n == 2
    if n == 3: return True
    if n % 2 == 0: return False
    # First write n as 2**s * d, with d odd.
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s + 1, d/2
    # This set of candidates is good up to 341,550,071,728,321
    assert n < 341550071728321
    for a in [2, 3, 5, 7, 11, 13, 17]:
        if a >= n: return True
        x = expmod(a, d, n)
        if x == 1: continue
        for r in xrange(s-1):
            if x == n-1: break
            x = (x**2) % n
        if x != n-1: return False
    return True

def is_prime(number):
    """Simple divisibility test for primality"""
    if number < 341550071728321: return probably_prime(number)
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def divisors(number):
    """Return a list of proper divisors of n"""
    divisors = [1]
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            divisors.append(number/i)
    return divisors

def totient(n):
    """Computes Euler's totient"""
    factors = factor(n)
    phi, last_f = 1, 1
    for f in factors:
        if f == last_f:
            phi *= f
        else:
            phi, last_f = phi*(f - 1), f
    return phi

def is_palindrome(candidate):
    """Determine whether or not a number (or any string) is palindromic"""
    digits = [digit for digit in str(candidate)]
    return (digits == digits[::-1])

def is_pandigital(candidate):
    """Determine whether or not a number with n digits contains all the
    digits from 1 to n"""
    if candidate > 987654321: return False
    digits = [digit for digit in str(candidate)]
    for i in range(1, len(digits)+1):
        if not str(i) in digits: return False
    return True

# nice permutation generator from Michael Davies
# http://code.activestate.com/recipes/252178/
def permutations(str):
    """Yield all permutations of a given list or string"""
    if len(str) <=1:
        yield str
    else:
        for perm in permutations(str[1:]):
            for i in range(len(perm)+1):
                #nb str[0:1] works in both string and list contexts
                yield perm[:i] + str[0:1] + perm[i:]

