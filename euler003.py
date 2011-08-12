
def euler3(target=317584931803):
    """http://projecteuler.net/index.php?section=problems&id=3
    
    What is the largest prime factor of the number 317584931803?"""
    i, sqrt_target = 1, int(target ** 0.5) + 1
    while i < sqrt_target:
        if target % i == 0:
            factor, target = i, target / i
        i += 1
    return factor

