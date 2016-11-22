#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                                Dice Game       -       Problem 205

Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin?
Give your answer rounded to seven decimal places in the form 0.abcdefg

'''
import time
from random import randint
from itertools import count, permutations, combinations_with_replacement, combinations


print('\n--------------------------AUTOMATED TESTS------------------------------')

print(randint(1,6),'\n')
P = list(permutations([2,1,1,1,1,1],6))
print('Perm Test : ', len(P) ,P)

# p_cnt, c_cnt = 0, 0
# for i in range(1,1000):
#     P = [randint(1,4), randint(1,4), randint(1,4), randint(1,4), randint(1,4), randint(1,4), randint(1,4), randint(1,4), randint(1,4)]
#     C = [randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
#     if sum(P) > sum(C) :
#         p_cnt+=1
#     if sum(P) < sum(C) :
#         c_cnt+=1
#     elif sum(P) == sum(C) :
#         p_cnt += 0.5
#         c_cnt += 0.5
#     print(str(i)+'.     P :  ' , p_cnt/i ,'       C : ' ,c_cnt/i ,  '         P ', P, sum(P),'        C  ',C , sum(C),  '     ',p_cnt/i + c_cnt/i)
#     if i % 1e6 == 0: print(i)
#     # if i == 2e7 :
#     #     print(str(i)+'.     P :  ' , p_cnt/i ,'       C : ' ,c_cnt/i , p_cnt/i + c_cnt/i   , '         P ', P, sum(P),'        C  ',C , sum(C),  '     ',p_cnt/i + c_cnt/i)
#     #     break




# Tried :  P :   0.608528675        C :  0.391471325 1.0,





print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()

total = 5
combinations = [1] + [0]*total
monies = [1]*(total)

for x in monies:
    for i in range(x,total+1):
        combinations[i] += combinations[i-x]
    print(combinations)

print (combinations[total])

# Must do a recursive function to generate  https://wizardofodds.com/gambling/dice/2/














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
