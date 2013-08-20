
def euler97():
    """http://projecteuler.net/problem=97

    Find the last ten digits of the non-Mersenne prime: 28433 x 2^7830457 + 1.
    """
    return (2**7830457 * 28433 + 1) % 10000000000

