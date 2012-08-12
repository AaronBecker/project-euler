

def count_factors(x):
    """Count the factors (not necessarily prime) of x"""
    factors = 2  # 1 and x
    for i in xrange(2, int(x ** 0.5) + 1):
        if x % i == 0:
            factors += 2
    return factors


def euler12(target=500):
    """http://projecteuler.net/problem=12

    The sequence of triangle numbers is generated by adding the natural
    numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 =
    28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred
    divisors?
    """
    n = target
    last_factors = count_factors(n - 1)
    while 1:
        factors = count_factors(n)
        if factors * last_factors - max(factors, last_factors) >= target:
            f = count_factors(n * (n - 1) / 2)
            if f <= target:
                n += 1
                continue
            return n * (n - 1) / 2
        last_factors = factors
        n += 1
