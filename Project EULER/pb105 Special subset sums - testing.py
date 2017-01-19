#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Fri, 6 Jan 2017, 21:42
#The  Euler Project  https://projecteuler.net
'''
Special subset sums: testing        -       Problem 105

Let S(A) represent the sum of elements in set A of size n.
We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

1.      S(B) ≠ S(C); that is, sums of subsets cannot be equal.
2.      If B contains more elements than C then S(B) > S(C).

For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84,
whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair combinations and S(A) = 1286.

Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets containing
seven to twelve elements (the two examples given above are the first two sets in the file),
identify all the special sum sets, A1, A2, ..., Ak, and find the value of S(A1) + S(A2) + ... + S(Ak).

NOTE: This problem is related to Problem 103 and Problem 106.

'''
import time
from itertools import combinations

filename = "pb105_sets.txt"
def load_file(filename):
    with open(filename) as f:
        matrix = [list(map(int, line.split(","))) for line in f.readlines()]
    f.close()
    return matrix

print(load_file(filename ))

def isSpecialSumSet(s):
    uSet = set(s)
    for i in range(2,len(s)):
        maxSet = max(uSet)
        for a in combinations(s, i):
            ss = sum(a)
            if ss <= maxSet or ss in uSet: return False
            else: uSet.add(ss)
    return True


F = load_file(filename )

print('\n--------------------------TESTS------------------------------')




print('\n================  My FIRST SOLUTION,  VERY FAST, 40 ms ===============\n')
t1  = time.time()

def solution_pb105() :
    cnt , Set_sum = 0, 0
    for i in range(len(F)):
        S = F[i]
        if isSpecialSumSet(S) == True :
            cnt+=1
            Set_sum += sum(S)
            print(str(cnt)+'.   '  ,S)

    return print('\nAnswer : \t', Set_sum )

solution_pb105()                #   Answer : 	 73702

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')                  #       Completed in : 49.002647 ms





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
