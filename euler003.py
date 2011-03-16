
def euler3(target=317584931803):
    """What is the largest prime factor of the number 317584931803?"""
    orig_target = target
    sqrt_target = int(target ** 0.5) + 1
    i = 1
    while i < sqrt_target:
        if target % i == 0:
            factor = i
            target = target / i
        i += 1
    print "The largest prime factor of %d is %d\n" % (orig_target, factor)
    return factor

