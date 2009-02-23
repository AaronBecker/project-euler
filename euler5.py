from euler_util import LCM

def euler5(upper_bound=20):
    """What is the smallest number that is evenly divisible by all of the numbers
    from 1 to 20?"""
    result = LCM(range(1, upper_bound+1))
    print "The smallest number evenly divisible by all numbers from 1 to %d is %d\n" %\
            (upper_bound, result)
    return result

