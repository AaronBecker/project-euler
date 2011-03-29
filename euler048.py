
def euler48():
    """http://projecteuler.net/index.php?section=problems&id=48
    
    Find the last ten digits of 1^1 + 2^2 + ... + 1000^1000.  """
    sum = 0
    for x in range(1, 1001):
        sum += x ** x % 10 ** 10
    return sum % 10 ** 10
