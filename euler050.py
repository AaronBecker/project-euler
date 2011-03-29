from euler_util import sieve_of_eratosthenes

def euler50(upper_bound=1000000):
    """http://projecteuler.net/index.php?section=problems&id=50
    
    Which prime, below one-million, can be written as the sum of the most
    consecutive primes?"""
    primes = sieve_of_eratosthenes(upper_bound)
    prime_sums = [primes[0]] * len(primes)
    for i in range(len(primes)-1):
        prime_sums[i+1] = primes[i+1] + prime_sums[i] 
    primes_set = set(primes)
    current_candidate = 1
    current_candidate_length = 1
    # note: the sum of the first 1000 primes is well over 10^6, so don't try
    # longer sequences
    for start in range(len(primes)):
        for end in range(start + current_candidate_length, min(len(primes), start+1000)):
            prime_slice = primes[start:end+1]
            slice_sum = prime_sums[end] - prime_sums[start]
            if slice_sum > upper_bound: break
            if slice_sum in primes_set and end - start > current_candidate_length:
                current_candidate = slice_sum
                current_candidate_length = end - start
    return current_candidate

