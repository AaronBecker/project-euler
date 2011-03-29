
def collatz(upper_bound):
    """Generate number of terms in Collatz sequence for n (n/2 or 3n+1)"""
    known_terms = []
    for n in xrange(1, upper_bound):
        terms = 1
        while n != 1:
            if len(known_terms) >= n:
                terms = known_terms[n-1] + terms - 1
                break
            if n % 2 == 0:
                n /= 2
            else:
                n = 3*n + 1
            terms += 1
        known_terms.append(terms)
        yield terms

def euler14(upper_bound=1000000):
    """http://projecteuler.net/index.php?section=problems&id=14
    
    Which starting number under one million produces the longest Collatz chain?
    """
    return max(zip(collatz(upper_bound), range(1, upper_bound)))[1]

