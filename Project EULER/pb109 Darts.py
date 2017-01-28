#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 21 Jan 2017, 13:52
#The  Euler Project  https://projecteuler.net
'''
                                Darts       -       Problem 109

In the game of darts a player throws three darts at a target board
which is split into twenty equal sized sections numbered one to twenty.


The score of a dart is determined by the number of the region that the dart lands in.
A dart landing outside the red/green outer ring scores zero.
The black and cream regions inside this ring represent single scores.
However, the red/green outer ring and middle ring score double and treble scores respectively.

At the centre of the board are two concentric circles called the bull region, or bulls-eye.
The outer bull is worth 25 points and the inner bull is a double, worth 50 points.

There are many variations of rules but in the most popular game the players will begin
with a score 301 or 501 and the first player to reduce their running total to zero is a winner.
However, it is normal to play a "doubles out" system,
which means that the player must land a double (including the double bulls-eye at the centre of the board)
on their final dart to win;
any other dart that would reduce their running total to one or lower means the score for that set of three darts is "bust".

When a player is able to finish on their current score it is called a "checkout"
and the highest checkout is 170: T20 T20 D25 (two treble 20s and double bull).

There are exactly eleven distinct ways to checkout on a score of 6:
                                +--------+
                                |D3|  |  |
                                |--+--+--|
                                |D1|D2|  |
                                |--+--+--|
                                |S2|D2|  |
                                |--+--+--|
                                |D2|D1|  |
                                |--+--+--|
                                |S4|D1|  |
                                |--+--+--|
                                |S1|S1|D2|
                                |--+--+--|
                                |S1|T1|D1|
                                |--+--+--|
                                |S1|S3|D1|
                                |--+--+--|
                                |D1|D1|D1|
                                |--+--+--|
                                |D1|S2|D1|
                                |--+--+--|
                                |S2|S2|D1|
                                +--------+
Note that D1 D2 is considered different to D2 D1 as they finish on different doubles.
However, the combination S1 T1 D1 is considered the same as T1 S1 D1.

In addition we shall not include misses in considering combinations; for example, D3 is the same as 0 D3 and 0 0 D3.

Incredibly there are 42336 distinct ways of checking out in total.

How many distinct ways can a player checkout with a score less than 100?


'''
import time


V = { 'S25' : 25, 'D25' : 50}     # dict with All the values
A = [ 'S25', 'D25' ]        # Singles, Doubles, Triples --> All
D = [ 'D25' ]       # Only Doubles -->D

for i in range(1, 21):
    # print(i , 'S'+str(i)  )
    V['S'+str(i) ] = i
    V['D'+str(i) ] = 2*i
    V['T'+str(i) ] = 3*i
    A.extend( [ 'S'+str(i), 'D'+str(i), 'T'+str(i)  ] )
    D.append( 'D'+str(i) )

print('Dict with the Total Darts values :' , len(V),'\n', V , '\n')
print('Singles + Doubles + Triples :\t',len(A), '\n',A)
print('Only  Doubles :\t',len(D), '\n', D)

print('\n--------------------------TESTS------------------------------')

# t1  = time.time()
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION, 50 ms  ===============\n')
t1  = time.time()


def first_sol_darts():
    U_100 , cnt = 0, 0
    for d in range(len(D)) :
        cnt+=1
        # print(str(cnt)+'.    ', D[d], '          ' ,V[D[d]])
        U_100 += 1
        for i in range(len(A)):
            cnt+=1
            if V[A[i]]+V[D[d]] < 100 :
                U_100 += 1
                # print(str(cnt)+'.    ', A[i] ,D[d],'             ' ,V[A[i]] , V[D[d]] , '=',V[A[i]] + V[D[d]])
            for j in range(i, len(A)):              # i because we need also combinations like T1 T1 ; D1 D1, S1 S1 ...etc...
                cnt+=1
                if V[A[i]] + V[A[j]] + V[D[d]] < 100 :
                    U_100 += 1
                    # print(str(cnt)+'.    ', A[i], A[j] ,D[d],'           ' ,V[A[i]], V[A[j]] ,V[D[d]] ,'=' ,V[A[i]] + V[A[j]] + V[D[d]] )

    return print('\nScore Checkouts <100  : \t', U_100)


first_sol_darts()               #   38182


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          #       Completed in : 52.003145 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  10 ms --------------------------')
t1  = time.time()

# ===== Wed, 23 Nov 2016, 17:47, mbh038, England
# Between 4 and 5 ms in Python. There are up to 21 ways to checkout with one dart,
# and if two or three darts are needed then the combined score of the of the first one or
# two darts has to leave us on a double score.
# The only tricky bit is to avoid double counting among the first two darts of the three dart finishes.

def mbh038(limit=100):
    #doubles
    dd=[2*x for x in range(1,21)]+[50]
    #1-dart scores
    d1=[x*y for x in range(1,21) for y in [1,2,3]]+[25,50]
    #1-dart and distinct two dart scores
    d1d2=d1+[d1[i]+d1[j] for i in range(62) for j in range(i,62)]

    #all the ways to finish on a double, using 1,2 or 3 darts
    total=len([x for x in dd if x<limit])+len([x+y for x in dd for y in d1d2 if x+y<limit])

    return print(total)

mbh038()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ===== Mon, 19 Dec 2016, 21:52, justin.saunders, England
# Just looked at this as a long list of possible other scores and a double as the first item.
# The other scores array has 0 and we only use the values later or equal in the array:

# Just have an array of 100 points (yes 0 and 1 won't be used)

tgt = 100
points = list(range(1, 21))
doubles = list(range(2, 41, 2))
triples = list(range(3, 61, 3))
points.append(25)
doubles.append(50)
ends = doubles[:]
others = [0] + points + doubles + triples
cnt = [0] * tgt

# ok so we need to finish on a double
for e in ends:
    for o1 in range(len(others)):
        for o2 in range(o1, len(others)):
            v = e + others[o1] + others[o2]
            if v < tgt:
                cnt[v] += 1

print ('Problem 109:', sum(cnt))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# === Fri, 26 Aug 2016, 23:09, tyrelt, USA
# I see a lot of posts claiming 'simple' code but I think mine is pretty tough to beat.
# Took me longer to write my list of possible scores than anything else.

scores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
          20, 25, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32,
          34, 36, 38, 40, 50, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39,
          42, 45, 48, 51, 54, 57, 60]

answer = 0
for i in range(len(scores)):
    for j in range(i, len(scores)):
        for score3 in scores[22:43]:
            if scores[i]+scores[j]+score3 < 100:
                answer += 1

print(answer)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# Tue, 11 Oct 2016, 17:23, piotrek_k, Python  , Poland

from itertools import combinations_with_replacement as combinations

single_throws = list(range(1, 21)) + [25]
double_throws = [2*i for i in single_throws]
triple_throws = [3*i for i in single_throws[:20]]
all_throws = single_throws + double_throws + triple_throws


checkout_in_1_throw = double_throws
checkout_in_2_throws = [    a + b for a in all_throws for b in double_throws]
checkout_in_3_throws = [    sum(a) + b for a in combinations(all_throws, 2) for b in double_throws]

all_checkouts = checkout_in_1_throw + checkout_in_2_throws + checkout_in_3_throws

print(len([i for i in all_checkouts if i < 100]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, SIMPLEST  --------------------------')
t1  = time.time()

# ==== Fri, 24 Oct 2014, 02:10 , HuggyHermit, Scotland

from itertools import combinations_with_replacement

scores = [0, 25, 50]
for m in range(1, 4):
    scores.extend(m*x for x in range(1, 21))
doubles = [50] + [2*x for x in range(1, 21)]

total = 0
for double in doubles:
    for others in combinations_with_replacement(scores, 2):
        if double + sum(others) < 100:
            total += 1

print (total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  VERY ELEGANT --------------------------')
t1  = time.time()

# ==== Sun, 30 Nov 2014, 15:56, tmikkelsen, Norway

from itertools import combinations_with_replacement

regions = set([('M', 0), ('S25', 25), ('D25', 50)])
for i in range(1,21):
    regions.update([('S' + str(i), i),
                    ('D' + str(i), 2*i),
                    ('T' + str(i), 3*i)])

checkouts = set()
for d in regions:
    if d[0].startswith('D'):
        for r1, r2 in combinations_with_replacement(regions, 2):
            checkouts.add((d[0], frozenset([r1[0], r2[0]]), d[1]+r1[1]+r2[1]))

sum(c[2] < 100 for c in checkouts)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7, DYNAMIC PROGRAMMING --------------------------')
t1  = time.time()

# # ====Tue, 2 Jun 2015, 02:46, wakkadojo, USA
# Some refreshing dynamic programming. Got thrown for a spin because I didn't notice we could only throw 3 darts.

def count (score, c, amt, d, m):
    if d < 1:
        return 0
    if amt == 0:
        return 1
    if amt < 0:
        return 0
    if c >= len (score):
        return 0
    key = (amt, c, d)
    if key not in m:
        m[key] = \
            count (score, c+1, amt, d, m) + count (score, c, amt-score[c], d-1, m)
    return m[key]

singles = list (range (1, 21)) + [ 25 ]
doubles = [ 2*x for x in singles ]
triples = [ 3*x for x in singles[:-1] ]
score = singles + doubles + triples
m = {}

print (sum (sum (count (score, 0, s-x, 3, m) for x in doubles) for s in range (100)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,  LIST COMPREHENSION --------------------------')
t1  = time.time()

# # ====Tue, 14 Jul 2015, 23:56, hornemann55, Denmark
# Simple and straight forward, runs in 35ms

doubles = list(range(2,41,2))
doubles.append(50)
all = list(range(0,21))
all.extend(doubles)
all.extend([i for i in range(3,61,3)])
all.append(25)
l = len(all)
print(sum([1 for i in range(l) for j in range(l) for d in doubles if all[i]+all[j]+d < 100 and j>=i]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 9,  SIMPLE --------------------------')
t1  = time.time()

# ====  Sat, 11 May 2013, 03:52, rblackadar, USA
# Straightforward yet fairly concise Python:

enddarts = [2*x for x in range(1,21)] + [50]
otherdarts = list(range(0,21)) + [25] + enddarts + [3*x for x in range(1,21)]

count = 0
for x in enddarts:
   for i,y in enumerate(otherdarts):
      for j,z in enumerate(otherdarts):
         if i>j: continue      # because we consider reversed order the same
         if x+y+z < 100: count += 1
print(count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 9,  11 ms --------------------------')
t1  = time.time()

# ====Mon, 15 Jun 2009, 14:01, lalitp, India
# This is my code in Python. Runs in 58ms

S=[i for i in range(1,21)]
D=[2*i for i in S]+[50]
T=[3*i for i in S]
S+=[25]
SDT=S+D+T
N=sum([1 for u in D if u<100])
N+=sum([1 for u in SDT for v in D if u+v<100])
N+=sum([1 for i,u in enumerate(SDT) for v in SDT[i:] for w in D if u+v+w<100])
print (N)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

