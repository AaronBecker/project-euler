
def partials(n):
    p, seen = [], {}
    sqrt, sqrt_floor = n**0.5, int(n**0.5)
    if sqrt_floor == n**0.5: return []
    m, d, a = 0, 1, sqrt_floor
    while True:
        seen[(m, d, a)] = True
        m = d * a - m
        d = (n - m**2) / d
        a = int((sqrt + m) / d)
        if seen.has_key((m, d, a)): return p
        p.append(a)

def euler64(limit=10000):
    """http://projecteuler.net/problem=64

    All square roots are periodic when written as continued fractions.
 
    The first ten continued fraction representations of (irrational) square
    roots are:
 
    2=[1;(2)], period=1
    3=[1;(1,2)], period=2
    5=[2;(4)], period=1
    6=[2;(2,4)], period=2
    7=[2;(1,1,1,4)], period=4
    8=[2;(1,4)], period=2
    10=[3;(6)], period=1
    11=[3;(3,6)], period=2
    12= [3;(2,6)], period=2
    13=[3;(1,1,1,1,6)], period=5
 
    Exactly four continued fractions, for N <= 13, have an odd period.
 
    How many continued fractions for N <= 10000 have an odd period?
    """
    return sum(1 for n in xrange(limit+1) if len(partials(n)) % 2 != 0)
