
def euler16(x=2**1000):
    """http://projecteuler.net/index.php?section=problems&id=16
    
    What is the sum of the digits of the number 2**1000?"""
    return sum([int(d) for d in str(x)])

