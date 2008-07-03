#!/usr/bin/env python

import sys
import optparse
import time

def collatz(upper_bound):
    """Generate number of terms in Collatz sequence for n (n/2 or 3n+1)"""
    known_terms = []
    for n in xrange(1, upper_bound):
        terms = 1
        while n != 1:
            if len(known_terms) >= n:
                terms = known_terms[n-1] + terms - 1
                break
            if n % 2 == 0:
                n /= 2
            else:
                n = 3*n + 1
            terms += 1
        known_terms.append(terms)
        yield terms

def count_factors(x):
    """Count the factors (not necessarily prime) of x"""
    factors = 2 # 1 and x
    for i in xrange(2, x**0.5 + 1):
        if x % i == 0:
            factors += 2
    return factors

def is_palindrome(candidate):
    """Determine whether or not a number (or any string) is palindromic"""
    digits = [digit for digit in str(candidate)]
    return (digits == digits[::-1])

def factorial(x):
    """Compute x!"""
    fac = 1
    for i in range(1, x+1):
        fac *= i
    return fac

# simple number theory functions modified from http://www.4dsolutions.net
def gcd(a,b):
   """Return greatest common divisor using Euclid's Algorithm."""
   while b:      
	a, b = b, a % b
   return a

def lcm(a,b):
   """Return lowest common multiple."""
   return (a*b)/gcd(a,b)

def GCD(terms):
   """Return gcd of a list of numbers."""
   return reduce(lambda a,b: gcd(a,b), terms)

def LCM(terms):
   """Return lcm of a list of numbers."""   
   return reduce(lambda a,b: lcm(a,b), terms)

# quick prime sieve from literateprograms.org
def sieve_of_eratosthenes(n):
    """Generate a list of the prime numbers [2, 3, ... m] where
    m is the largest prime <= n."""
    n = n + 1
    sieve = range(n)
    sieve[:2] = [0, 0]
    for i in xrange(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in xrange(i ** 2, n, i):
                sieve[j] = 0
    # Filter out the composites, which have been replaced by 0's
    return [p for p in sieve if p]

def factor(number, factors=[1]):
    sqrt = int(number ** 0.5) + 1
    primes = sieve_of_eratosthenes(number)
    index = 0 
    while primes[index] <= sqrt:
        prime = primes[index]
        while number % prime == 0:
            number /= prime
            factors.append(prime)
        index += 1
    return factors

def project_euler_1(upper_bound=1000):
    """ Add all the natural numbers below 1000 that are multiples of 3 or 5"""
    fives = set(range(0, upper_bound, 5))
    threes = set(range(0, upper_bound, 3))
    union_sum = sum(fives | threes)
    print "The sum of the multiples of 3 and 5 under %d is %d\n" %\
        (upper_bound, union_sum)
    return union_sum

def project_euler_2(upper_bound=1000000):
    """Find the sum of all the even-valued terms in the Fibonacci sequence which do not 
    exceed one million."""
    f1, f2 = 2, 1
    even_sum = 0
    while f1 < upper_bound:
        if f1 % 2 == 0:
            even_sum = even_sum + f1
        f1, f2 = f1+f2, f1
    print "The sum of even fibonacci numbers less than %d is %d\n" %\
            (upper_bound, even_sum)
    return even_sum

def project_euler_3(target=317584931803):
    """What is the largest prime factor of the number 317584931803?"""
    orig_target = target
    sqrt_target = int(target ** 0.5) + 1
    i = 1
    while i < sqrt_target:
        if target % i == 0:
            factor = i
            target = target / i
        i += 1
    print "The largest prime factor of %d is %d\n" % (orig_target, factor)
    return factor

def project_euler_4(upper_bound=1000):
    """Find the largest palindrome made from the product of two 3-digit numbers."""
    max_pal = 0
    for x in xrange(0,1000):
        for y in xrange(0,1000):
            if x*y > max_pal and is_palindrome(x*y):
                max_pal = x*y
    print "The largest palindrome product of numbers under %d is %d\n" %\
            (upper_bound, max_pal)
    return max_pal

def project_euler_5(upper_bound=20):
    """What is the smallest number that is evenly divisible by all of the numbers
    from 1 to 20?"""
    result = LCM(range(1, upper_bound+1))
    print "The smallest number evenly divisible by all numbers from 1 to %d is %d\n" %\
            (upper_bound, result)
    return result

def project_euler_6(upper_bound=100):
    """What is the difference between the sum of the squares 
    and the square of the sums?"""
    sum_sq = sum([x * x for x in range(1, upper_bound+1)])
    sq_sum = sum(range(1, upper_bound+1)) ** 2
    result = sq_sum - sum_sq
    print "The difference between the sum of squares and the squared sum from 1 to %d"\
            " is %d" % (upper_bound, result)
    return result

def project_euler_7(n=10001):
    """Find the 100001st prime."""
    # Find all primes less than some initial guess. If that doesn't provide enough
    # primes, try again with a bigger guess
    guess = 1000000
    primes = []
    while len(primes) < n:
        primes = sieve_of_eratosthenes(guess)
        guess *= 2
    print "The %dth prime is %d\n" % (n, primes[n-1])
    return primes[n-1]

ep8 = """\
73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450\
"""
def project_euler_8(digit_string=ep8):
    """Find the greatest product of five consecutive digits in the given number."""
    max_product = 1
    for i in xrange(len(digit_string)-5):
        product = int(digit_string[i]) *\
                int(digit_string[i+1]) *\
                int(digit_string[i+2]) *\
                int(digit_string[i+3]) *\
                int(digit_string[i+4])
        if max_product < product:
            max_product = product
    print "The greatest product of 5 consecutive digits is %d\n" % max_product
    return max_product

def project_euler_9(target=1000):
    """Find the product of the Pythagorean triplet where a + b + c = 1000."""
    for x in xrange(1, target):
        for y in xrange(1, target):
            if x**2 + y**2 - (target - x - y)**2 == 0:
                z = target - x - y
                print "%d^2 + %d^2 = %d^2" % (x, y, z)
                print "%d + %d + %d = %d" % (x, y, z, target)
                print "abc = %d" % (x * y * z)
                return x * y * z
    print "Triple not found.\n"
    return 0

def project_euler_10(target=1000000):
    prime_sum = sum(sieve_of_eratosthenes(target))
    print "The sum of all primes less than %d is %d." % (target, prime_sum)
    return prime_sum


ep11 = """\
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 \
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 \
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 \
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 \
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 \
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 \
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 \
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 \
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 \
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 \
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 \
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 \
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 \
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 \
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 \
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 \
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 \
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 \
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 \
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48\
"""
def project_euler_11(grid_string=ep11, xdim=20, ydim=20):
    """What is the greatest product of four numbers in any direction in
    the grid (up, down, left, right, diagonal)?"""
    grid = [int(x) for x in grid_string.split(" ")]

    # define scan functions for looking at products
    def right(idx):
        if xdim - idx < 4:
            return 0
        else:
            return grid[idx] *\
                    grid[idx+1] *\
                    grid[idx+2] *\
                    grid[idx+3]
    def down(idx):
        if ydim - idx / xdim < 4:
            return 0
        else:
            return grid[idx] *\
                    grid[idx+1*xdim] *\
                    grid[idx+2*xdim] *\
                    grid[idx+3*xdim]
    def ldiag(idx):
        if idx < 4 or ydim - idx / xdim < 4:
            return 0
        else:
            return grid[idx] *\
                    (grid[idx+1*xdim - 1]) *\
                    (grid[idx+2*xdim - 2]) *\
                    (grid[idx+3*xdim - 3])
    def rdiag(idx):
        if xdim - idx < 4 or ydim - idx / xdim < 4:
            return 0
        else:
            return grid[idx] *\
                    (grid[idx+1*xdim + 1]) *\
                    (grid[idx+2*xdim + 2]) *\
                    (grid[idx+3*xdim + 3])

    max_product = 0
    for i in xrange(len(grid)):
        product = right(i)
        if product > max_product:
            max_product = product
        product = down(i)
        if product > max_product:
            max_product = product               
        product = ldiag(i)
        if product > max_product:
            max_product = product               
        product = rdiag(i)
        if product > max_product:
            max_product = product
    print "The maximum product is %d" % max_product
    return max_product

def project_euler_12(target=500):
    """What is the first triangular number to have over 
    five hundred divisors?"""
    n = target
    last_factors = count_factors(n-1)
    while 1:
        factors = count_factors(n)
        if factors * last_factors - max(factors, last_factors) >= target:
            print "Trying %d * %d / 2" % (n-1, n)
            f = count_factors(n*(n-1)/2) 
            if f <= target:
                print "only %d factors, continuing..." % f
                n += 1
                continue
            print "The first triangular number with "\
                    "at least %d factors is %d" % (target, n * (n - 1) / 2)
            print n
            return n * (n - 1) / 2
        last_factors = factors
        n += 1
        
pe13 = """\
37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690
"""

def project_euler_13(number_string=pe13):
    """Find the first ten digits of the sum of one-hundred 
    50-digit numbers."""
    numbers = [int(num) for num in number_string.split()]
    sum_str_prefix = str(sum(numbers))[0:10]
    print "The first ten digits of the sum are %s." % sum_str_prefix
    return

def project_euler_14(upper_bound=1000000):
    """Which starting number under one million produces the longest 
    Collatz chain?"""
    cseq = zip(collatz(upper_bound), range(1, upper_bound))
    (max_terms, max_seed) =  max(cseq)
    print "The longest Collatz chain under %d is %d, produced by %d." %\
            (upper_bound, max_terms, max_seed)
    return max_seed

def project_euler_14(grid_size=20):
    """How many routes are there through a 20x20 grid?"""
    grid = [[0] * (grid_size+1)] * (grid_size+1)
    for i in range(grid_size+1):
        grid[i][0] = 1
        grid[0][i] = 1
    for i in range(1, grid_size+1):
        for j in range(1, grid_size+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    routes = grid[grid_size][grid_size]
    print "There are %d routes through a %dx%d grid." % (routes, grid_size,
            grid_size)
    return routes

def project_euler_15(x=2**1000):
    """What is the sum of the digits of the number 2**1000?"""
    digit_sum = sum([int(d) for d in str(x)])
    print "The sum of the digits of is %d" % digit_sum
    return digit_sum

def project_euler_16(upper_bound=1000)
    digits = {
            1: 3,
            2: 3,
            3: 5,
            4: 4,
            5: 4,
            6: 3,
            7: 5,
            8: 5,
            9: 4 }
    unique_numbers = { 
            10: 3,
            11: 6,
            12: 6,
            13: 8,
            15: 7,
            1000: 11}
    tens_modifiers = {
            20: 6,
            30: 6,
            40: 6,
            50: 5,
            60: 5,
            70: 7,
            80: 6,
            90: 6 }

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    parser = optparse.OptionParser(
        formatter=optparse.TitledHelpFormatter(width=78),
        add_help_option=None)

    # define options here:
    #parser.add_option(
    #    '-h', '--help', action='help',
    #    help='Show this help message and exit.')

    settings, args = parser.parse_args(argv)

    # check number of arguments, verify values, etc.:
    if args:
        try:
            # find the function named project_euler_# and time its execution
            # if it does not exist, exit gracefully
            function_name = "project_euler_" + str(args[0])
            invoke_function = globals()[function_name]
            if (callable(invoke_function)):
                start = time.time()
                globals()["project_euler_" + str(args[0])]()
                end = time.time()
                print '%s took %0.3f ms' % (function_name, (end-start)*1000.0)
                return 0
            else:
                print 'Specified function does not exist'
                return 1
        except KeyError:
            print 'Specified function does not exist'
            return 1

    print 'Specify the problem number to solve'
    return 1

if __name__ == "__main__":
    status = main()
    sys.exit(status)
