
def euler3(target=317584931803):
    """http://projecteuler.net/index.php?section=problems&id=3
    
    What is the largest prime factor of the number 317584931803?"""
    orig_target = target
    sqrt_target = int(target ** 0.5) + 1
    i = 1
    while i < sqrt_target:
        if target % i == 0:
            factor = i
            target = target / i
        i += 1
    return factor

