#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Digit power sum     -       Problem 119

The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 8**3 = 512.
Another example of a number with this property is 614656 = 28**4.

We shall define a_n to be the n-th term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a_10 = 614656.

Find a_30.
'''
import time
from itertools import count
import numtheory
import gmpy2

print('\n--------------------------TESTS------------------------------')


def end_of_loop():
    raise StopIteration
print('This loop stops at 100 even if normally will go to Infinity :'  , list( end_of_loop() if i*i > 100 else  i*i for i in count(1) ))




print(gmpy2.is_power(78125))

print(gmpy2.iroot(125,3))


print('\n-------------------   INITIAL TESTING,   ------------------- \n')


# cnt = 0
# # for i in range(11, 10**6):
# for i in count(11):
#     o = [ int(i) for i in str(i)   ]
#     s = sum(o)
#     for j in range(1,6) :
#         if pow(s, j ) == i :
#             cnt+=1
#             print(str(cnt)+'.   ',i,  s,  j)

#
# 1.    81 9 2
# 2.    512 8 3
# 3.    2401 7 4
# 4.    4913 17 3
# 5.    5832 18 3
# 6.    17576 26 3
# 7.    19683 27 3
# 8.    234256 22 4
# 9.    390625 25 4
# 10.    614656 28 4
# 11.    1679616 36 4


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def end_of_loop():
    raise StopIteration

twos = list( end_of_loop() if i*i > 10**2 else  i*i for i in count(2) )
threes = list( end_of_loop() if pow(i, 3) > 10**5  else  pow(i, 3) for i in count(2) )
fours = list( end_of_loop() if pow(i, 4) > 10**7  else  pow(i, 4)for i in count(2) )
fives = list( end_of_loop() if pow(i, 5) > 10**9  else  pow(i, 5) for i in count(2) )
sixes = list( end_of_loop() if pow(i, 6) > 10**11  else  pow(i, 6) for i in count(2) )
sevens = list( end_of_loop() if pow(i, 7) > 10**13  else  pow(i, 7) for i in count(2) )
eigths = list( end_of_loop() if pow(i, 8) > 10**15  else  pow(i, 8) for i in count(2) )
nines = list( end_of_loop() if pow(i, 9) > 10**17  else  pow(i, 9) for i in count(2) )

D = { 2: twos , 3: threes , 4: fours , 5: fives , 6:  sixes , 7: sevens , 8: eigths , 9:  nines  }

POW = []
counter=0
for i in range(2, 9+1):
    # print(len(D[i]) ,D[i])
    for j in range(len(D[i])):
        s = sum([ int(k) for k in str(D[i][j]) ])
        if s ==  D[i].index( D[i][j] )+2  :
            counter+=1
            print(str(counter)+'.       pwr:', i  ,'    ',D[i][j] , '     ' ,D[i].index( D[i][j] )+2 )
            POW.append(D[i][j])

print('\nPowers List : ', len(POW) ,POW)

print('\nAnswer : ', POW[30-1])             #       Answer :  248155780267521

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n================  My SECOND SOLUTION, SIMPLER & IMPROVED  ===============\n')
t1  = time.time()

def end_of_loop():
    raise StopIteration

def digit_sum(n):
   r = 0
   while n:
       r = r + n % 10
       n = n // 10
   return r

def solve_pb119():
    POW = []
    counter=0
    for exp in range(2, 9+1):
        D = list( end_of_loop() if pow(i, exp) > 10**(2*exp-1) else  pow(i,exp ) for i in count(2) )
        for j in range(len(D)):
            s = digit_sum(D[j])
            if s ==  D.index( D[j] )+2  :
                counter+=1
                # print(str(counter)+'.       pwr:', i  ,'    ',D[j] , '     ' ,D.index( D[j] )+2 )
                # POW.append(D[j])
            if counter ==  30:
                return print('\nAnswer : \t',D[j])

solve_pb119()                   #   Answer :  248155780267521


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')





print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, List Comprehension  --------------------------')
t1  = time.time()

# ======== Thu, 26 May 2016, 02:48,   froycard, Venezuela
# My solution using Python and coding with one-liner style... pretty fast: around 0.05 seconds:

dict={	x**y:(x,y) for x in range(2,100) for y in range(2,40) if x**y>9 and x == sum([int(i) for i in (str(x**y))])}
print (sorted(dict.keys() )[29])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, VERY NICE ,aolea  --------------------------')
t1  = time.time()

# =========   Sun, 16 Oct 2016, 15:05,   aolea. Spain
# Looping low values of base and exponent and checking the base value against the digit sum of the exponentiation,
# later on sorting the results togged the position of each one.
# Less than 3 milliseconds in python

def digit_sum(n):
   r = 0
   while n:
       r = r + n % 10
       n = n // 10
   return r

results = []
for exponent in range(1, 10):
    if len(results)==30:
        break
    for base in range(1,100):
        if digit_sum(base**exponent) == base and base**exponent>10:
            results.append(base**exponent)
count = 1
for i in sorted(results):
    print(count,i)
    count = count + 1


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  NICE --------------------------')
t1  = time.time()

# =======  Fri, 14 Oct 2016, 00:38, mbh038, England
# About 3.1 ms in Python.
#
# I generate a set p_s of all the numbers  k**x>9 for x from 2 to 10 and k from 1 to 100.
# There are just 742 such numbers. Our a_n have to be among them, or among an extended such set.
# I make a sorted list of these, and also a dictionary pdpd of k:[k**x for x  from 2 to  10].
# For each element p in p_s, starting from the lowest, I find the sum p_sum of its digits,
# and check if p is in the list of powers of that sum, in the dictionary entry for it in p_d.
# If it is, we have our next a_n.


def an():
    ns={}
    n=0
    ps=set([k**x for x in range(2,10) for k in range(1,100) if k**x>9])
    pd={ k:[k**x for x in range(1,10)] for k in range(1,100) }
    ps=sorted(ps)
    for p in ps:
        psum=sum([int(i) for i in str(p)])
        if p in pd[psum]:
            n+=1
            ns[n]=p
            if n==30:
                break
    print (ns[30])

an()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ====== Sat, 17 Jan 2015, 23:34, rallen0527, USA
# .004 secs in Python, though it may be a little verbose.

def sumDigits(x):
    total = 0
    a = str(x)
    for c in a:
        total += int(c)
    return total

goodOnes = [1]

for a in range(2, 100):
    for b in range(2, 20):
        d = a ** b
        if d > 10**16:
            break
        c = sumDigits(d)
        if c == a:
            goodOnes.append(d)
    if len(goodOnes) == 35:
        break


goodOnes.sort()
print("The answer is", goodOnes[30])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()





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
