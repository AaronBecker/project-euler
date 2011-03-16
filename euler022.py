
pe22 = eval('[' + open('euler22_input.txt').readlines()[0] + ']')

def euler22(names=pe22):
    """What is the total of all the name scores in the file of first names?"""
    names.sort()
    name_sum = 0
    for i in range(len(names)):
        name_sum += (i+1) * sum([ord(c) - ord('A') + 1 for c in names[i]])
    print 'The sum of the name scores is %d' % name_sum
    return name_sum
