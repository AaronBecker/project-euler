from euler_util import factorial

def euler20(x=100):
    """http://projecteuler.net/index.php?section=problems&id=20
    
    Find the sum of digits in 100!"""    
    return sum([int(c) for c in str(factorial(x))])

