
def euler3(target=317584931803):
    """http://projecteuler.net/problem=3
    
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?
    """
    for i in xrange(2, int(target ** 0.5)):
        while target % i == 0:
            factor, target = i, target / i
    return factor

