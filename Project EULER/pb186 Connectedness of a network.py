#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Connectedness of a network      -       Problem 186
Here are the records from a busy telephone system with one million users:

                                RecNr	    Caller	    Called
                                    1	        200007	    100053
                                    2	        600183	    500439
                                    3	        600863	    701497
                                ...	...	...
The telephone number of the caller and the called number in record n are :
Caller(n) = S_(2n-1) and Called(n) = S_2n where S_1,2,3,... come from the "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, Sk = [100003 - 200003*k + 300007k**3] (modulo 1000000)
For 56 ≤ k, Sk = [S_(k-24) + S(k-55)] (modulo 1000000)

If Caller(n) = Called(n) then the user is assumed to have miss dialled and the call fails; otherwise the call is successful.

From the start of the records, we say that any pair of users X and Y are friends
if X calls Y or vice-versa. Similarly,
X is a friend of a friend of Z if X is a friend of Y and Y is a friend of Z;
and so on for longer chains.

The Prime Minister's phone number is 524287.
After how many successful calls, not counting misdials,
will 99% of the users (including the PM) be a friend, or a friend of a friend etc., of the Prime Minister?

'''
import time

def Lagged_Fibonacci_Generator_gen():           # EFFICIENT GENERATOR
    '''
    For 1 ≤ k ≤ 55, Sk = [100003 - 200003*k + 300007*k**3] (modulo 1000000)
    For 56 ≤ k, Sk = [S_(k-24) + S(k-55)] (modulo 1000000)
                                                                                                            '''
    tmp=[]
    for k in range(1,56) :
        s = (100003 - 200003*k + 300007*k**3) % 1000000
        # print(k, s)
        tmp.append(s)
        yield s
    while True :
        s = (tmp[-24]+tmp[-55])%1000000
        tmp.append(s)
        tmp.pop(0)
        # print(len(tmp) ,tmp)
        yield s

t1  = time.time()

LFG = Lagged_Fibonacci_Generator_gen()

for i in range(1, 2*10**7+1):
    n = next(LFG)
    print(str(i)+'.     ', n)
    if n == 524287 : break              # 3681162.      524287


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------TESTS------------------------------')

# It's 99% of the one million users. The list of calls is infinite.
# You're asked how much of that infinite list you need to look at before 99% ' \
# of the users are connected to the PM (either directly or indirectly).
#
# For example, suppose there are five users, and the calls go
#
# CODE: SELECT ALL
# (misdial) 4,4
# 1: 1,4
# 2: 2,4
# (misdial) 3,3
# (misdial) 1,1
# 3: 5,4
# 4: 3,2
# (misdial): 2,2
# 5: 3,4
#
# After the first two successful calls, user 5 is still not connected to anyone.
# After the third, they are connected to users 4 (directly, because of call 3),
# 1 (because 1 is connected to 4 by call 1),
# 2 (because 2 is connected to 4 by call 2),
# and 5 (because 4 is a friend of 5, and 5 is a friend of 4,
# that makes 5 a friend of a friend of 5).
# At this point, user 5 is connected to 4 out of the 5 users, which is 80%.
#
# If we were asked how many successful calls it took for user 5 to be connected to 80% of the users, the answer would be 3.




print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()

















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
