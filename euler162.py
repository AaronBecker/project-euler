
def single_recurrence(total, last):
    return 15*last + total

def double_recurrence(total, last, first, second):
    return 14*last + first + second

def triple_recurrence(total, last, first, second, third):
    return 13*last + first + second + third

def euler162():
    """http://projecteuler.net/index.php?section=problems&id=162

    Hexadecimal numbers"""
    total, has_0, has_1, has_a = 15, 0, 1, 1
    has_10 = has_a0 = has_a1 = has_a10 = a10_total = 0
    for i in xrange(2, 17):
        total, has_0, has_1, has_a, has_10, has_a0, has_a1, has_a10 = \
                15*16**(i-1), \
                single_recurrence(total, has_0), \
                single_recurrence(total, has_1), \
                single_recurrence(total, has_a), \
                double_recurrence(total, has_10, has_1, has_0), \
                double_recurrence(total, has_a0, has_a, has_0), \
                double_recurrence(total, has_a1, has_a, has_1), \
                triple_recurrence(total, has_a10, has_a1, has_a0, has_10)
        a10_total += has_a10
    return "%X" % a10_total

