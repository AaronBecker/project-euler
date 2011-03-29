
def decrypt(text, key):
    dlist = []
    for i in xrange(len(text)):
        dlist.append(chr(ord(text[i]) ^ ord(key[i % 3])))
        if not 32 <= ord(dlist[-1]) <= ord('z'): return -1
    dtext = ''.join(dlist)
    if dtext.find(' the ') != -1:
        return sum(ord(d) for d in dtext)
    else:
        return -1


pe59 = eval('"".join(map(chr, [' +
        open('euler059_input.txt').readlines()[0].strip() + ']))')
def euler59(text=pe59):
    """http://projecteuler.net/index.php?section=problems&id=59

    Using a brute force attack, can you decrypt the cipher using XOR encryption?
    """
    # note: key is known to be 3 letters, lower case
    for x in xrange(ord('a'), ord('z')+1):
        for y in xrange(ord('a'), ord('z')+1):
            for z in xrange(ord('a'), ord('z')+1):
                val = decrypt(text, chr(x)+chr(y)+chr(z))
                if val != -1: return val
