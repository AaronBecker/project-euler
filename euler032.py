
from euler_util import is_pandigital

def is_pandigital_product(x, y):
    product_string = str(x) + str(y) + str(x*y)
    if len(product_string) != 9: return False
    return is_pandigital(int(product_string))

def euler32():
    """http://projecteuler.net/index.php?section=problems&id=32
    
    Find the sum of all numbers that can be written as pandigital products."""
    return sum(set(x*y for x in range(1,50) for y in range(1,
        2000) if x < y and is_pandigital_product(x, y)))

