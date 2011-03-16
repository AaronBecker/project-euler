
def euler15(x=2**1000):
    """What is the sum of the digits of the number 2**1000?"""
    digit_sum = sum([int(d) for d in str(x)])
    print "The sum of the digits of is %d" % digit_sum
    return digit_sum

