
def euler28(size=1001):
    """http://projecteuler.net/index.php?section=problems&id=28
    
    What is the sum of both diagonals in a 1001 by 1001 spiral?"""
    counter, dim, sum = 1, 2, 1
    for i in range((size-1)/2):
        sum += 4*counter + 10*dim
        counter += 4*dim
        dim +=2
    return sum
