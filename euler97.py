
def euler97():	
    """Find the last ten digits of the non-Mersenne prime: 
    28433 x 2^7830457 + 1."""
    r = (2**7830457 * 28433 + 1) % 10000000000
    print 'The last 10 digits of 28433 x 2^7830457 + 1 are %d' % r
    return r

