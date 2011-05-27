
roman_value = {
    'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000
}
def numeral_to_int(numeral):
    value = 0
    length = len(numeral)
    for i in xrange(length):
        if i < length-1 and roman_value[numeral[i+1]] > roman_value[numeral[i]]:
            value -= roman_value[numeral[i]]
        else:
            value += roman_value[numeral[i]]
    return value

integral_value = [ (1000, 'M'), (900, 'CM'), (500, 'D'),
        (400, 'CD'), (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'), (10, 'X'),
        (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I') ]
def int_to_numeral(n):
    numeral = ''
    for (value, fragment) in integral_value:
        while n >= value:
            n, numeral = n-value, numeral+fragment
    return numeral

def minimize_numeral(numeral):
    return int_to_numeral(numeral_to_int(numeral))

with open('euler089_input.txt') as f:
    pe089 = [line.strip() for line in f.readlines()]

def euler89(numerals=pe089):
    """http://projecteuler.net/index.php?section=problems&id=89

    The rules for writing Roman numerals allow for many ways of writing each
    number (see FAQ: Roman Numerals). However, there is always a "best" way of
    writing a particular number.

    For example, the following represent all of the legitimate ways of writing
    the number sixteen:

    IIIIIIIIIIIIIIII
    VIIIIIIIIIII
    VVIIIIII
    XIIIIII
    VVVI
    XVI

    The last example being considered the most efficient, as it uses the least
    number of numerals.

    The 11K text file, roman.txt (right click and 'Save Link/Target As...'),
    contains one thousand numbers written in valid, but not necessarily
    minimal, Roman numerals; that is, they are arranged in descending units and
    obey the subtractive pair rule (see FAQ for the definitive rules for this
    problem).

    Find the number of characters saved by writing each of these in their
    minimal form.

    Note: You can assume that all the Roman numerals in the file contain no
    more than four consecutive identical units.
    """
    return sum(len(rn)-len(minimize_numeral(rn)) for rn in numerals)
