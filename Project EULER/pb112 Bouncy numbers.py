#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 19 Nov 2016, 15:55
#The  Euler Project  https://projecteuler.net
'''
                                        Bouncy numbers     -   Problem 112
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred,
but just over half of the numbers below one-thousand (525) are bouncy.
In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780
the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
'''
from __future__ import division
import time
from itertools import count


print('\n--------------------------TESTS------------------------------')

# Bouncy number : if neither monotonic increasing or decreasing

n = 9972  #, 9910, 6664, 6662

def bouncy_number_first(n):     # This function works well but it is SLOW
    I =  [ int(str(n)[i]) for i in range(1, len( str(n)) ) if  int(str(n)[i]) >= int(str(n)[i-1]) ]
    D =  [ int(str(n)[i]) for i in range(1, len( str(n)) ) if  int(str(n)[i]) <= int(str(n)[i-1]) ]
    if len(I) == len(str(n))-1 or len(D) == len(str(n))-1 :
        return False
    else : return True


def bouncy_number(n):               # This function works well , is FASTER
    N = str(n)
    Inc, Dec = 0, 0
    for i in range(1, len(N)) :
        if int(N[i-1]) <= int(N[i]):
            Inc = 1
        else :
            Inc =0
            break
    if Inc == 1 : return False
    elif Inc == 0 :
        for i in range(1, len(N)) :
            if int(N[i-1]) >= int(N[i]):
                Dec = 1
            else :
                Dec =0
                break
    if Dec == 1 : return False
    elif Inc == 0 and Dec ==0 : return True

def monotonic_number(n) :
    listN = list(str(n))
    flag1 = False
    flag2 = False
    for i in range(1, len(listN)):
        if listN[i] > listN[i-1]:
            flag1 = True
        if listN[i] < listN[i-1]:
            flag2 = True
    if flag1 == True and flag2 == True:
        return False # print('False . NOT monotonic ! ')
    else : return True # print('True. IS monotonic !')


print('Test for bouncy_number Function :  ', bouncy_number(n),'\n' )        # Functions Tests look good
print('Test for bouncy_number_first Frunction :  ', bouncy_number_first(n),'\n' )        # Functions Tests look good

# AUTOMATED TEST ! DON'T DELETE THEM !!!!!!!!!!!!!!!!!!!!!
print('------------------------------ AUTOMATED TESTS --------------------------')
def automated_test():
    from random import randint
    for i in range(1,200):
        n = randint(101,1e4)
        print(n, '    1-st , 2-nd    : ',bouncy_number_first(n),  bouncy_number(n) )

# automated_test()


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def find_bouncy(percent=0.5):
    bnc = 0
    nonb = 100
    for i in count(101) :
    # for i in range(101,1001) :
    #     if bouncy_number(i) == True :
        if monotonic_number(i) == False :
            bnc+=1
        else :
            nonb+=1
        Pbb =  bnc/( i)
        Pbn =  nonb/( i)
        # print(str(i)+'.   ' ,   bnc, nonb,'      ' ,Pbb,  '     ', Pbn )
        if Pbb == percent and i > 200 :
            print(str(i)+'.   ' ,   bnc, nonb,'      ' ,Pbb,  '     ', Pbn )
            result = i
            break
    return print('\nBouncy : ', bnc,'\nNon-bouncy :  ', nonb, '\nAnswer :  ', result )

if __name__ == '__main__':
    find_bouncy(percent = 0.99 )         # Answer : 1587000


t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')

'''

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, che_sac , USA   --------------------------')
t1  = time.time()

# Time taken - 3.46 secs
# Straight logic, nothing special.
# First check for increasing number,
# then for decreasing number
# If skipped either of those then it's a bouncing number.

def isbouncy(n):
    if n < 100:
        return False
    ns = str(n)
    # 0 - true; 1 - false
    flag = True
    # check for increasing sequence
    for i in range(len(ns)-1):
        if ns[i] <= ns[i+1]:
            pass
        else:
            break
    else:
        flag = False
    # check for decreasing sequence
    for i in range(len(ns)-1):
        if ns[i] >= ns[i+1]:
            pass
        else:
            break
    else:
        flag = False

    return flag

limit = 10000000
n = 1
count = 0
while n <= limit:
    if isbouncy(n):
        count += 1

        if 100 * (count / n) == 99 :
            print('n = {}, count = {}'.format(n,count))
            break
    n += 1


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 2, ggordonhall, Scotland   --------------------------')
t1  = time.time()
# Pretty simple really:

def inc_num(n):
	x = 0
	while x < (len(str(n))-1):
		if str(n)[x]>str(n)[x+1]:
			return False
		x+=1
	return True

def dec_num(n):
	x = 0
	while x < (len(str(n))-1):
		if str(n)[x]<str(n)[x+1]:
			return False
		x+=1
	return True

def bouncy_num(n):
	if inc_num(n)==False and dec_num(n)==False:
		return True
	return False

def prob112():
	x = 100
	b = 0
	while True:
		if bouncy_num(x)==True:
			b+=1
		prop = (b/x)*100
		if prop == 99:
			return x
		x+=1

print (prob112())

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, thehunnybadge, Canada  --------------------------')
t1  = time.time()


def is_bouncy(x):
    if list(str(x)) != sorted(list(str(x))) and list(str(x))[::-1] != sorted(list(str(x))):
        return True

bouncy = 19602
num = 21780
bounciness = 0
while bounciness < 0.99:
    num += 1
    if is_bouncy(num) == True:
        bouncy += 1
    bounciness = float(bouncy)/float(num)
else:
    print (num)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, TheRedBull, Germany  --------------------------')
t1  = time.time()

def bouncy(x):
        x = str(x)
        inc = True
        dec = True
        bouncy = False
        for i in range(len(x)-1):
                if int(x[i+1]) < int(x[i]):
                        inc = False
                elif int(x[i+1]) > int(x[i]):
                        dec = False
        return not inc and not dec


bouncies = 0
i = 0

while True:
        i += 1
        if bouncy(i):
                bouncies += 1
        if bouncies >= 0.99 * i:
                print(i)
                break


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, night.train,   --------------------------')
t1  = time.time()

def check_increasing_number (num):
    num_list = list(str(num))
    for i in range (len(num_list)-1):
        if num_list[i] > num_list[i+1]:
            return 0
    return 1

def check_decreasing_number (num):
    num_list = list(str(num))
    for i in range (len(num_list)-1):
        if num_list[i] < num_list[i+1]:
            return 0
    return 1


num_bouncy = 0
i = 10
tgt_perc = 0.99

while num_bouncy / (i+0.0) < tgt_perc:
    i += 1
    if (check_increasing_number(i) == 0):
        if (check_decreasing_number(i) == 0):
            num_bouncy += 1
print (i)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 6, MagnusRoland, Sweden  --------------------------')
t1  = time.time()

def isIncr(n):
    n = str(n)
    prev_d=0
    for d in n:
        if int(d)<prev_d: return False
        prev_d=int(d)
    return True
def isDecr(n):
    n = str(n)
    prev_d=9
    for d in n:
        if int(d)>prev_d: return False
        prev_d=int(d)
    return True
def isBouncy(n):
    return (isIncr(n)==False and isDecr(n)==False)

tot_bouncy=0
least=1
while (1):
    if isBouncy(least): tot_bouncy+=1
    if tot_bouncy/least==0.99: break
    least+=1
print(least)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

'''

print('\n--------------------------SOLUTION 7, aolea  --------------------------')
t1  = time.time()

count = 100
countBouncy = 0
n = 100
proportion = countBouncy / count

while proportion < 0.99:
    # print(n,proportion)
    n = n + 1
    listN = list(str(n))
    flag1 = False
    flag2 = False
    for i in range(1, len(listN)):
        if listN[i] > listN[i-1]:
            flag1 = True
        if listN[i] < listN[i-1]:
            flag2 = True
    if flag1 == True and flag2 == True:
        countBouncy = countBouncy + 1
    count = count + 1
    proportion = countBouncy/count
print(n)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


