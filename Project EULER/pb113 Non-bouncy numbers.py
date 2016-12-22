#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 10 Dec 2016, 14:18
#The  Euler Project  https://projecteuler.net
'''
                                          Non-bouncy numbers        -       Problem 113
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that
there are only 12951 numbers below one-million that are not bouncy
and only 277032 non-bouncy numbers below 10**10.

How many numbers below a googol (10**100) are not bouncy (monotonic ) ?
'''
import time

print('--------------------------TESTS------------------------------')

n = 9972  #, 9910, 6664, 6662

def monotonic_number(n) :       # Non-bouncy
    ''':Description: Function to check if a number is non-bouncy (monotonic).
    Example : 12235, 22222, 1579, 23459 , 885522, 9821, 966661  - are non-bouncy (monotonic)

    :param n: int, the number to check
    :return: boolean, True or False
    '''
    listN = list(str(n))
    flag1 = False
    flag2 = False
    for i in range(1, len(listN)):
        if listN[i] > listN[i-1]:
            flag1 = True
        if listN[i] < listN[i-1]:
            flag2 = True
    if flag1 == True and flag2 == True:
        return False
    else : return True


print('Test for bouncy_number Function :  ', monotonic_number(n),'\n' )        # Functions Tests look good


print('\n ------------  MANUAL TEST For INCREASING & DECREASING -------------' )

# cnt = 0     # DECREASING
# for i in range(9, 0, -1):
#     for j in range(i , -1 , -1):
#         # print(str(cnt)+'.   ', i, j)
#         for k in range(j, -1, -1) :
#             for l in range(k, -1, -1) :
#                 for m in range(l, -1, -1) :
#                     cnt+=1
#                     print(str(cnt)+'.   ', i, j, k, l, m)

# cnt = 0      # INCREASING
# for i in range(1, 10):
#     for j in range(i,10):
#         for k in range(j,10) :
#             for l in range(k,10) :
#                 for m in range(l, 10) :
#                     cnt+=1
#                     print(str(cnt)+'.   ', i, j, k, l, m)

# S = 0         # MODEL LOOP
# def loop_rec(y, number):
#     global S
#     if (number >= 1):
#         loop_rec( y+1, number - 1 )
#         s = 0
#         for i in range(1, y):
#             s+=i
#             print(i, end=' ')
#         S+=s
#         print('    ',s, S)
#     else:
#         return
#
# loop_rec(1, 10)


print('------------------------------ AUTOMATED TESTS --------------------------')

print('Method to check that my algorithm is correct :')
def automated_test():
    cnt=0
    for i in range(10**0, 10**5):
        b = monotonic_number(i)
        if b == True :
            print(str(i) + '.     : ' , b )
            # if i > 100 :
            cnt+=1

    return print('\ncnt:  ', cnt )

# automated_test()            # cnt:   474 -->  1-1000 ;       1674 --> 1-10.000   ;       4953 --> 1-100.000

########### CHECH VALUES ####################
# 100-1000 : 375 ;   1000-10000 : 1200 ;   10000-100000 : 3279;    1e5-1e6 : 7998 ;
# 1-1000000 :   12951
# This problem must be done by analyzing the string sequence for increase or decrease, not by manually
# analyzing all the range !  RECURSION



print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

print('\n-------------INCREASING ----------------------')
I  = []
def Non_Bouncy_inc( length ):        #### INCREASING RECURSION
    global I
    if length == 2 :
        I = [list(range(1,10))]
    if length > 2 :
        Non_Bouncy_inc( length-1 )
        tmp = I[-1].copy()
        for i in range(1, 10):
            tmp[i-1] = sum(I[-1][0:i])
            # print(tmp[0:j], '   ',sum(tmp[0:j]) )
        I.append(tmp)
    # print(I)
    return   sum(I[-1])

print('\n\nthe Function Test Non_Bouncy_inc : \t',Non_Bouncy_inc(6))
print('\n',I)

print('\n------------------DECREASING ----------------------')
D  = []
def Non_Bouncy_dec(length ):    ####### DECREASING RECURSION
    global D
    if length == 2 :
        D = [list(range(2,11))]
        # print(D)
    if length >2 :
        Non_Bouncy_dec(length-1 )
        tmp = D[-1].copy()
        # print('tmp:    ->  ',tmp)
        for j in range(1, 10):
            tmp[j-1] = sum(D[-1][0:j])+1
            # print(tmp[0:j], '   ',sum(tmp[0:j])+1 )
        D.append(tmp)

    return   sum (D[-1]) #, D        # sum([ sum(i) for i in  D ])

print('\n\nthe Function Test Non_Bouncy_dec : \t',Non_Bouncy_dec( 4 ),'\n')
print('\n',D)

print('\n---------------------------------------------')
def solution_pb113(power=7):
    total = 99
    for h in range(3, power+1):
        # D, I = [], []
        a = Non_Bouncy_inc(h)
        b = Non_Bouncy_dec( h)
        total += a+b-9
        # print(a, b , total)

    return print('\nAnswer :\t ',total)

solution_pb113(100)         # Answer :  51161058134250





t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n================  My SECOND SOLUTION, VERY FAST  ===============\n')
t1  = time.time()

def solution_2(nr_length) :
    u = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    d = [ 2, 3, 4, 5, 6, 7, 8, 9, 10]
    S = 99
    length = 100
    for j in range(length - 2):
        I = u.copy()
        D = d.copy()
        for i in range(len(u)) :
            u[i] = sum(I[0:i+1])
            d[i] = sum(D[0:i+1])+1
        S+= sum(u)+sum(d)+1-9
        # print(d, f, sum(d)+sum(f) )
    return print('\nAnswer:\t',  S-length+2)

solution_2(100)

# automated_test()            # cnt:   474 -->  1-1000 ;       1674 --> 1-10.000   ;       4953 --> 1-100.000

########### CHECH VALUES ####################
# 100-1000 : 375 ;   1000-10000 : 1200 ;   10000-100000 : 3279;    1e5-1e6 : 7998 ;
# 1-1000000 :   12951


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  INSTANT & VERY SIMPLE --------------------------')
t1  = time.time()
# ======= Wed, 25 May 2016, 18:09, froycard, Venezuela

# Trying to do it by using Brute-Force, but obviously it was farthest worst option to solve this,,,
# in billions of years (2.31481481481e+89 years) to arrive at a solution...
# so the other way is using other mathematic algorithm to get the solution...
# My solution in Python:

from math import factorial as fact
def comb(n,k):
	return int(fact(n)/(fact(k)*fact(n-k)))
print (comb(109, 100)+comb(110, 100)-(1001+1))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()
# Sun, 21 Aug 2016, 15:05,  gvhl  , Netherlands
# Recursive algorithm using some memoization by dictionary.
# The rising function can start with a 0 so it counts any number in the form of 000xxx as well,
# whilst the descending function is started at a positive integer (starting at 0 would only give 1 solution anyway)
# so the numbers with a fewer amount of digits need to be counted as well.
#
# At last per amount of digits counted 10 needs to be subtracted, seeing as numbers in the form iiiii
# (such as 88888) are counted twice, once by both algorithms.

dicstijg = {}
dicdaal = {}
for l in range(10):
    dicstijg[l] = {}
    dicdaal[l] = {}

def funcstijg(n, diep):
    if diep == 1:
        return 10-n
    else:
        res = 0
        for i in range(n, 10):
            if diep-1 in dicstijg[i]:
                res += dicstijg[i][diep-1]
            else:
                incr = funcstijg(i, diep-1)
                res += incr
                dicstijg[i][diep-1] = incr
        return res

def funcdaal(n, diep):
    if diep == 1:
        return n+1
    else:
        res = 0
        for i in range(0, n+1):
            if diep-1 in dicdaal[i]:
                res += dicdaal[i][diep-1]
            else:
                incr = funcdaal(i, diep-1)
                res += incr
                dicdaal[i][diep-1] = incr
        return res

def func(digits):
    som = funcstijg(0, digits)
    for k in range(1,digits+1):
        som +=  + funcdaal(9, k)

    for pos in range(digits):
        som -= 10

    return som-1

ans = func(100)
print ("result = " + str(ans))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()
# Sun, 30 Oct 2016, 12:52, aolea, Spain
# Going up is just combinations with replacement for each digit amount from 1 to the total amount of digits.
# Going down the same + the possible amount of 0-s at the end of each number.
#
# Total = up + down - numbers that appear in both up and down (9*number of digits.)

def fac(n):
    if n == 0:
        return 1
    else:
        aux = 1
        while n > 1:
            aux = aux * n
            n = n - 1
    return aux

def comb_w_repl(m,n):
    return int(fac(n+m-1)/(fac(n)*fac(m-1)))

digits = 100
non_bouncy_up = 0
non_bouncy_down = 0

for i1 in range(1,digits+1):
    non_bouncy_up = non_bouncy_up + comb_w_repl(9,i1)

for i1 in range(1,digits+1):
    non_bouncy_down = non_bouncy_down + comb_w_repl(9,i1)*(digits-i1+1)

total_non_bouncy = non_bouncy_up + non_bouncy_down - 9*digits
print(total_non_bouncy)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  RECURSION (with Memoization)  --------------------------')
t1  = time.time()
# ========= Tue, 1 Nov 2016, 23:08, roiesa, Israel
# Used memoized recursion. Memoization made it run very fast


def DecrMemo(dic,d,n):#q113 Number of decreasing sequences with length n with the digits 0 to d
        if ((d,n) in dic):
                return dic[(d,n)]
        elif (d==0):
                dic[(d,n)]= 1
        elif (n==1):
                dic[(d,n)] = d+1
        else:
                dic[(d,n)]=sum([DecrMemo(dic,i,n-1) for i in range(d+1)])

        return dic[(d,n)]

def q113(n):
        dic =dict()
        return sum([DecrMemo(dic,9,j) for j in range(1,n+1)])+DecrMemo(dic,9,n)-(n+1)-9*n

print(q113(100))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()
# ========== Sun, 13 Nov 2016, 21:35, Khalid , Saudia Arabia
# Thinking in combinatorics is tough. I knew it could be solved using combinations,
# but I couldn't figure out exactly how. So I just wrote out the logic, and it worked.
# It's fast too. It tells me there are 27575236359866967672053698477085136905925000 numbers under 10 to the power 100000 in around 3 seconds.


# counts are for two digit numbers, they are already included in the total
increasing = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
decreasing = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
equal = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
target = 100

total = 99
total_arr = [0] * 10
for i in range(2, target):
    for d in range(9, 0, -1):
        for d2 in range(9, d, -1):
            increasing[d2] += increasing[d] + equal[d]
    for d in range(0, 10):
        for d2 in range(0, d):
            decreasing[d2] += decreasing[d] + equal[d]
    for i in range(0, 10):
        total += increasing[i] + decreasing[i] + equal[i]

print (total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()
# ==========          Sun, 24 May 2015, 02:35,  mmaximus, Portugal

# I noticed this is like the coin partition problem: for example, an increasing number is determined by
# #0s + #1s + ... + #9s, as long as this adds to 100 (the number of digits).
# # This is like making a certain amount (100 in our case) with coins of certain denominations,
# # and the denominations are all 1 (one for each time we take a certain digit).
#
# For the decreasing numbers, we have to do each order of magnitude separately, since now 0s will appear on either side
# of the partition, and so we cannot capture them all in one go.
#
# Finally, we subtract the 'constant' numbers like 99999 8888 since these are double counted,
# and the number zero, which was counted 100 times.
#
# The code uses the DP solution posted in previous problems, and is extremely fast:

options = [1,1,1,1,1,1,1,1,1,1]

total = 0
amount = 100
ways = [0]*(amount + 1)
ways[0] = 1
for i in range(len(options)):
    for j in range(options[i], amount+1):
        ways[j] += ways[j - options[i]]

for i in range(2, amount):
    total += ways[i]

total += 2* ways[amount]
print(total-9*(amount-1)-amount)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n',globals())






