
def euler205():
    """http://projecteuler.net/index.php?section=problems&id=205

    Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2,
    3, 4.  Colin has six six-sided (cubic) dice, each with faces numbered 1, 2,
    3, 4, 5, 6.

    Peter and Colin roll their dice and compare totals: the highest total wins.
    The result is a draw if the totals are equal.

    What is the probability that Pyramidal Pete beats Cubic Colin? Give your
    answer rounded to seven decimal places in the form 0.abcdefg.
    """

    peter, colin = [0] * 37, [0] * 37
    for d1 in range(1, 5):
        for d2 in range(1, 5):
            for d3 in range(1, 5):
                for d5 in range(1, 5):
                    for d5 in range(1, 5):
                        for d6 in range(1, 5):
                            for d7 in range(1, 5):
                                for d8 in range(1, 5):
                                    for d9 in range(1, 5):
                                        peter[d1+d2+d3+d5+d5+d6+d7+d8+d9] += 1
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            for d3 in range(1, 7):
                for d4 in range(1, 7):
                    for d5 in range(1, 7):
                        for d6 in range(1, 7):
                            colin[d1+d2+d3+d4+d5+d6] += 1
    odds = 0
    for c in range(6, 37):
        odds += float(colin[c]) / sum(colin) * float(sum(peter[c+1:])) / sum(peter)
    print colin
    print peter
    return '%0.7f' % odds
