
def euler25():
    """What is the first term in the Fibonacci sequence
    to contain 1000 digits?"""
    f1, f2, term = 2, 1, 3
    while f1 < 10 ** 999:
        f1, f2, term = f1+f2, f1, term + 1
    print "Fibonacci term %d is %d" % (term, f1)
    return term

