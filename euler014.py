

def collatz(upper_bound):
    """Generate number of terms in the Collatz sequence
    for integers from 1 up to n."""
    known_terms = []
    for n in xrange(1, upper_bound):
        terms = 1
        while n != 1:
            if len(known_terms) >= n:
                terms = known_terms[n - 1] + terms - 1
                break
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1
            terms += 1
        known_terms.append(terms)
        yield terms


def euler14(upper_bound=1000000):
    """http://projecteuler.net/problem=14

    The following iterative sequence is defined for the set of positive
    integers:

    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following
    sequence:

    13  40  20  10  5  16  8  4  2  1

    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """
    return max(zip(collatz(upper_bound), range(1, upper_bound)))[1]
