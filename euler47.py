from euler_util import factor

def euler47():
    """Find the first four consecutive integers to
    have four distinct primes factors."""
    current = 1
    current_run = 0
    while True:
        if len(set(factor(current))) - 1 == 4:
            current_run += 1
            if current_run == 4:
                print current - 3
                return current - 3
        else:
            current_run = 0
        current += 1
