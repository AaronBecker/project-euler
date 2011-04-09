
def count_factors(x):
    """Count the factors (not necessarily prime) of x"""
    factors = 2 # 1 and x
    for i in xrange(2, int(x**0.5) + 1):
        if x % i == 0:
            factors += 2
    return factors

def euler12(target=500):
    """http://projecteuler.net/index.php?section=problems&id=12
    
    What is the first triangular number to have over five hundred divisors?"""
    n = target
    last_factors = count_factors(n-1)
    while 1:
        factors = count_factors(n)
        if factors * last_factors - max(factors, last_factors) >= target:
            f = count_factors(n*(n-1)/2) 
            if f <= target:
                n += 1
                continue
            return n * (n - 1) / 2
        last_factors = factors
        n += 1

