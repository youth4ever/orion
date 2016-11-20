#!/usr/bin/python3
# Solved by Bogdan Trif @   Completed on Fri, 23 Sep 2016, 16:38
#The  Euler Project  https://projecteuler.net
'''
Largest exponential     -       Problem 99
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.
However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.
Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a
base/exponent pair on each line, determine which line number has the greatest numerical value.
NOTE: The first two lines in the file represent the numbers in the example given above.
'''
import math as np
import time

print(np.log10(519432))

# Using pandas to manipulate files
print( ' ------------------   Using pandas to manipulate files  -----------')
import pandas as pd
df=pd.read_csv('pb099_base_exp.txt', sep=',',header=None)
print(df.values)

print('------'*20)
print('\n ---  MY SOLUTION ---------\n')
t1  = time.time()

# Load the file line by line separated by new line and on each line separated by comma :
filePath = r'pb099_base_exp.txt'
base_exp = [(line.rstrip('\n')).split(',') for line in open(filePath)]

# Transform the data into INTEGERS :
for i,line in enumerate(base_exp):
    base_exp[i] = [int(num) for num in line]
#print(type(base_exp[0][0]),  type(base_exp[0]),  base_exp[0:7])

maxval=0
iter = 0
for i in range(0, len(base_exp)):
       if maxval < np.log10(base_exp[i][0])* base_exp[i][1]:
              maxval = np.log10(base_exp[i][0])* base_exp[i][1]
              iter = i+1
       #print(str(i+1)+'.   ',base_exp[i][0], base_exp[i][1], end='    ')
       #print(np.log10(base_exp[i][0])* base_exp[i][1])

print('The maximum value is ',maxval,'  on the line ',iter)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')                 # Completed in :   Completed in : 5.0004 ms

###############################################
print('\n============  OTHER SOLUTIONS FROM EULER FORUM =============')
print('\n----------------SOLUTION 1 , yukuku from Indonesia-------------------------')
t1  = time.time()

m=[[int(c) for c in line.split(',')] for line in open('pb099_base_exp.txt').readlines()]
print (max((i for i in range(len(m))), key=lambda i: m[i][0]**(m[i][1]/100000.0)) + 1)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')                # 6.0003 ms

print('\n----------------SOLUTION 2 -------------------------')

t1  = time.time()

from timeit import default_timer as timer
from math import log

def PE_0099():

    with open("pb099_base_exp.txt") as f:
        data=[[int(x) for x in line.split(",")] for line in f]

    maxval=-1
    for i in range(len(data)):
        value=data[i][1]*log(data[i][0])
        if value>maxval:
            maxval=value
            maxline=i

    print (maxline+1,data[maxline],maxval)



PE_0099()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')                #Completed in : 6.0005 ms

print('\n----------------SOLUTION 3 , INTERESTING LOADING of FILE-------------------------')

t1  = time.time()

import math
count = 1
big_line = 1
my_log = 0
with open("pb099_base_exp.txt","r") as f:
    text = f.readlines()
    for line in text:
        base, exp = line.split(",")
        baseI = int(base)
        expI = int(exp)
        log10 = math.log10(baseI)
        logNum = expI*log10
        if logNum > my_log:
            my_log = logNum
            big_line = count
        count += 1
f.close()

print (big_line)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')