#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 22 Oct 2016, 12:31
#The  Euler Project  https://projecteuler.net
'''
                            Cubic permutations      -       Problem 62

The cube, 41063625 (345**3), can be permuted to produce two other cubes:
56623104 (384**3) and 66430125 (405**3).

In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

import time
from itertools import permutations
from math import factorial
print('------------- TESTS ------------------')

nr = list(str(41063625))
perm = list(permutations(nr))

def intersect(a, b):
     return list(set(a) & set(b))

for i in range(len(perm)):
    print(str(i+1)+'.   ', perm[i] , end='  ')
    if i == 10 : break

print('\n8! = ',factorial(8),'\n\n')

print('-------------------------   MY FIRST SOLUTION  -  PAINSTAKINGLY SLOW ----------------------------------')

t1  = time.time()



# RANGES :
#48-100,   101-215,   216-464,   465-1000,   1001-2154,   2155-4641,   4642-9999
#
# SETS = []
# P=[]
# down = 4642
# c,maxi = 0, 0
# for i in range(down,100000):
#     c +=1
#     if len(str(i**3)) == len(str(down**3)) :
#         pass
#         #print('-----------')
#         #print(str(i)+'.   ', i , i**3)
#         if maxi < i+1 : maxi = i+1
#     else:        break
#     for j in range(i+1, i+c ) :
#         #print(i,'   ' ,j-c)
#         u = sorted(str(i**3))
#         v = sorted(str((j-c)**3))
#         if u ==v :
#             #print( i,    j-c ,'      ' , sorted(str(i**3)))
#             P = P+[[i, j-c]]
#
# print('\nUp Range: ',maxi, 'Lower Range down :', maxi-1)
#
# print('\n\nPairs:   ',len(P),P,'\n')
#
# counter=0
# for k in range(len(P)+1) :
#     tmp=[]
#     for l in range(k+1,len(P) ) :
#         counter += 1
#         #print(str(counter)+".  ",P[k] , P[l])
#         if P[l][0] in P[k] or P[l][1] in P[k] :
#             print(list(set(P[k]+P[l])))
#             tmp = tmp+list(set(P[k]+P[l]))
#             tmp = list(sorted(set(tmp)))
#     if len(tmp) > 3 and tmp not in SETS :
#         SETS.append(tmp)
#
#
# print('\n\nSETS:', len(SETS), SETS)
# print('\nAnswer : ', min([ SETS[i][0]**3 for i in range(len(SETS)) if len(SETS[i])>=5 ]) )         # Answer 127035954683


t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')            # Shame time of 151.040639 s

#SETS = [[227, 221], [319, 289], [341, 329]]

# val=0
# for i in range(len(SETS)-1):
#     if intersect(SETS[i] ,SETS[i+1]) != [] :
#         val+=1
# print(val)


print('-------------------------   MY OPTIMIZED  SOLUTION    ----------------------------------')

t1  = time.time()

def cubic_permutations():
    '''Uses a dictionary to store sorted numbers as keys and lists as values '''

    from itertools import count
    d = {}
    for i in count():
        cube = i**3
        signature = ''.join(sorted(str(cube)))
        #print(signature)
        if signature in d:
            d[signature].append(cube)
            #print(d[signature])
            if len(d[signature]) == 5:
                print(d[signature][0])
                break
        else :
            d[signature] = [cube]       # Here we add a list value to each key of the dictionary, Nice idea !

cubic_permutations()



t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1)*1000, 6), 'ms\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1 ,  VERY FAST & HIGHLY EFFICIENT, Hoff1 , USA --------------------------')
# Runs in just over a second without placing any upper bounds on indices.
# Calculates cubes and then searches a list to see how many times permutations of that number have occurred before.
# Once 5 are found, the first occurrence of those permutations is printed.

t1  = time.time()

cubes, cube_sort = [], []
n, c = 0, 0
while c != 5:
    n += 1
    cubes.append(n**3)
    a = list(str(cubes[-1]))
    cube_sort.append(a)
    a.sort()
    c = cube_sort.count(a)
print(cubes[cube_sort.index(a)])

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')



print('\n--------------------------SOLUTION 2 ,  VERY FAST & , Aolea , Spain --------------------------')
t1  = time.time()

i = 415
flag = True
listAux = []
aux = []
count = []
while flag == True:
    i = i + 1
    aux1 = i**3
    listAux1 = sorted(list(str(aux1)))
    if listAux1 in listAux:
        count[listAux.index(listAux1)] = count[listAux.index(listAux1)] + 1
        if count[listAux.index(listAux1)] == 5:
            flag = False
    else :
        count.append(1)
        aux.append(i)
        listAux.append(listAux1)
print(aux[listAux.index(listAux1)]**3)

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')


print('\n--------------------------SOLUTION 3 ,  the NICEST, the BEST, the FASTEST , markus.obi, Germany --------------------------')
print('----> Incredibil de tare Solutia !!!!!! <------------------- \n')
# One of the easiest and fastest to solve problems for me.
# The key idea is to just convert the cube to string, sort the string and count the occurrences of each sorted string in a dictionary.
# i.e. sorting the strings "41063625", "56623104" and "66430125" gives the signature "01234566"
# 1-2 minutes to code. 15 milliseconds to run.

import itertools
t1  = time.time()

def solve():
    d = dict()
    for i in itertools.count():
        cube = i*i*i
        signature = "".join(sorted(str(cube)))
        if signature in d:
            d[signature].append(cube)
            if len(d[signature]) == 5:
                print(d[signature][0])
                return
        else:
            d[signature] = [cube]

solve()

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1)*1000,6), 'ms\n')      #  51.002979 ms


print('\n--------------------------SOLUTION 4 , mathcat, USA  --------------------------')
# One of the simpler one. Runs in milisecs.  I created a 10 digit number for each cube with each digit counting how many 0s or 1s or 2s etc.
# This number is added to hash (dictionary in python). Every time new cube is computed, it checks against dictionary and adds to it.
# If anytime while adding, there are 5 elements associated with that dictionary entry, program terminates.
t1  = time.time()

import sys
import os
import math

def digit_counts(n):
   dc = [0]*10
   r = 0
   while n:
       dc[n % 10], n = dc[n % 10]+1, n // 10

   for i in range(0, 10):
       r = r + (dc[i] * (10**i))
   return r

def main ():
    limit = 10000
    if (len(sys.argv) == 2):
        limit = int(sys.argv[1])

    cubes_dc_dict = dict()
    for n in range (1, limit):
        cube = n**3;
        dc = digit_counts(cube)
        if dc in cubes_dc_dict:
            cubes_dc_dict[dc].append(n)
            if ((len(cubes_dc_dict[dc]))==5) :
                print (cubes_dc_dict[dc], "->",  cubes_dc_dict[dc][0]**3)
        else:
            cubes_dc_dict[dc] = [n]

if __name__ == "__main__":
  main()

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')


print('\n--------------------------SOLUTION 5 , I have seen better, MatthewDonovan, Denmark   --------------------------')
t1  = time.time()
# I generated all the cubes of all numbers less than 10^5.
# Then I wrote a separate function to generate a string containing the number of each digit contained in the number.
# e.g. 11322 becomes "0221000000". I then created a dictionary with those strings as the keys and the cubes as the values.
# Once that was done, traverse the dictionary to find all keys with exactly 5 values mapping to them.

cubes = []

def digits(n):
    output_list = [0] * 10
    for q in str(n):
        output_list[int(q)] += 1
    output_str = ""
    for i in output_list:
        output_str += str(i)
    return output_str

for i in range(1, 10**4):
    cubes.append(i**3)

dict_of_numbers = {}
for i in cubes:
    if digits(i) in dict_of_numbers:
        dict_of_numbers[digits(i)].append(i)
    else:
        dict_of_numbers[digits(i)] = [i]

for i in dict_of_numbers:
    if len(dict_of_numbers[i]) == 5:
        print(dict_of_numbers[i])



t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')

print('\n--------------------------SOLUTION 6 ,  VERY VERY GOOD , carlitos, Spain --------------------------')

t1  = time.time()

from math import ceil
from collections import defaultdict

def permuted_cubes(digits=10, times=3):
    group = defaultdict(list)
    for n in range(10, ceil(pow(10, digits/3))):
        n3 = n**3
        group[tuple(sorted(str(n3)))].append(n3)
    for lst in group.values():
        if len(lst) >= times:
            yield lst

print(list(permuted_cubes(12, times=5)))
#print(min(min(list(permuted_cubes(12, times=5)))))      # This operation takes about 100 ms

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1)*1000,6), 'ms\n')      # Completed in  : 79.004526 ms
