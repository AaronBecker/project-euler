
import functools


def trim(docstring):
    import sys
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


class memoized(object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """
    # see http://wiki.python.org/moin/PythonDecoratorLibrary
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not args in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)


def product(numbers):
    import operator
    return reduce(operator.mul, numbers)


def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return the least common multiple of a and b."""
    return (a * b) / gcd(a, b)


def GCD(terms):
    """Return gcd of a list of numbers."""
    return reduce(lambda a, b: gcd(a, b), terms)


def LCM(terms):
    """Return lcm of a list of numbers."""
    return reduce(lambda a, b: lcm(a, b), terms)


def sieve_of_eratosthenes(n):
    """Generate a list of the prime numbers [2, 3, ... m] where
    m is the largest prime <= n. Takes O(n) space."""
    # see literateprograms.org
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


def factor(number):
    """Return a list of prime factors of n"""
    factors, sqrt = [1], int(number ** 0.5) + 1
    if sqrt > factor.primes_max:
        factor.primes_max = max(sqrt, 2 * factor.primes_max)
        factor.primes = sieve(factor.primes_max)
    for prime in factor.primes:
        if prime > sqrt: break
        while number % prime == 0:
            number /= prime
            factors.append(prime)
    if number > 1:
        factors.append(number)
    return factors
factor.primes = []
factor.primes_max = 0


def expmod(x, n, m):
    """Compute x**n mod m"""
    result = 1
    while n > 0:
        if n % 2 != 0:
            result, n = (result * x) % m, n - 1
        x, n = (x ** 2) % m, n / 2
    return result


def miller_rabin(n, tests):
    """Do a probabalistic primality test using the Miller-Rabin algorithm."""
    # First write n as 2**s * d, with d odd.
    s, d = 0, n - 1
    while d % 2 == 0:
        s, d = s + 1, d / 2
    # Now perform the tests
    for a in tests:
        x = expmod(a, d, n)
        if x == 1: continue
        for r in xrange(s - 1):
            if x == n - 1:
                break
            x = (x ** 2) % n
        if x != n - 1: return False
    return True


def miller_rabin_candidates(n):
    """Provide a set of tests that guarantees that miller-rabin will be
    correct for numbers n or less."""
    if n < 1373653: return [2, 3]
    if n < 9080191: return [31, 73]
    if n < 4759123141: return [2, 7, 61]
    c = [2, 3, 5, 7, 11]
    if n > 2152302898747: c.append(13)
    if n > 3474749660383: c.append(17)
    if n > 341550071728321: assert False
    return c


def is_prime(n):
    """Determine whether or not n is prime"""
    if n < 2: return False
    if n % 2 == 0 or n % 3 == 0: return False
    return miller_rabin(n, miller_rabin_candidates(n))


def divisors(number):
    """Return a list of proper divisors of n"""
    divisors = [1]
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            divisors.append(number / i)
    return divisors


def totient(n):
    """Compute Euler's totient"""
    factors = factor(n)
    phi, last_f = 1, 1
    for f in factors:
        if f == last_f:
            phi *= f
        else:
            phi, last_f = phi * (f - 1), f
    return phi


def is_palindrome(candidate):
    """Determine whether or not a number (or any string) is palindromic"""
    digits = [digit for digit in str(candidate)]
    return (digits == digits[::-1])


def is_pandigital(candidate):
    """Determine whether or not a number with n digits contains all the
    digits from 1 to n"""
    if int(candidate) > 987654321: return False
    digits = [digit for digit in str(candidate)]
    for i in range(1, len(digits) + 1):
        if not str(i) in digits: return False
    return True


def shortest_path(start, neighbors, weight, goal):
    """Find a minimum-cost path to a goal state using Dijkstra's algorithm.

    Takes an initial state, a function mapping states to neighbor states, a
    a function mapping states to weights, and a function that indicates whether
    or not a state is a goal state.
    """
    import heapq
    visited, q = set(), []
    heapq.heappush(q, (weight(start), [start]))
    while len(q) > 0:
        cost, path = heapq.heappop(q)
        if goal(path[-1]): return (cost, path)
        if path[-1] in visited: continue
        visited.add(path[-1])
        for n in neighbors(path[-1]):
            if n not in visited:
                new_path = path[:] + [n]
                heapq.heappush(q, (cost + weight(n), new_path))
