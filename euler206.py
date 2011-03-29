import re

template = re.compile("1.2.3.4.5.6.7.8.9")
def check_template(n):
    return template.match(str(n))

def euler206():
    """http://projecteuler.net/index.php?section=problems&id=206

    Find the unique positive integer whose square has the form
    1_2_3_4_5_6_7_8_9_0, where each "_" is a single digit."""
    # note: n^2 ends in 0, so the last _ is also a zero and n
    # also ends in zero.
    for n in xrange(int(19293949596979899 ** 0.5), int(10203040506070809 ** 0.5), -1):
        if check_template(n*n): return n*10
