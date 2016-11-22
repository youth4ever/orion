#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sun, 20 Nov 2016, 23:12
#The  Euler Project  https://projecteuler.net
'''
                                                            Magic 5-gon ring        -   Problem 68
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example),
each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

                                                 Total	           Solution Set
                                                    9	        4,2,3; 5,3,1; 6,1,2
                                                    9	        4,3,2; 6,2,1; 5,1,3
                                                    10	        2,3,5; 4,5,1; 6,1,3
                                                    10	        2,5,3; 6,3,1; 4,1,5
                                                    11	        1,4,6; 3,6,2; 5,2,4
                                                    11	        1,6,4; 5,4,2; 3,2,6
                                                    12	        1,5,6; 2,6,4; 3,4,5
                                                    12	        1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings.
What is the maximum 16-digit string for a "magic" 5-gon ring?
'''
import time

print('\n--------------------------TESTS------------------------------')
t1  = time.time()
from itertools import permutations

digits = [1,2,3,4,5,6,7,8,9,10]
P = list(permutations(digits, 3))
print(len(P),P, '\n')

# def generate_3_gon_rings ():
cnt=0
d1 = [1,2,3,4,5,6]
P1 = list(permutations(d1, 3))
for i in range(len(P1) ) :
    A = tuple(P1[i])
    # print(A, sum(A), end='   ')
    d2 = [i for i in d1 if i not in A]
    # print(str(i)+'.   ',d2)
    P2 = list(permutations(d2, 2))
    for j in range(len(P2)):
        B   = (P2[j][0] , A[2] , P2[j][1] )
        # print(B, sum(B))
        if sum(A) == sum(B) :
            # if tuple(B) in P1 : P1.remove( tuple(B) )
            # print(len(P1))
            d3 = [ i for i in d2 if i not in P2[j]]
            C = ( d3[0], B[2], A[1] )
            if sum(C) == sum(B) :
                if A < B and A < C :
                    cnt+=1
                    print(str(cnt)+'.   ',A, B, C)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def Magic_Pentagon_ring():
    d1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    P1 = list(permutations(d1, 3))
    cnt=0
    for i in range(len(P1) ) :
        A = tuple(P1[i])
        d2 = [i for i in d1 if i not in A]
        P2 = list(permutations(d2, 2))
        for j in range(len(P2)):
            B   = (P2[j][0] , A[2] , P2[j][1] )
            if sum(A) == sum(B) :
                d3 = [ i for i in d2 if i not in P2[j]]
                # print(d3)
                P3 = list(permutations(d3, 2))
                for k in range(len(P3)):
                    C = ( P3[k][0], B[2], P3[k][1] )
                    if sum(C) == sum(B) :
                        d4 = [ i for i in d3 if i not in P3[k]]
                        # print(d4)
                        P4 = list(permutations(d4, 2))
                        for l in range(len(P4)):
                            D = ( P4[l][0], C[2], P4[l][1] )
                            if sum(D) == sum(C) :
                                d5 = [ i for i in d4 if i not in P4[l]]
                                # print(d5)
                                E = ( d5[0], D[2], A[1] )
                                if sum(E) == sum(D):
                                    if A < B and A< C and  A<D and A < E :
                                        cnt +=1
                                        U = ''.join( str(i) for i in list(A+B+C+D+E))
                                        print(str(cnt)+'.    ',A, B, C, D, E,  U)
                                        maxv = 0
                                        if len(U) == 16 :
                                            if int(U) > maxv :
                                                maxv = int(U)
    return print('\nAnswer :     ', maxv)

Magic_Pentagon_ring()           # Answer :      6531031914842725




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 160.009146 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')


print('\n--------------------------SOLUTION 1, mfm24    --------------------------')
t1  = time.time()

# I went for brute forcing with a list comprehension. Takes a couple of seconds.

from itertools import permutations
r= max(((a0,p0,p1), (a1,p1,p2), (a2,p2,p3), (a3,p3,p4), (a4,p4,p0))
       for a0, a1, a2, a3, a4, p0, p1,p2,p3,p4 in permutations(range(1,11))
       if 10 in (a0,a1,a2,a3,a4)
       if min(a0,a1,a2,a3,a4) == a0
       if a0+p0+p1 == a1+p1+p2 == a2+p2+p3 == a3+p3+p4 == a4+p4+p0)

print("".join("".join(str(d) for d in triple) for triple in r))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, VERY GOOD,  Avi Levy, USA  --------------------------')
t1  = time.time()

# double counting shows that 11 + average on inner inner = common sum of lines
# since average on inner inner is between 3 and 7 (inclusive),
# this proves the common sum is between 14 and 18 (inclusive).

sols = []
queue = [([],[10],set(range(1,10)),j) for j in range(14,19)]
while queue:
  inner, outer, remaining, s = queue.pop(0)
  li, lo = len(inner), len(outer)

  satisfied = True
  for i in range(li-1):
    if i >= lo:
      break
    if inner[i] + inner[i+1] + outer[i] != s:
      satisfied = False
      break
  if not satisfied:
    continue

  if li == 5 and lo == 5:
    o = ""
    m = min(outer)
    j = outer.index(m)
    for i in range(5):
      o += str(outer[(i+j)%5]) + str(inner[(i+j)%5]) + str(inner[(i+j+1)%5])
    sols.append(o)
    continue

  n = None

  # extend outer ring
  if li > lo + 1:
    n = s - inner[lo] - inner[lo+1]

  if li == 5 and lo == 4:
    n = s - inner[-1] - inner[0]

  if n:
    if n in remaining:
      queue.append((inner, outer + [n], remaining - {n},s))
    continue

  # extend inner ring
  if li == 4:
    n = 5*(s - 11) - sum(inner)

  if 1 <= li < lo + 1:
    n = s - inner[-1] - outer[li-1]

  if n and n not in remaining:
    continue

  for i in [n] if n else remaining:
    queue.append((inner + [i], outer, remaining - {i},s))

print(max(sols))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 4, THE BEST - VERY VERY GOOD, philiplu, USA  --------------------------')
t1  = time.time()

# One millisecond in Python 3 (which seems to be the timer resolution in Windows),
# thanks to time spent thinking about how to prune down the solution space from the original 10!
#
# * The 10 must be in the outer group (solution space 10!/2)
# * The inner nodes' sum must be divisible by 5 (solution space 374,400)
# * Once you pick the inner nodes, the outer nodes are forced (solution space now 3,120)
# * Avoid rotations by ignoring permutations that don't leave the minimum outer node
# in the upper left position (solution space now just 624).
#
# After enough initial thought, the actual coding was trivial.

'''
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and
each line adding to nine.

                                        (4)
                                          \
                                          (3)
                                          / \
                                        (1)-(2)-(6)
                                        /
                                      (5)

Working clockwise, and starting from the group of three with the numerically
lowest external node (4,3,2 in this example), each solution can be described
uniquely. For example, the above solution can be described by the set: 4,3,2;
6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and
12. There are eight solutions in total.

Total      Solution Set
9       4,2,3; 5,3,1; 6,1,2
9       4,3,2; 6,2,1; 5,1,3
10      2,3,5; 4,5,1; 6,1,3
10      2,5,3; 6,3,1; 4,1,5
11      1,4,6; 3,6,2; 5,2,4
11      1,6,4; 5,4,2; 3,2,6
12      1,5,6; 2,6,4; 3,4,5
12      1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum
string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to
form 16- and 17-digit strings. What is the maximum 16-digit string for a
"magic" 5-gon ring? (Warning - bad ASCII art ahead)

                                ()
                                 \
                                  \
                                  ()      ()
                                  / \    /
                                 /   \  /
                                ()    ()
                               /|     /
                              / |    /
                             () ()--()--()
                                |
                                |
                                ()

---

Brute force would mean checking 10! permutations in the 5-gon, but we can do
better.

Consider partitioning the numbers 1 to 10 into an outer group of 5, filling the
nodes outside the pentagon, and an inner group of 5, filling the nodes on the
pentagon.  The 10 must appear in the outer group to generate a 16 digit number.
That reduces the number of permutations to 10!/2.

Next, label the group of outer nodes A, inner nodes B.  Then sum(A)+sum(B) =
55, since that's just the digits from 1 to 10 in some order.  Each of the 5
lines has the same sum, so the sum of all 5 lines is 5 times more than that, so
also divisible by 5.  The sum of all 5 lines is the sum of the outer group plus
twice the sum of the inner group.  So:

    (sum(A) + sum(B)) mod 5 = 0
    (sum(A) + 2*sum(B)) mod 5 = 0
    --> sum(B) mod 5 = 0

Of the C(9,5) = 126 choices for the inside group, only 26 have a sum divisible
by 5.  The number of permutations is now down to 26 * 5! * 5! = 374,400.

But notice that once we pick a permutation of the inner group, each of the
outer nodes is forced.  That's because the sum along each line is the same, so
a permutation of the inner group picks 2 out of the 3 elements along each line,
forcing the third to add up to the line's sum.  The number of permutations to
check is now down to 26 * 5! = 3,120.

We can compute the sum along each line:

    sum(lines) = sum(A) + 2*sum(B)
               = 55 - sum(B) + 2*sum(B)
               = 55 + sum(B)

So each line has the sum 11+sum(B)/5.  To test each of the 3,120 permutations
of the inner group, force the outer node on each line to 11+sum(B)/5 minus the
sum of the two inner nodes of that line.  If that forced number isn't in the
outer group, or has already been picked, we can ignore this permutation.

Finally, according to the problem instructions, we start numbering at the
lowest outer node.  If a permutation doesn't result in that minimum value in
our first outer node, ignore it.

'''


import itertools as it

def p68():
    results = []
    for inner in it.combinations(range(1, 10), 5):
        inner_sum = sum(inner)
        if inner_sum % 5 != 0:
            continue
        outer = set(range(1, 11)) - set(inner)
        outer_min = min(outer)
        line_sum = 11 + inner_sum // 5
        for inner_perm in it.permutations(inner):
            if line_sum - inner_perm[0] - inner_perm[1] != outer_min:
                continue
            outer_perm = (outer_min,
                          line_sum - inner_perm[1] - inner_perm[2],
                          line_sum - inner_perm[2] - inner_perm[3],
                          line_sum - inner_perm[3] - inner_perm[4],
                          line_sum - inner_perm[4] - inner_perm[0])
            if outer == set(outer_perm):
                result = [outer_perm[0], inner_perm[0], inner_perm[1],
                          outer_perm[1], inner_perm[1], inner_perm[2],
                          outer_perm[2], inner_perm[2], inner_perm[3],
                          outer_perm[3], inner_perm[3], inner_perm[4],
                          outer_perm[4], inner_perm[4], inner_perm[0]]
                results.append(int(''.join(str(node) for node in result)))
                # print(results[-1], inner_perm, outer_perm)
    return max(results)

print(p68())



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, armamut, Turkey  --------------------------')
t1  = time.time()

# Project Euler #68
# 16.10.2015 20:30

from itertools import permutations

megalist = []
a = range(1,10)
for x in permutations(a):
	s = 10+x[4]+x[5]
	if (x[0]+x[5]+x[6]==s) and (x[1]+x[6]+x[7]==s) and (x[2]+x[7]+x[8]==s) and (x[3]+x[8]+x[4]==s):
		thelist = [ (10,x[4],x[5]), (x[0],x[5],x[6]), (x[1],x[6],x[7]), (x[2],x[7],x[8]), (x[3],x[8],x[4]) ]
		mm = x.index(min(x[0:4]))+1
		thelist = [ thelist[(i+mm)%5] for i in range(5) ]
		thelist = ''.join( [ ''.join(map(str,i)) for i in thelist ]  )
		megalist.append(thelist)

print (max(megalist))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 6,  Nidjo123, Croatia --------------------------')
t1  = time.time()

import itertools

def is_valid_ring(outer, inner):
    s = outer[4] + inner[4] + inner[0]

    for i in range(4):
        if outer[i] + inner[i] + inner[i + 1] != s:
            return False

    return True

def toString(outer, inner):
    res = ""

    for i in range(4):
        res += str(outer[i]) + str(inner[i]) + str(inner[i + 1])

    res += str(outer[4]) + str(inner[4]) + str(inner[0])

    return res

inner = [1, 2, 3, 4, 5]

outer = range(7, 11, 1)

inner_perms = list(itertools.permutations(inner))
outer_perms = list(itertools.permutations(outer))

res = True

for outer_perm in outer_perms:
    for inner_perm in inner_perms:
        outer = list(outer_perm)
        outer.insert(0, 6)

        if is_valid_ring(outer, inner_perm):
            s = toString(outer, inner_perm)

            if len(s) == 16:
                if res == True:
                    res = s
                elif int(s) > int(res):
                    res = s


print(res)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
