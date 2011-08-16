
from math import factorial

chains = {}
facts = map(factorial, range(10))
def chain_length(n):
    value, chain = n, set()
    while value not in chain:
        if value in chains:
            chains[n] = chains[value] + len(chain)
            return chains[n]
        chain.add(value)
        value = sum(facts[int(d)] for d in str(value))
    chains[n] = len(chain)
    return chains[n]
    

def euler74(ub=10**6):
    """http://projecteuler.net/index.php?section=problems&id=74

    The number 145 is well known for the property that the sum of the factorial
    of its digits is equal to 145:

    1! + 4! + 5! = 1 + 24 + 120 = 145

    Perhaps less well known is 169, in that it produces the longest chain of
    numbers that link back to 169; it turns out that there are only three such
    loops that exist:

    169  363601  1454  169
    871  45361  871
    872  45362  872

    It is not difficult to prove that EVERY starting number will eventually get
    stuck in a loop. For example,

    69  363600  1454  169  363601 (1454)
    78  45360  871  45361 (871)
    540  145 (145)

    Starting with 69 produces a chain of five non-repeating terms, but the longest
    non-repeating chain with a starting number below one million is sixty terms.

    How many chains, with a starting number below one million, contain exactly
    sixty non-repeating terms?"""    
    return sum(1 for x in xrange(1, ub+1) if chain_length(x) == 60)
