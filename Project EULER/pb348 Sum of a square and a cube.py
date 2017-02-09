#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @       Completed on Sun, 5 Feb 2017, 13:06
#The  Euler Project  https://projecteuler.net
'''
Sum of a square and a cube      -       Problem 348

Many numbers can be expressed as the sum of a square and a cube. Some of them in more than one way.

Consider the palindromic numbers that can be expressed as the sum of a square and a cube,
both greater than 1, in exactly 4 different ways.

For example, 5229225 is a palindromic number and it can be expressed in exactly 4 different ways:

22852 + 203
22232 + 663
18102 + 1253
11972 + 1563

Find the sum of the five smallest such palindromic numbers.

'''
import time, gmpy2
import  eulerlib

def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]

print( eulerlib.is_palindrome( 5229225) )


def next_palindrome(n):
    X = len(n)>>1
    Y = X+(len(n)&1)
    first = n[X-1::-1]
    second = n[Y:]
    Z = n[:Y]
    assert Y >= X        #, "by construction"
    assert len(second) >= len(first)        #, "by construction"
    if len(first) == len(second) and first > second:
        assert int(first) > int(second)         #, "because ASCII"
        yield Z+first
    # if int(first) > int(second):
    #     return Z+first
    else:
        bar = str(int(Z)+1)
        yield bar+bar[:X][::-1]







print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force(up_lim=2*10**4):
    P = {}

    for i in range(10**3, up_lim):
        if i% 10**3 == 0 : print(str(i)+'.   ')
        for j in range(2,  i//7 ):
            n = i**2 + j**3
            if eulerlib.is_palindrome(n) :
                # print(n,'    ', i, j, '        ', i**2, '       ', j**3)
                if n not in P :
                    P[n]=[(i , j)]
                else : P[n].append((i,j) )

    print('\n',len(P))
    S =  {  k: v for k,v in P.items() if len(v) == 4 }
    print('\n',len(S), '\n' ,S )

    return print('\nAnswer : \t', sum([i for i in S.keys()])  )

# brute_force()

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')

#                                        5229225 [(2285, 20), (2223, 66), (1810, 125), (1197, 156)]
#                                        37088073 [(6083, 44), (4323, 264), (3417, 294), (3300, 297)]
#                                        56200265 [(7491, 44), (7249, 154), (7069, 184), (5832, 281)]
#                                        108909801 [(10401, 90), (6202, 413), (5901, 420), (3583, 458)]
#                                        796767697 [(28215, 88), (27827, 282), (24904, 561), (21705, 688)]

print('\n================  My FIRST SOLUTION, 1 min  ===============\n')
t1  = time.time()

def palindromes_sums_of_square_and_cube() :
    P = next_palindrome('5229220')
    L, fives = {}, 0
    while 1 :
        p = next(P)
        if int(p[0]) in [1,3,5,7] :        # Check only odd palindromes
            cnt, tmp = 0, []
            for i in range(20, 700 ) :
                test_nr = int(p) - i**3
                if gmpy2.is_square(test_nr) :
                    cnt+=1
                    tmp.append( ( int(test_nr**(1/2))  , i) )
                if cnt == 4 :
                    L[int(p)] = (tmp)
                    print( int(p), tmp )
                    fives+=1
                    break
            if fives == 5 :
                return print( '\nAnswer : \t', sum([i for i in L.keys()]) )

        P = next_palindrome(p)

palindromes_sums_of_square_and_cube()                   # Answer : 	 1004195061

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, 35 sec  --------------------------')
t1  = time.time()

# ==== Sat, 26 Sep 2015, 12:34, max.doom , Germany
# Brute force. ~47sec (~15sec on my server). Nothing new... the palindromic() test is nice.


def solution_1():
    squares = {}
    cubes = {}
    palindromes = {}

    def init(nsquares, ncubes):
        for i in range(2,nsquares):
            squares[i] = i*i
        for i in range(2,ncubes):
            cubes[i] = i*i*i

    def palindromic(n):
        s = str(n)
        return s==s[::-1]

    init(30000, 700)

    for i in squares:
        for j in cubes:
            sum = squares[i]+cubes[j]
            if palindromic( sum ):
                if not sum in palindromes:
                    palindromes[sum] = []
                palindromes[sum].append({'s':i, 'c': j})

    sum = 0
    for match in palindromes:
        if len( palindromes[match] ) == 4:
            sum += match
            print (match, palindromes[match], '\n')

    return print ("sum:", sum)

# solution_1()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, FAST & VERY ELEGANT, 10 sec  --------------------------')
t1  = time.time()


from itertools import *
import collections, operator

pals = set(range(2,10))
for m in range(1,10**4):
	fr = str(m)
	rev = fr[::-1]
	pals.add(int(fr + rev))
	for n in range(10):
		pals.add( int(fr + str(n) + rev) )

limit = lambda k: k < 10**9

squares = list( takewhile(limit, accumulate(count(1, 2))) )
cubes = list(takewhile(limit, starmap(operator.mul,enumerate(squares,1))) )

palsums = collections.Counter( psum for psum in starmap(operator.add,product(squares,cubes)) if psum in pals )
soln = sorted(pal for pal,ct in palsums.items() if ct == 4)

print( sum(soln[:5]) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  10 sec --------------------------')
t1  = time.time()

# ==== Sun, 11 Jan 2015, 02:43, raulbc777, Paraguay
# BRUTEFORCE.
# First, I create a set of all the palindromes for, let's say, ten digits and this number of digits may be ajustable,
# more digits if we have less than five solutions or less if we have them and we want to reduce the future runtime for unnecesary checks.
# I used a very fast code to generate all the palindromes in a set.
# Then I create two lists, sqList and cubicList, and with two nested loops to generate all the possible sums.
# The idea is to create a dictionary for all the sums that gives a palindrome number as a result.
# The dictionary would have a list of tuple as its values.
# If the sum is not  in the set of palindromes jumps to a next sum,
# if the result is in the palindrome set (True) but the cubic + square is not the dictionary,
# it sets a new key with this sum. If the the key is in the dictionary adding another pair,
# it appends a new tuple = (square, cubic) in the list as a value.
#
# Once this dictionary is created we select all the list that have a length equal to four.
#
# I set the limit of 28500, after a number of trials for having the minimum length of sqList and
# cubicList that will give the smallest first five palindromes with this property.
# The code bellow gives the result in 9 secs:

def solution_3():

    import itertools
    import string
    from itertools import count

    def getPalindrome():
        """
            Generator for palindromes.
            Generates palindromes, starting with 0.
            A palindrome is a number which reads the same in both directions.
        """
        yield 0
        for digits in count(1):
            first = 10 ** ((digits - 1) // 2)
            for s in map(str, range(first, 10 * first)):
                yield int(s + s[-(digits % 2)-1::-1])

    def allPalindromes(minP, maxP):
        """Get a sorted list of all palindromes in intervall [minP, maxP]."""
        palindromGenerator = getPalindrome()
        palindromeList = []
        for palindrome in palindromGenerator:
            if palindrome > maxP:
                break
            if palindrome < minP:
                continue
            palindromeList.append(palindrome)
        return palindromeList



    def sq(n):
        return n**2

    def cubic(n):
        return n**3

    start = time.time()
    minP, maxP = 5000000, 1000000000
    palindList = allPalindromes(minP, maxP)

    palindSet = set(palindList)

    limit = 28500
    cubicLimit = int(limit**(2/float(3)))
    sqList = []
    cubicList = []
    for i in range(1, limit):
        sqList.append(sq(i))
        if i < cubicLimit:
            cubicList.append(cubic(i))

    solDict = {}
    for cubic in cubicList:
        for sq in sqList:
            if cubic + sq not in palindSet:
                continue
            if cubic + sq not in solDict:
                solDict[sq + cubic] = [(sq, cubic)]
            else:
                solDict[sq + cubic].append((sq, cubic))

    print ("Number    " + "                Squares and Cubes")
    print()
    sumRes = 0
    count = 0
    for k, v in solDict.items():
        if len(v) == 4:
            print (k, v)
            sumRes += k
            count += 1
        if count == 5: break

    return print ("\nThe sum of these kind of numbers is :", sumRes )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  22 sec --------------------------')
t1  = time.time()

# ==== Mon, 1 Aug 2016, 15:58, Knight-erraunt, Poland
# I have a pretty long solution in Python which seems to be rather fast compared to other Python solutions on this discussion.
# It uses itertools and some helpers with doctest for some simple tests,
# I am trying to learn a bit about writing nice clean code.
# It struck me how short some of the Python solutions on the beginning of this thread are,
# nevertheless I am rather satisfied with mine - no hand calculated bounds, code is not as ugly as usually,
# and last but not least - got this one on the first attempt which recently does not happen that often.

def solution_4() :
    import itertools

    def take(n, iterable):
        "Return first n items of the iterable as a list"
        return list(itertools.islice(iterable, n))


    def nth(iterable, n, default=None):
        "Returns the nth item or a default value"
        return next(itertools.islice(iterable, n, None), default)


    def consume(iterator, n):
        "Advance the iterator n-steps ahead. If n is none, consume entirely."
        next(itertools.islice(iterator, n, n), None)


    def palindrome_gen():
        """
        Generates palindromicall numbers from the
        smallest by value.

        >>> take(12, palindrome_gen())
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22]

        >>> nth(palindrome_gen(), 19)
        101

        >>> nth(palindrome_gen(), 20)
        111

        >>> it = palindrome_gen()
        >>> consume(it, 19)
        >>> take(11, it)
        [101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202]

        >>> it = palindrome_gen()
        >>> consume(it, 10 + 9 + 10 * 9)
        >>> take(14, it)
        [1001, 1111, 1221, 1331, 1441, 1551, 1661, 1771, 1881, 1991, 2002, \
    2112, 2222, 2332]

        """
        odd_half = 0
        odd_val = int(str(odd_half) + str(odd_half)[::-1][1:])
        even_half = 1
        even_val = int(str(even_half) + str(even_half)[::-1])
        while True:
            if odd_val < even_val:
                odd_half += 1
                yield odd_val
                odd_val = int(str(odd_half) + str(odd_half)[::-1][1:])
            else:
                even_half += 1
                yield even_val
                even_val = int(str(even_half) + str(even_half)[::-1])

    if __name__ == '__main__':
        squares, cubes = set(), []

        decompositions = {
        }

        nsquares_base, ncube_base = 1, 1
        for pal in palindrome_gen():
            while nsquares_base ** 2 <= pal:
                squares.add(nsquares_base ** 2)
                nsquares_base += 1
            while ncube_base ** 3 <= pal:
                cubes.append(ncube_base ** 3)
                ncube_base += 1
            decomposition = []
            for cube in cubes:
                if pal - cube in squares:
                    decomposition += [(pal - cube, cube)]

            if len(decomposition) == 4:
                decompositions[pal] = decomposition

            if len(decompositions) >= 5:
                break
        print(decompositions)
        return print(sum(decompositions.keys()))

# solution_4()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
