
def check_template(n):
    s = str(n)
    return s[0] == '1' and\
            s[2] == '2' and\
            s[4] == '3' and\
            s[6] == '4' and\
            s[8] == '5' and\
            s[10] == '6' and\
            s[12] == '7' and\
            s[14] == '8' and\
            s[16] == '9'

def euler206():
    """Find the unique positive integer whose square has the form
    1_2_3_4_5_6_7_8_9_0, where each "_" is a single digit."""
    # note: n^2 ends in 0, so the last _ is also a zero and n
    # also ends in zero. n^2/100 ends in 9, so its square root
    # ends in 3 or 7
    s = 0
    for n in xrange(int(10203040506070809 ** 0.5), int(19293949596979899 ** 0.5)):
        if check_template(n*n):
            print n, n*n
            print '%d^2 = %d' % (n*10, n**2 * 100)
            return
