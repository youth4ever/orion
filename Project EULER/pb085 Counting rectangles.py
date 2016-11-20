#!/usr/bin/python3
# Solved by Bogdan Trif @       Completed on Mon, 31 Oct 2016, 12:44
#The  Euler Project  https://projecteuler.net
'''
Counting rectangles     -       Problem 85
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:
Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
'''
from numpy import prod
from itertools import combinations
import time

def is_prime(n):
    ''' VERY FAST. Does not depend on a pre-generated sieve or on other module !'''
    if n == 1:
        return False
    for i in range(2, int((n**0.5)+1)):
        if not n % i:
            return False
    return True

# print(isprime(100000980001501))

def factors(a):
    '''Outputs a list of the unique prime factors of its input; The Second Fastest Algorithm
    This Function is splitting a number in its factors, and detects also if the number is a prime. '''
    b = 2
    d = []
    f = a
    while f > 1:
        while f % b != 0:
            b = b + 1
        d = d + [b]
        f = f / b
    if len(d) >1:
        return  d
    else: return print(a,' is prime')




def make_rectangles(n) :
    ''' Functions which transform an area into a rectangle

    :param n: is the Area which will be computed. If the number is a prime it just returns [n,1]

    :return: a list with pairs of numbers which represent sides of a rectangle    '''
    lst =[]
    if is_prime(n) == False:
        # print(i, factors(i))
        C = list(combinations(factors(n), 2))
        for k in range(len(C)):
            q = [ n//prod(C[k]),  prod(C[k]) ]
            q = sorted(q)
            if q not in lst : lst.append( q )
        for j in range( len(factors(n))):
            p = ( int(prod(factors(n)[0:j]))  , prod(factors(n)[j::]) )
            p = sorted(p)
            if p not in lst : lst.append( p  )
        return lst
    elif is_prime(n) == True :
        lst = [n , 1]
        return [lst]

print('\nMake Rectangles Function: ',make_rectangles(2772))

def calc_rectangle(a , b):
    '''    Function which calculates the possible number of sub rectangles in an area

    :param a: is the length of the rectangle

    :param b:  the height of the rectangle

    :return:  returns the number of rectangles that can be formed inside    '''
    S = 0
    for i in range(1, a+1):
        for j in range(1, b+1):
            S += (a-i+1) * (b-j+1)
    return S

print('\n',calc_rectangle(36, 77))



print('\n---------------TESTS------------------')
# Must also make combinations for multiple factors cases, like 64, could be: (2,32), (4, 16), (8,8)  rectangles
# or 48 : (2,24), (4, 12), (8, 6), (16, 3)
# 42 : (2 , 21), (3, 14) , (6, 7)
# Now I must make a function which for a given a, b sides calculates the total number of rectangles
#

# Test for the function make_rectangle :
# for i in range(108,110):
#     print('------------------')
#     if is_prime(i) == False:
#         print(i, factors(i))
#         # if  len(factors(i)) > 2 and len(set(factors(i))) == len(factors(i)) :
#         C = list(combinations(factors(i), 2))
#         for k in range(len(C)):
#             print (  (  i//prod(C[k]),  prod(C[k])  ) , '   <-- combinations')
#         # else :
#         for j in range( len(factors(i))):
#             print( ( prod(factors(i)[0:j])  , prod(factors(i)[j::])  ) )

# a , b = 5, 2
# S = 0
# for i in range(1, a+1):
#     for j in range(1, b+1):
#         S += (a-i+1) * (b-j+1)
#         print(i,j,'    ', (a-i+1) * (b-j+1),'        one')
# print(S)
#
# print(factors(100))
# print(set(factors(100)))
# C = list(combinations(factors(100), 2))
# print(C)


print('\n---------------------------- MY FIRST SOLUTION, UNNECESSARY COMPLICATED  -----------------------------')
t1  = time.time()

# epsilon = 10000
# for i in range(2000, 10000):
#     for j in range(len(make_rectangles(i))) :
#         a = make_rectangles(i)[j][0]
#         b = make_rectangles(i)[j][1]
#         # print(i, calc_rectangle(a,b))
#         nr = calc_rectangle(a,b)
#         if abs(2*10**6 - nr) < epsilon :
#             epsilon = abs(2*10**6 - nr)
#             print('Rectangles: ',nr,'   ; Sides : ', a, b, ' ;  Area:', a*b)
#     if epsilon < 10:
#         break

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')

print('\n---------------------------- MY SECOND SOLUTION,   -----------------------------')
t1  = time.time()

def rect(x,y):          # Tanasa Ioan 's function, Much much faster than mine
    return x*y*(x+1)*(y+1)//4

def calc_rectangle(a , b):
    S = 0
    for i in range(1, a+1):
        for j in range(1, b+1):
            S += (a-i+1) * (b-j+1)
    return S

def compute_rectangles() :
    epsilon = 10000
    for a in range(25, 100):
        for b in range(25, 100) :
            nr = rect(a,b)
            if abs(2e6 - nr) < epsilon :
                epsilon = abs(2e6 - nr)
            if epsilon < 10:
                return print('Rectangles nr: ',nr,'   ; Sides : ', a, b, ' ;  Area:', a*b)

compute_rectangles()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')


print('\n============  OTHER SOLUTIONS FROM EULER FORUM =============')
print('\n----------------SOLUTION 1 ,NICE SOLUTION  ,TanasaIoan, Romania-------------------------')
t1  = time.time()
# I figured out the formula of rectangles for a grid(x,y)=x*(x+1)*y*(y+1)/4 and here is my code in python:
#
# def rect(x,y):
#     return x*y*(x+1)*(y+1)//4
#
# result=0
# L=0
# def check(x,y):
#     global result
#     global L
#     if abs(2000000-rect(x,y))<abs(2000000-result):
#         result=rect(x,y)
#         L=x*y
#
# for a in range(3000):
#     for b in range(a,3000):
#         check(a,b)
# print(result)
# print(L)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')                # Completed in : 7914.4526 ms


print('\n----------------SOLUTION 2 , juancroldan  , Spain-------------------------')
t1  = time.time()
# Quite easy in Python using sum properties.

tot = lambda x: sum(range(0,x+1))
n = lambda w,h: tot(w)*tot(h)

area = None
distance = float("inf")

for i in range(0,100):
	for j in range(i,100):
		dist = abs(n(i,j)-2000000)
		if dist<distance:
			distance = dist
			area = i*j

print(area,distance)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')

print('\n----------------SOLUTION 3 , Basim, England-------------------------')
t1  = time.time()
# Simple python solution as mentioned by others using the triangle number fact:
triangle = lambda x: (x*(x+1)) / 2
target = 2000000

bestFound = 0
bestI = 0
bestJ = 0

for i in range(1, 100):
	for j in range(1, 100):
		newVal = triangle(i)*triangle(j)
		if abs(target - newVal) < abs(target - bestFound):
			bestFound = newVal
			bestI = i
			bestJ = j

print("Best:", bestFound, "at", str(bestI) + ":" + str(bestJ))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')

print('\n----------------SOLUTION 4 , NICE, List Comprehension, mfm24, -------------------------')
t1  = time.time()
# First I noticed that, for an X,Y rectangle,  the number of sub-rectangles of size (x,y) is equal to the area of the (1+X-x, 1+Y-y) rectangle.
# Then it was just a case of summing the area of all rectangle from (1 to X, 1 to Y).
# To find the upper bound on the rectangle width, just need to realise that when Y is 1,
# X will be largest and the max value of X is therefore < sqrt(4e6) => X,Y < 2000.
# Then can brute force with generator in python (noting that the max value of any side of the rectangle is 2000):

closeness = lambda x: abs(x[0] - 2e6)
print(min((((m*(m+1)*n*(n+1)/4),m*n) for m in range(2000) for n in range(2000)), key=closeness))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')

print('\n----------------SOLUTION 5 ,-------------------------')
t1  = time.time()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')


