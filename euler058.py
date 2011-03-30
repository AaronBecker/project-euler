
from euler_util import is_prime

def euler58():
    """http://projecteuler.net/index.php?section=problems&id=58

    Investigate the number of primes that lie on the diagonals of the spiral
    grid.""" 
    value, side, count = 1, 2, 0
    primes, total = 0, 0
    while True:
        primes, total = primes + is_prime(value), total + 1
        if count == 0:
            if primes > 0 and float(primes)/total < 0.1:
                return side - 1
        count, value = count + 1, value + side
        if count == 4:
            side, count = side + 2, 0

