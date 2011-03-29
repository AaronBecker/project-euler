
def euler2(upper_bound=1000000):
    """http://projecteuler.net/index.php?section=problems&id=2
    
    Find the sum of all the even-valued terms in the Fibonacci sequence which
    do not exceed one million."""
    f1, f2 = 2, 1
    even_sum = 0
    while f1 < upper_bound:
        if f1 % 2 == 0:
            even_sum = even_sum + f1
        f1, f2 = f1+f2, f1
    return even_sum

