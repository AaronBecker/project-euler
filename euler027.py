from euler_util import sieve

primes = set(sieve(10 ** 6))

def quad_score(a, b):
    score = 0
    while score*score + a*score + b in primes: score += 1
    return score

def euler27():
    """http://projecteuler.net/index.php?section=problems&id=27
    
    Find a quadratic formula that produces the maximum number of primes for
    consecutive values of n."""
    best_a, best_b, best_score = 0, 0, 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            score = quad_score(a, b)
            if score > best_score:
                best_a, best_b, best_score = a, b, score
    return best_a * best_b
