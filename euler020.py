from euler_util import factorial

def euler20(x=100):
    """Find the sum of digits in 100!"""    
    s = sum([int(c) for c in str(factorial(x))])
    print 'The sum of the digits of %d is %d' % (x, s)
    return s

