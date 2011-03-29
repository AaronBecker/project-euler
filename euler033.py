
from fractions import Fraction

def can_cancel(num, denom):
    if num >= denom or num % 10 == 0 and denom % 10 == 0: return False
    sn, sd = str(num), str(denom)
    if sn[0] in sd:
        sn, sd = sn[1], sd.replace(sn[0], '', 1)
    elif sn[1] in sd:
        sn, sd = sn[0], sd.replace(sn[1], '', 1)
    else:
        return False
    if int(sd) == 0: return False
    return Fraction(num, denom) == Fraction(int(sn), int(sd))


def euler33():
    """http://projecteuler.net/index.php?section=problems&id=33
    
    Find the fractions with an unorthodox cancelling method."""
    fracs = [Fraction(num, denom) for num in range(10, 100) \
            for denom in range(10, 100) if can_cancel(num, denom)]
    return reduce(lambda x, y: x*y, fracs).denominator

