from math import factorial

def euler53(upper_bound=10**6):
    """http://projecteuler.net/index.php?section=problems&id=53
    
    How many values of C(n,r), for 1 <= n <= 100, exceed one-million?"""
    found = 0
    for n in range(1, 101):
        nfac = factorial(n)
        for r in range(1, n):
            c = nfac / factorial(r) / factorial(n-r)
            if c > upper_bound:
                found += 1
    return found
