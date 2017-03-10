#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Connectedness of a network      -       Problem 186
Here are the records from a busy telephone system with one million (10**6)  users:

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
import time, itertools, zzz
from collections import deque

def Lagged_Fibonacci_Generator_gen():           # EFFICIENT GENERATOR
    '''    For 1 ≤ k ≤ 55, Sk = [100003 - 200003*k + 300007*k**3] (modulo 1000000)
            For 56 ≤ k, Sk = [S_(k-24) + S(k-55)] (modulo 1000000)                      '''
    from collections import deque
    queue_55 = deque()    
    for k in range(1,56) :
        s = (100003 - 200003*k + 300007*k**3) % 1000000
        # print(k, s)        
        queue_55.append(s)        
        yield s
    while True :
        s = (queue_55[-24]+queue_55[-55])%1000000        
        queue_55.append(s)
        queue_55.popleft()
        # print(len(tmp) ,tmp)
        yield s


print('\n---------------- TESTS ---------')

########   NOT MY CODE. But I can Inspire from it
# def generator():
#     queue_55 = deque()
#     queue_24 = deque()
#     for k in range(1, 56):
#         s_k = (100003 - 200003 * k + 300007 * (k ** 3)) % 1000000
#         queue_55.append(s_k)
#         if k >= 32:
#             queue_24.append(s_k)
#         yield s_k
#     while True:
#         s_k = (queue_55.popleft() + queue_24.popleft()) % 1000000
#         queue_55.append(s_k)
#         queue_24.append(s_k)
#         yield s_k
#
# G = generator()
# cnt = 0
# for i in G :
#     print(i , next(G))
#     cnt+=1
#     if cnt ==100 : break
#
#
# graph_list = [set([i]) for i in range(1000000)]
#
# def get_pos_of(i):
#     while isinstance(graph_list[i], int):
#         i = graph_list[i]
#     return i

print('\n---------------- Test to find the call number of PM ---------')

t1  = time.time()

def first_call_number_of_PM() :
    LFG = Lagged_Fibonacci_Generator_gen()
    PMnr  = 524287
    TS = set()              # TS = Tracker SET
    for i in range(1, 2*10**7+1):
        n1, n2 = next(LFG), next(LFG)
        TS.update({n1,n2})
        if ( n1 or n2 ) == PMnr  :       # call Id :  2575194.      n1=  524287         n2=  974071           Total Nrs : 	 994204
            return print('call Id :  '+str(i)+'.      n1= ', n1, '        n2= ', n2, '          Total Nrs : \t', len(TS) )

# first_call_number_of_PM()

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def first_attempt() :
    LFG = Lagged_Fibonacci_Generator_gen()
    PMnr , PMnr_id = 524287, 33.33
    PMnr_conn = 0
    NET = []
    TS = set()              # TS = Tracker SET
    for i in itertools.count(1) :
        # if i == 564 : break                   # Controller over the infinite loop
        n1, n2 = next(LFG), next(LFG)

        # CASE 0 - Miss dialled
        if n1 == n2 : continue

        #  CASE 1       -   # FIRST NUMBER - DIALLER, Second not in NET
        if ( n1 in TS ) and (n2 not in TS) :
            for j in range(len(NET)) :
                if n1 in NET[j] :
                    NET[j].add(n2)
                    break

        #  CASE 2       -   # Both are already in Network
        if (n1 in TS) and (n2 in TS ) :
            m1, m2 = None, None
            for j in range(len(NET)) :
                if n1 in NET[j] : m1 = j
                if n2 in NET[j] : m2 = j
                if (m1 and m2) != None : break
            tmp_set = NET[m1].union(NET[m2])

            if m1 > m2 :   NET.pop(m1) ;   NET.pop(m2)
            if m1 < m2 :   NET.pop(m2)  ;  NET.pop(m1)
            if PMnr in tmp_set :                     # We assure that the PM_nr_id    IS NOT changed        !!!
                NET.insert(tmp_set)
                print(len(tmp_set),'         ', tmp_set  )
            else : NET.append(tmp_set)

            # print(len(tmp_set),'\t\t\t', tmp_set)

        #  CASE 3       -       # SECOND NUMBER - CALLED, First not in NET
        if ( n2 in TS ) and ( n1 not in TS ) :
            for j in range(len(NET)) :
                if n2 in NET[j] :
                    NET[j].add(n1)
                    break

        #  CASE 4           # Both numbers are NOT in TS ( Tracker Set )
        if (n1 not in TS) and (n2 not in TS ) :
            NET.append({ n1,n2 } )

        TS.update({n1, n2})

        # SPECIAL CASE - Prime Minister
        if PMnr in TS :             # PRIME MINISTER Connections handle
            if PMnr_id != 0 :      # We move the set of the Prime Minister to the 0 index in the list
                for j in range(len(NET)) :
                    if PMnr in NET[j] :
                        A = NET[j]
                        NET.pop(j)
                        NET.insert(A )
                        PMnr_id = 0
                        print('\n++++++  ', NET[0], '   Total phone numbers : ',len(TS),'  ++++++' )
                        break
            elif PMnr_id == 0 :
                PMnr_conn = len(NET[0])
        if i%10**4 == 0 :
            print('call Id :  '+str(i)+'.     Dialler :', n1, '       Called : ', n2, '      Total Nrs : \t', len(TS) , '      Groups : ', len(NET) , '      fragmentation :\t', round( len(NET)*2/len(TS) ,6), '\t\t', len(TS)-2*len(NET ) )

        # print(len(NET), NET)


        if PMnr_conn >= ( 99 * len(TS) )/100 :
            return print( '\nCalls : \t', i, '\t\t PM conn : \t', PMnr_conn, '    Total nrs :   ', len(TS) )





t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60,6), 'min\n\n')



 ############ UNDERSTANDING THE PROBLEM #############
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


print('\n==========  My FIRST SOLUTION, With Help  , 30 sec ===============\n')
t1  = time.time()

# ============    @ 2017-03-09, 19:26  ===============
#Couldn't have done it without OBVIOUS HELP from the internet !!! In effect my solution
# would take 1 day to finish and the response would have been wrong as I did not took into account
# correctly the 1.000.000 users comparison and I would have compared with the numbers dialed.async
# But at least I learnt something very important about sets and some nice tricks like the get_position_of
# deque and so on. It this is more important !

def get_position_of( list_of_sets , b):
    while isinstance( list_of_sets[b] , int ) :
        b = list_of_sets[b]
    return b

def calls_number_solution() :
    LFG = Lagged_Fibonacci_Generator_gen()
    PMnr = 524287
    calls = 0
    NET = [ set([i]) for i in range( 10**6) ]

    TS = set()              # TS = Tracker SET
    for i in itertools.count(1) :
        # if i == 15938 : break                   # Controller over the infinite loop
        # if i == 15 : break                   # Controller over the infinite loop
        n1, n2 = next(LFG), next(LFG)
        if n1 == n2 : continue
        calls +=1
        TS.add(n1); TS.add(n2)
        pos1 = get_position_of(NET, n1)
        pos2 = get_position_of(NET, n2)

        if pos1 != pos2 :
            to_put_into = min(pos1, pos2)
            to_remove = max(pos1, pos2)
            NET[to_put_into] |= NET[to_remove]
            NET[to_remove] = to_put_into

        if i%10**5 == 0 :
            print('call Id :  '+str(i)+'.     Dialler :', n1, '       Called : ', n2, '    positions :', pos1, pos2 ,'    Total Nrs : \t', len(TS) ,'    Calls :', calls )
            # print('       ' ,NET[187853: 187857],'    ' ,NET[ 909800:909805],'       ' ,NET[150341:150345])

        PMnr_set_len = len(NET[get_position_of(NET,  PMnr)]  )
        if PMnr_set_len >= 990000 :
            return print( '\nCalls : \t', calls , '\t\t PM conn : \t', PMnr_set_len, '    Total nrs :   ', len(TS) )


calls_number_solution()         #       Calls : 	 2325629 , PM conn : 	 990000     Total nrs :    990458



t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')
zzz.Star_Wars()

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
