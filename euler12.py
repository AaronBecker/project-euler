from euler_util import count_factors

def euler12(target=500):
    """What is the first triangular number to have over 
    five hundred divisors?"""
    n = target
    last_factors = count_factors(n-1)
    while 1:
        factors = count_factors(n)
        if factors * last_factors - max(factors, last_factors) >= target:
            print "Trying %d * %d / 2" % (n-1, n)
            f = count_factors(n*(n-1)/2) 
            if f <= target:
                print "only %d factors, continuing..." % f
                n += 1
                continue
            print "The first triangular number with "\
                    "at least %d factors is %d" % (target, n * (n - 1) / 2)
            print n
            return n * (n - 1) / 2
        last_factors = factors
        n += 1

