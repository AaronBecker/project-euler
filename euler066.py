
def partials(n):
    p, seen = [], {}
    sqrt, sqrt_floor = n**0.5, int(n**0.5)
    if sqrt_floor == n**0.5: return []
    m, d, a = 0, 1, sqrt_floor
    while True:
        seen[(m, d, a)] = True
        m = d * a - m
        d = (n - m**2) / d
        a = int((sqrt + m) / d)
        if seen.has_key((m, d, a)): return p
        p.append(a)

def pell(d):
    if d**0.5 == int(d**0.5): return 0
    n, p, num, denom = 0, partials(d), int(d**0.5), 1
    old_num, old_denom, num, denom = num, denom, p[0]*num+1, p[0]
    print p
    print old_num, old_denom
    if old_num**2 - d * old_denom**2 == 1:
        return old_num
    print num, denom
    if num**2 - d * denom**2 == 1:
        return num
    while True:
        # formula appears to be wrong...check with d=7
        n, partial = n+1, p[(n+1) % len(p)]
        num, denom = partial*num + old_num, partial*denom + old_denom
        old_num, old_denom = num, denom
        print num, denom
        if num**2 - d * denom**2 == 1:
            return num
        if n > 100: return False

def euler66(term=1000):
    """http://projecteuler.net/index.php?section=problems&id=66
    
    Consider quadratic Diophantine equations of the form:

        x**2 – Dy**2 = 1

    For example, when D=13, the minimal solution in x is 6492 – 131802 = 1.

    It can be assumed that there are no solutions in positive integers when
    D is square.

    By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain
    the following:

        3**2 – 2*2**2 = 1
        2**2 – 3*1**2 = 1
        9**2 – 5*4**2 = 1
        5**2 – 6*2**2 = 1
        8**2 – 7*3**2 = 1

    Hence, by considering minimal solutions in x for D  7, the largest
    x is obtained when D=5.

    Find the value of D <= 1000 in minimal solutions of x for which the
    largest value of x is obtained.
    """
    print pell(7)
    #for x in xrange(2, 8):
    #    print pell(x)
    #return sum(int(d) for d in str(nth_e_convergent(term).numerator))
