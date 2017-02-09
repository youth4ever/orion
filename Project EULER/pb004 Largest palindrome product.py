#!/usr/bin/python3
# Solved by Bogdan Trif @ 14 Sep 16 (21:54)
#The  Euler Project  https://projecteuler.net
'''
                    Largest palindrome product  -   Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

import itertools
import time

def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]


def tuple_to_string(tup):
   if ( type(tup) == tuple ):
      strng = ''.join(map(str, (tup)))
      #print(strng)
      #print('Type of  ',strng,' is:  ',type(strng))
      return strng
   else: print('Not a tuple type !')

def tuple_to_list(tup):
   if ( type(tup) == tuple ):
      lst = [str(i) for i in tup]
      #print(lst)
      #print('Type of  ',lst,' is:  ',type(lst))
      return lst
   else: print('Not a tuple type !')

print('\n=========== My First Solution ===============')

t1 = time.time()

six_digits_polidromes=[]
three_digit_numbers=[x for x in range(100,1000)]
selected_polidromes=[]
#print(three_digit_numbers[0],three_digit_numbers[-1])

ten_digits= list(itertools.permutations([0,1,2,3,4,5,6,7,8,9], 3))      # This takes all 3 elements
print ('There are', len(ten_digits),' unique Permutations between the ten digits :     \n', ten_digits,'\n',type(ten_digits))
print('And this is how you access a sub element from the array ::    ',ten_digits[2][2])

iter=0
for X in ten_digits:
    a= tuple_to_string(X)
    iter +=1
    b = int(a+a[::-1])
    six_digits_polidromes.append(b)
    if iter <3 :
        print(type(b) ,b)

print('-----'*30)

print('Length : ',len(six_digits_polidromes),';   ALL Six digits polidromes : ' ,six_digits_polidromes)

counter = 0
for X in six_digits_polidromes:
    counter += 1
    for Y in three_digit_numbers:
        #if counter  > 1000 :
        if X % Y == 0:
            if (Y <1000 and Y>100 and X//Y < 1000 and X//Y > 100):
                selected_polidromes.append(X)
                #print('Palindrome number :  ', X , ' ;     Factors  :' , Y , X//Y )


#print(selected_polidromes)

GOLD_polidromes = set(selected_polidromes)
print('Just ',len(GOLD_polidromes), 'polidromes')
print('Sorted GOLD Polidromes :  ',sorted(GOLD_polidromes))
print('LARGEST POLIDROME OF PRODUCT OF THREE 3-DIGIT NUMBERS:',sorted(GOLD_polidromes)[-1],'            !!!!!!')

print('There were found :   ',len(GOLD_polidromes),'  polidromes numbers formed from six digits with both factors : 100 < nr < 1000')

t2  = time.time()
print('\nCompleted in :', round((t2-t1),3), 's')               #My solution was Completed in :  218.01257133483887 ms

#################################
print('===='*30)


print('\n=========  OTHER SOLUTIONS FROM EULER FORUM ===============')
t1 = time.time()

for i in range(900,1000):
    for j in range(900,1000):
        x = str(i*j)
        if x == x[::-1]:
            tmp = x
print(tmp)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),3), 's')

# THE FASTEST SOLUTION !! INCREDIBLE !!!!!!!!!!         Completed in : 15.00082015991211 ms

#################################
t1 = time.time()

palindrome=0
for i in range(100,1000):
    for j in range(100,1000):
        if str(i*j)==str(i*j)[::-1] and i*j>palindrome:
            palindrome=i*j
print(palindrome)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),3), 's')
##############################

# Simple Python code, and executed about 0,5 s
t1 = time.time()

table = []
for i in range (999,100,-1):
	for x in range (999,100,-1):
		if str(x*i) == str(x*i)[::-1]:
			table.append(x*i)
print (max(table))

t2  = time.time()
print('\nCompleted in :', round((t2-t1),3), 's')
################################
t1 = time.time()

print(max([i * j for i in range(100,1000) for j in range(100,1000) if str(i*j) == str(i*j)[::-1]]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1),3), 's')
####################################

print('\n ---------------------  Pathetic METHOD using for loops-----------------')

t1 = time.time()

def largestPal():
    for a in range(9,-1,-1):
        for b in range(9,-1,-1):
            for c in range(9,-1,-1):
                for i in range(100, 1000):
                    num = 100001*a + 10010*b + 1100*c
                    if num % i == 0 and num / i > 99 and num / i < 1000:
                        return num

print(largestPal())

t2  = time.time()
print('\nCompleted in :', round((t2-t1),3), 's')

print('------'*30)
# SECOND FASTEST METHOD !           Completed in : 64.00346755981445 ms

####################################
t1 = time.time()

lst = []
for i in range(999,100, -1):
  for j in range(999,100, -1):
    num = str(i*j)
    if num == num[::-1]: lst.append(int(num))
print (max(lst))

t2  = time.time()
print('\nCompleted in :', round((t2-t1),3), 's')

################################