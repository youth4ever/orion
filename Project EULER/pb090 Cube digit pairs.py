#!/usr/bin/python
# Solved by Bogdan Trif @  lCompleted on Fri, 28 Oct 2016, 09:02
#The  Euler Project  https://projecteuler.net
'''
Cube digit pairs        -       Problem 90
Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube.
By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:
In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred:
01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.
However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7}
allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.
{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent
the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.
How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
'''
from itertools import combinations
import time


#digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    # I lost 3 weeks because
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 6]
worthy = []

print('----------------------MY FIRST SOLUTION, the SLOWEST, Must Re-DO it -----------------------------')
t1  = time.time()


C = list(combinations(digits,6))
# for j in range(len(C)):     print(str(j+1)+'.   ',C[j])
#print(len(C), C)

A = (0, 5, 6, 7, 8, 9)
B = (1, 2, 3, 4, 6, 7)

# squares = ['01' , '04' , '06' , '09', '16' , '19' ,'25' , '36' , '39' , '46' , '49' , '18'  ]
squares1 = ['01' , '04' , '06' , '16' ,'25' , '36' , '46' , '18' ]

counter = 0
superC = 0
for m in range(len(C)):                   #C[125:127]:
    for n in range(m):                      # C[130:132]:
        counter +=1
        Cm = "".join(str(i) for i in list(C[m]))
        Cn = "".join(str(i) for i in list(C[n]))
        #print(str(counter)+".   ", C[n], C[m] , "   ",Cn , Cm   )
        iter = 0
        sqr=[]
        cnt1 = 0
        for i in C[m]:
            for j in C[n]:
                cnt1 +=1
                cub = ''.join(sorted(str(i)+str(j)))
                #print (str(counter)+'.  ',str(cnt1)+'.   ' , i ,j ,  cub )
                if ( cub in squares1  ):     # ['01' , '04' , '06' , '09', '16' , '19' ,'25' , '36' , '39' , '46' , '49' , '18'  ]
                    sqr.append(cub)
                    iter += 1
                    #print(str(counter)+'.  ',str(cnt1)+'.   ', cub,'   ' ,sqr)
        ze = set(sqr)
        pairs=[]
        if  ( ( ('01' in sqr)  and ('04' in sqr) and (('06' or '09') in sqr ) and (('16' or '19') in sqr ) and ('25' in sqr) and \
              (('36' or '39') in sqr )  and ('18' in sqr )   and   (('46' or '49') in sqr ))  )  :
                    superC += 1
                    pairs=[Cn , Cm]
                    worthy.append(pairs)
                    #print(str(superC)+'.      '  ,'      ',len(sqr),'   ' ,sqr ,'             ' ,str(Cn), str(Cm)) #,counter)    len(ze) ,ze


print('\nworthy Arrangements :  ', superC,'\n')         # Answer 1217
# print(worthy)


#for i in range(len(worthy)):
#    if   worthy[i][0] == worthy[i][1] :
#        print(worthy[i])

# print('\n----------WORTHY , the DUPLICATES ---------------')
# cnt = 0
# for x in range(len(worthy)):
#     for y in range(len(worthy)):
#         if worthy[y] ==  worthy[x][::-1]  :
#             cnt += 1
#             #selected.remove(worthy[y])
#             print(str(cnt)+".  ", worthy[y], worthy[x] )

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1)*1000,6), 'ms\n')          #  Completed in  : 3352.191925 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1 , VERY ELEGANT & FAST , http://blog.dreamshire.com/project-euler-90-solution/ --------------------------')

t1  = time.time()


from itertools import combinations

squares = [(0,1), (0,4), (0,6), (1,6), (2,5), (3,6), (4,6), (8,1)]
cube = list(combinations([0,1,2,3,4,5,6,7,8,6], 6))

def valid(c1, c2):
    return all(x in c1 and y in c2 or x in c2 and y in c1 for x, y in squares)

print ("Project Euler 90 Solution =", sum(1 for i,c1 in enumerate(cube)
                                         for c2 in cube[:i]
                                             if valid(c1, c2)))

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1)*1000,6), 'ms\n')

print('\n--------------------------SOLUTION 2 , nopria, Italy  --------------------------')

t1  = time.time()

from itertools import combinations as c

print(sum(1 for i,j in c(c('0123456786',6),2) if all((s[0] in i and s[1] in j) or (s[1] in i and s[0] in j) for s in ('01','04','06','16','25','36','64','81'))))

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1)*1000,6), 'ms\n')

# which in turn derives from the equivalent but more readable version:

t1  = time.time()

import itertools

squares = ('01','04','06','16','25','36','64','81') # if 64 can be displayed also 49 can

c = tuple(itertools.combinations('0123456786',6))

q = 0
for i in range(len(c)):
    for j in range(i,len(c)):
        if all((s[0] in c[i] and s[1] in c[j]) or (s[1] in c[i] and s[0] in c[j]) for s in squares):
            q += 1

print(str(q))


t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1)*1000,6), 'ms\n')

print('\n--------------------------SOLUTION 3 , the FASTEST  philiplu, USA --------------------------')
# Weird that this is marked as difficulty 40%.  It felt more like a 10%, maybe 15%, one.
# Not a particularly pretty solution, with brute force and one giant boolean test, but it worked in 10 msec and went together very easily.

t1  = time.time()

from itertools import combinations
import sys

def p90():
    combos = [''.join(x) for x in combinations('0123456789', 6)]
    combos_no_9 = [x.replace('9','6') for x in combos]
    combos_bools = [[(ch in combo) for ch in '0123456789'] for combo in combos_no_9]
    count = 0
    for i, c1 in enumerate(combos_bools):
        for c2 in combos_bools[i:]:
            if ((c1[0] and c2[1]) or (c2[0] and c1[1])) and \
               ((c1[0] and c2[4]) or (c2[0] and c1[4])) and \
               ((c1[0] and c2[6]) or (c2[0] and c1[6])) and \
               ((c1[1] and c2[6]) or (c2[1] and c1[6])) and \
               ((c1[2] and c2[5]) or (c2[2] and c1[5])) and \
               ((c1[3] and c2[6]) or (c2[3] and c1[6])) and \
               ((c1[4] and c2[6]) or (c2[4] and c1[6])) and \
               ((c1[6] and c2[4]) or (c2[6] and c1[4])) and \
               ((c1[8] and c2[1]) or (c2[8] and c1[1])):
                    count += 1
    return count

print(p90())

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1)*1000,6), 'ms\n')

print('\n--------------------------SOLUTION 4 ,   --------------------------')
t1  = time.time()


import itertools

N=[i for i in itertools.combinations(range(10), 6)]

must={1,4,9,16,25,36,49,64,81}
count=0
for i in range(len(N)):
    for j in range(i,len(N)):

        d1=set(N[i])
        d2=set(N[j])
        if 6 in d1: d1.add(9)
        if 6 in d2: d2.add(9)
        if 9 in d1: d1.add(6)
        if 9 in d2: d2.add(6)

        s=set()
        for x in d1:
            for y in d2:
               s.add(10*x+y)
               s.add(10*y+x)
        s.intersection_update(must)

        if len(s)!=9: continue
        count+=1

print('ans=',count)


t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1)*1000,6), 'ms\n')


print('\n--------------------------SOLUTION 5 ,  iamcow   --------------------------')
t1  = time.time()

import math
import itertools

nums = ['0','1','2','3','4','5','6','7','8','9']
cu = []
count = 0

for i in itertools.combinations(nums,6):
        cu.append(i)
pairs = []
for ii in range(len(cu)):
    for jj in range(ii+1,len(cu)):
        i = cu[ii]
        j = cu[jj]
        if (('0' in i and '1' in j) or ('0' in j and '1' in i))\
            and (('0' in i and '4' in j) or ('0' in j and '4' in i))\
            and ((('0' in i and '9' in j) or ('0' in j and '9' in i))\
                 or (('0' in i and '6' in j) or ('0' in j and '6' in i)))\
            and ((('1' in i and '6' in j) or ('1' in j and '6' in i))\
                 or (('1' in i and '9' in j) or ('1' in j and '9' in i)))\
            and (('2' in i and '5' in j) or ('2' in j and '5' in i))\
            and ((('3' in i and '6' in j) or ('3' in j and '6' in i))\
                 or (('3' in i and '9' in j) or ('3' in j and '9' in i)))\
            and ((('4' in i and '9' in j) or ('4' in j and '9' in i))\
                 or (('4' in i and '6' in j) or ('4' in j and '6' in i)))\
            and (('8' in i and '1' in j) or ('8' in j and '1' in i)) and i != j:
            count += 1

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1)*1000,6), 'ms\n')

print('\n--------------------------SOLUTION 6 , Nan-Do, Spain   --------------------------')
t1  = time.time()
# I had some problems understanding the wording of the problem.
# Before solving it I was not sure which was the right ordering. I made a couple of programs to solve all the orderings I understood were viable.

from itertools import combinations

squares = [(0, 1), (0, 4), (0, 9),   (1, 6),  (2, 5),  (3, 6),  (4, 9),  (6, 4),  (8, 1)]


def check_value_dice(value, dice):
    if value == 6 or value == 9:
        return (6 in dice or 9 in dice)
    else:
        return value in dice

total = 0
for d1 in combinations(range(0, 10), 6):
    extended_sets = set()
    for d2 in combinations(range(0, 10), 6):
        all_squares = True
        for v1, v2 in squares:
            if not ((check_value_dice(v1, d1) and check_value_dice(v2, d2)) or\
                    (check_value_dice(v2, d1) and check_value_dice(v1, d2))):
                all_squares = False
                break
        if all_squares:
            extended_sets.add(d2)
    total += len(extended_sets)
print (total / 2)

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1)*1000,6), 'ms\n')

print('\n--------------------------SOLUTION 7 ,  hansaplast, Switzerland  --------------------------')
t1  = time.time()

from itertools import product, combinations
count = 0
for left,right in product(combinations(range(10),6), combinations(range(10),6)):
	left = list(left) + [6,9] if 6 in left or 9 in left else left
	right = list(right) + [6,9] if 6 in right or 9 in right else right
	for sl,sr in [(0,1),(0,4),(0,6),(1,6),(2,5),(3,6),(4,6),(8,1)]:
		if not(sl in left and sr in right) and not(sr in left and sl in right):
			break
	else:
		count += 1
print(count//2)

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1)*1000,6), 'ms\n')

print('\n--------------------------SOLUTION 8 ,  hacatu, USA  --------------------------')
t1  = time.time()


from itertools import combinations
pairs = [(0,1),(0,4),(0,6),(1,6),(2,5),(3,6),(4,6),(1,8)]

def f9(n):
	return 6 if n == 9 else n

def checkPair(a, b, pair):
	x, y = pair
	return (x in a and y in b) or (y in a and x in b)

def check(a, b):
	return all([checkPair(a, b, pair) for pair in pairs])

c = 0
for a in combinations(range(10), 6):
	for b in combinations(range(10), 6):
		if check([f9(n) for n in a], [f9(n) for n in b]):
			c += 1;

print(c//2)

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1)*1000,6), 'ms\n')

print('\n--------------------------SOLUTION 9 , mmaximus, Portugal   --------------------------')
# Brute force... Why is this a 40% problem??
t1  = time.time()

from itertools import combinations, product
squares = {(0, 4), (0, 9), (1, 6), (2, 5), (4, 9), (6, 4), (3, 6), (0, 1), (8, 1)}

def is_ok(a, b):
    c = set(a)
    d = set(b)
    if 6 in c: c.add(9)
    if 9 in c: c.add(6)

    if 6 in d: d.add(9)
    if 9 in d: d.add(6)

    for pair in squares:
        if not (pair[0] in c and pair[1] in d):
            if not (pair[1] in c and pair[0] in d):
                return False
    return True

valid_solutions = set()
for com in product(combinations(range(0,10),6), combinations(range(0,10),6)):
    a, b = map(frozenset,com)

    if is_ok(a,b):
        if not(tuple([a,b]) in valid_solutions or tuple([b, a]) in valid_solutions):
            valid_solutions.add(tuple([a,b]))

print(len(valid_solutions))

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1)*1000,6), 'ms\n')
