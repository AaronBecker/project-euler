
from euler_util import sieve

primes = set(sieve(10**8))
print 'done sieving'
def euler58():
    """http://projecteuler.net/index.php?section=problems&id=58

    Investigate the number of primes that lie on the diagonals of the spiral
    grid.""" 
    max_prime = max(primes)
    value, side, count = 1, 2, 0
    primality = [0, 0]
    while True:
        if value > max_prime:
            print 'value %d exceeded max prime %d' % (value, max_prime)
            return 0
        primality[value in primes] += 1

        if count == 0:
            #print value, side - 1
            #print primality[True], primality[True] + primality[False], float(primality[True]) / (primality[True] + primality[False])
            #print ''
            #print float(primality[True]) / (primality[True] + primality[False])
            #print ''
            if primality[True] > 0 and float(primality[True]) / (primality[True] + primality[False]) < 0.1:
                return side - 1

        count, value = count + 1, value + side
        if count == 4:
            side += 2
            count = 0
        #if side > 10: return 0

