

def euler16(x=2 ** 1000):
    """http://projecteuler.net/problem=16

    2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 21000?
    """
    return sum([int(d) for d in str(x)])
