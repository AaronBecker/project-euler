
def euler29(a_max=101, b_max=101):
    """http://projecteuler.net/index.php?section=problems&id=29
    
    How many distinct terms are in the sequence generated by
    a ** b for 2 <= a <= 100 and 2 <= b <= 100?"""
    terms = set()
    for a in range(2, a_max):
        for b in range(2, b_max):
            terms.add(a ** b)
    return len(terms)

