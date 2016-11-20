#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Wed, 12 Oct 2016, 00:44
#The  Euler Project  https://projecteuler.net
'''
Concealed Square        -       Problem 206
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
'''
import time
t1  = time.time()

for i in range(1389226620, 1010101010, -10):
    if str(i)[-2] == '3' or str(i)[-2] == '7' :
            j = i**2
            #print(i,'  ',j ,'   ', len(str(j)),'   ', str(j)[::2])
            #break
            if j > 2*10**18 : break
            if str(j)[::2] == '1234567890' :
                print('This is a the seeked number :', i)               # 1389019170
                break

t2  = time.time()
print('\n' ,' Completed in :', round((t2-t1),4), 's\n')

print('\n============== OTHER SOLUTIONS FROM THE EULER FORUM =============')

print('\n---------------------------- SOLUTION 1, lmdamato, Netherlands -----------------------------')


t1  = time.time()

# for x in range(1010101010, 1389026621, 10) :
# 	if str(x*x)[::2] == "1234567890" :
# 		print (x)
# 		break

t2  = time.time()
print('\n' ,' Completed in :', round((t2-t1),4), 's\n')

print('\n---------------------------- SOLUTION 2, , VERY FAST,  akerzner  , Canada -----------------------------')
# First time posting my code, since I didn't see any similar strategies.
# Like everyone else, I ignored the last digit since it had to be 0.
# Then, I used the fact that any string of numbers concatenated with an n-digit number,
# when squared, always has the same last n digits. For example: 143^2 = 20449. 98143^2 = 9632048449.
# Notice how they both end with "449".
# Using this, I was able to add on numbers to the solution to come up with a short-ish list of candidate numbers.
# Then I just checked the positions of 1,2,3,...,9,0
# Runs in 3.3 seconds.



t1  = time.time()

d9 = ['3','7']
d7d8 = []
for n in range(100):
    for dig in d9:
            squared = int(str(n)+dig)**2
            if 800 < squared%(10**3) < 900:
                    if n>=10:
                        d7d8.append(str(n)+dig)
                    else:
                        d7d8.append('0'+str(n)+dig)
d5d6 = []
for n in range(100):
    for dig in d7d8:
            squared = int(str(n)+dig)**2
            if 70000 < squared%(10**5) < 80000:
                    if n>=10:
                        d5d6.append(str(n)+dig)
                    else:
                        d5d6.append('0'+str(n)+dig)
d3d4 = []
for n in range(100):
    for dig in d5d6:
            squared = int(str(n)+dig)**2
            if 6000000 < squared%(10**7) < 7000000:
                    if n>=10:
                        d3d4.append(str(n)+dig)
                    else:
                        d3d4.append('0'+str(n)+dig)
d1d2 = []
for n in range(100):
    for dig in d3d4:
            squared = int(str(n)+dig)**2
            if str(squared)[0]=='1':
                if 500000000 < squared%(10**9) < 600000000:
                        if n>=10:
                            d1d2.append(str(n)+dig)
                        else:
                            d1d2.append('0'+str(n)+dig)
candidates = [int(number+'0') for number in d1d2]
for number in candidates:
    sq=str(number**2)
    if sq[0] == '1' and sq[2]=='2' and sq[4] =='3' and sq[6]=='4' and sq[8]=='5' and sq[10]=='6' and sq[12]=='7' and sq[14]=='8' and sq[16]=='9':
        print (number, sq)

t2  = time.time()
print('\n' ,' Completed in :', round((t2-t1),4), 's\n')

print('\n---------------------------- SOLUTION 3, INCREDIBLE FAST,  daOnlyBG  , USA -----------------------------')

t1  = time.time()

start = 101010101
end = 138902662

for i in range(end, start, -1):
    if str(i)[-1]=='3' or str(i)[-1]=='7':
        X = str(i**2)
        if X[0]=='1' and X[2]=='2' and X[4]=='3' and X[6]=='4' and X[8]=='5' and X[10]=='6' and X[12]=='7' and X[14]=='8' and X[16]=='9':
            print (10*(int(X)**0.5))
            break

t2  = time.time()
print('\n' ,' Completed in :', round((t2-t1),4), 's\n')

print('\n---------------------------- SOLUTION 4, VERY NICE & FAST,  FJ_Sevilla  , Spain -----------------------------')


# Doing some smart reduction. First, remove the trailing two zeros.
# Once removed, most people found out last digit must be 3 or 7.
# I did farther analysis, and found 24 options for the last 3 digits (43, 53, 83, 167, 197, 207, 293, ...).
# Similarly, found 240 options for the last 5 digits.
# Then, I had to iterate only 10000 to find the first 4 digits of the square root.
# total time: 0.2 seconds in Python!

t1  = time.time()

for sq in (p + f for f in (30, 70) for p in range(1389026600, 1010101000, -100)):
    if str(sq * sq)[::2] == '1234567890': break
print(sq)

t2  = time.time()
print('\n' ,' Completed in :', round((t2-t1),4), 's\n')

print('\n---------------------------- SOLUTION 5, SLOWER ,  logit  , USA -----------------------------')
# I started with seeing how big the search space was (the difference between the smallest and largest possible bases)
#  and it was about ~380 million -- too much to brute force.
# To trim down this search space, we know the square has a last digit 0, so the base must have the last digit as 0 too.
#  This means the square has the last digits 00, so we can fill that in at the end, and only consider the rest (1_2_3_4_5_6_7_8_9)
# which must also be a perfect square.
#
# To trim it down further, we see a perfect square ending in 9 must have a base that ends in 3 or 7,
# so cut the search space in 10 again, and try each with the last digit 3 and 7.

# At this point we're only checking ~7.5 million numbers, which is feasible.

t1  = time.time()

from math import sqrt

lower = 10203040506070809
upper = 19293949596979899

digits = [str(i) for i in range(1,10)]

def is_concealed(n):
    t = tuple(str(n))
    for k in range(9):
        if t[k*2] != digits[k]:
            return False
    return True

for i in range(int(sqrt(lower)/10), int(sqrt(upper)/10)):
    for j in (3, 7):
        n = i*10 + j
        if is_concealed(n**2):
            print (n * 10)

t2  = time.time()
print('\n' ,' Completed in :', round((t2-t1),4), 's\n')

