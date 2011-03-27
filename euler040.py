
from math import log10

def euler40():
    """Finding the nth digit of the fractional part of the irrational
    number."""
    n, length = 1, 0
    while (length < 1000000):
        n, length = n + 1, length + int(log10(n))
    irrational = ''.join(str(n) for n in range(1, n))
    result = reduce(lambda x,y: x*y, 
            [int(irrational[d]) for d in 0,9,99,999,9999,99999,999999])
    print 'The product of digits is %d' % result
    return result

