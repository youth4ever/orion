#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
            Prize Strings       -       Problem 191

A particular school offers cash rewards to children with good attendance and punctuality.
If they are absent for three consecutive days or late on more than one occasion then they forfeit their prize.

During an n-day period a trinary string is formed for each child consisting of L's (late), O's (on time), and A's (absent).

Although there are 81 trinary strings for a 4-day period that can be formed, exactly 43 strings would lead to a prize:

OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
LAOO LAOA LAAO

How many "prize" strings exist over a 30-day period?

'''
import time
import itertools

print('\n--------------------------TESTS------------------------------')

marks=[ 'O', 'L' , 'A' ]

C = [p for p in itertools.product(marks, repeat=12)]
print( len(C), C[0:100] )
print(3**30)

cnt = 0
for i in range(len(C)):
    s = ''.join(C[i])
    a = s.find('AAA')
    l = s.count('L')
    # print(a, l, s)
    if a != -1 or l>=2 :
        cnt+=1
        # print(a, l, s)

print('\n', len(C) , len(C)-cnt, cnt)

# 81 : 43 / 38  ;   243 94 /149 ; 729 200 529   ;   2187 418 /1769  ;   6561 861 /5700  ;   19683 1753 17930    ;   59049 3536 55513
# 177147 7077 170070    ;   531441 14071 517370

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()

# Must see if there is a pattern from those numbers















# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
