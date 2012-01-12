
from euler_util import is_prime


def euler131(upper_bound=10**6):
    """http://projecteuler.net/problem=131

    There are some prime values, p, for which there exists a positive integer,
    n, such that the expression n**3 + pn**2 is a perfect cube.

    For example, when p = 19, 83 + 82*19 = 123.

    What is perhaps most surprising is that for each prime with this property
    the value of n is unique, and there are only four such primes below
    one-hundred.

    How many primes below one million have this remarkable property?
    """
    # Since n**3 + p*n**2 = (n+p)*n**2 with p prime, n and n+p are both
    # perfect cubes. So, this is just an alternative formulation for Cuban
    # primes: http://oeis.org/A002407
    #
    # These are also identical to the centered hexagonal numbers that are
    # also prime.
    hexes = [3*n*(n+1)+1 for n in xrange(int(upper_bound**0.5))]
    hexes = [n for n in hexes if n < upper_bound]
    return len([1 for n in hexes if is_prime(n)])

