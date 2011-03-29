
ep18 = """\
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

def triangle_index(row, n):
    """In a linearized triangular array, gives the index of the nth element
    of a row."""
    return n + row * (row + 1) / 2

def euler18(triangle_string=ep18):
    """http://projecteuler.net/index.php?section=problems&id=18
    
    Find the maximum sum travelling from the top of the triangle to the base."""
    triangle = [int(x) for x in triangle_string.split()]
    rows = triangle_string.count('\n')
    best = {}
    best[(0,0)] = triangle[0]
    for row in range(1, rows):
        best[(row,0)] = best[(row-1,0)] + triangle[triangle_index(row, 0)]
        best[(row,row)] = best[(row-1,row-1)] + triangle[triangle_index(row, row)]
        for i in range(1, row):
            best[(row,i)] = triangle[triangle_index(row, i)] + \
                    max(best[(row-1,i-1)], best[(row-1,i)])
    return max([best[(rows-1,i)] for i in range(0, rows-1)])

