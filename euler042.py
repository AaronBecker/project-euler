pe42 = eval('[' + open('euler042_input.txt').readlines()[0] + ']')

def word_score(s):
    return sum(ord(c) - ord('A') + 1 for c in list(s))

def euler42(input=pe42):
    """http://projecteuler.net/problem=42

    How many triangle words does the list of common English words contain?"""
    triangle_list = [int(0.5 * x * (x + 1)) for x in range(1, 51)]
    return sum(1 for word in input if word_score(word) in triangle_list)
