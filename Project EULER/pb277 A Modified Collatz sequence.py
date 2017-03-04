#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Tue, 21 Feb 2017, 11:25
#The  Euler Project  https://projecteuler.net
'''
A Modified Collatz sequence         -           Problem 277

A modified Collatz sequence of integers is obtained from a starting value a_1 in the following way:

a_(n+1) = a_n/3 if a_n is divisible by 3. We shall denote this as a large downward step, "D".

a(n+1) = (4a_n + 2)/3 if a_n divided by 3 gives a remainder of 1. We shall denote this as an upward step, "U".

a_(n+1) = (2a_n - 1)/3 if a_n divided by 3 gives a remainder of 2. We shall denote this as a small downward step, "d".

The sequence terminates when some an = 1.

Given any integer, we can list out the sequence of steps.
For instance if a1 = 231, then the sequence {a_n}={231,77,51,17,11,7,10,14,9,3,1} corresponds to the steps "DdDddUUdDD".

Of course, there are other sequences that begin with that same sequence "DdDddUUdDD....".
For instance, if a1=1004064, then the sequence is DdDddUUdDDDdUDUUUdDdUUDDDUdDD.
In fact, 1004064 is the smallest possible a1 > 10**6 that begins with the sequence DdDddUUdDD.

What is the smallest a1 > 10**15 that begins with the sequence "UDDDUdddDDUDDddDdDddDDUDDdUUDd"?

'''
import time


S= "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
# D --> mod 0
# U --> mod 1
# d --> mod 2

def Collatz_gen( n , seq ):
    A = [n]
    for s in seq  :
        if s == 'D' :          # if n%3 ==0 :  # D --> mod 0
            n= n//3
        if s == 'U' :           #n%3 == 1 :       # U --> mod 1
            n =  (4*n+2)//3
        if  s == 'd' :        # n%3 == 2 :       # d --> mod 2
            n= (2*n-1)//3
        # print(s ,'  =', n, end='   ')
        A.append(n)

    return A


def Inverse_Collatz_seq(n, seq) :
    A = [n]
    for s in seq[::-1] :

        if s == 'D' :       #mod 0
            n = n*3
            A.append(n)
        if s == 'U' :       # mod 1
            if  ((3*n-2)/4) %1 == 0 :
                n = (3*n-2)//4
                A.append(n)
            else : break
            # else :
            #     while ( (3*n-2)/4 ) %1 != 0 :
            #         if  ((3*n-2)/4) %1 == 0 :
            #             n = (3*n-2)//4
            #             break
            #         n -= 1

        if s == 'd' :     #  mod 2
            if  ( (3*n+1)/2 ) % 1 == 0 :
                n = (3*n+1)//2
                A.append(n)
            else : break
            # else :
            #     while ( (3*n+1)/2 ) %1 != 0 :
            #         if  ( (3*n+1)/2 ) % 1 == 0 :
            #             n = (3*n+1)/2
            #             break
            #         n+=1

        # print(s, ' = ', n, end=' ;  ')

    return A

S1 = "DdDddUUdDD"
S = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
S2 = "DdDddUUdDDDdUDUUUdDdUUDDDUdDD"

# {231, 77, 51, 17, 11, 7, 10, 14, 9 ,3 , 1}

print('\nInverse_Collatz_seq : \t', Inverse_Collatz_seq(1, S1 ))
print('\nInverse_Collatz_seq : \t', len(Inverse_Collatz_seq(1, S2 )) , Inverse_Collatz_seq(1, S2 ) )



print('\nCollatz_gen : \t', Collatz_gen(231, S1 ))
print('\nCollatz_gen : \t', Collatz_gen(1125977393124310, S ))


# n = 231
# print(n,end='  ')
# for i in range(30-1):
#
#     n = Collatz_gen(n)
#     print(n, end='   ')





print('\n--------------------------TESTS------------------------------')
t1  = time.time()



#### DIRECT METHOD, Using Straight Collatz Sequence : , Painstakingly SLOW
def direct_method(n=10**15+10**8+10**5) :
    while True :
        D = Collatz_gen(n, S )
        if len(D) == len(S) +1:
            print(str(n)+'.         digits : ', len(str(D[0])) , '        ' ,  D[0] , '         ' ,D[-1] )
            if D[-1] > 10**15 :
                if D[-1] < c_min :
                    c_min = D[-1]
                    print('\n -----  new answer :    ', c_min ,'\n' )
        n+=1






t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

S= "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
print(len(S),'       Sequence String ',S,'\n')

def solution_inverse_Collatz(n ) :
    c_min=10**20
    while True :
        C = Inverse_Collatz_seq(n, S )
        if len(C) == len(S)+1 :
            print(str(n)+'.         digits : ', len(str(C[-1])) , '        ' ,C[-1],'       ', C )
            if C[-1] > 10**15 :
                if C[-1] < c_min :
                    c_min = C[-1]
                    return print('\nAnswer :    ', c_min ,'\n' )
        n+=1


solution_inverse_Collatz(22*10**6)    #   Answer :      1125977393124310

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  INSTANT --------------------------')
t1  = time.time()

# ==== Tue, 8 Nov 2016, 07:22, Satoiji, MExico
# I don't know how to explain what I did, but glad it worked. Found a weird pattern and did my best to "use" it.
#
# done this in python, works in 0.0199999809265 s

#0 -> An / 3
#1 -> 4An + 2 / 3
#2 -> 2An - 1 / 3
def sequence(num, secSteps, nexts):
    if nexts == len(secSteps):
        return True
    if num == 1: return False
    if num % 3 == 0:
        if secSteps[nexts] == 'D':
            return sequence(num / 3, secSteps, nexts+1)
        else: return False
    elif num % 3 == 1:
        if secSteps[nexts] == 'U':
            return sequence((4*num + 2) / 3,secSteps,nexts+1)
        else: return False
    elif num % 3 == 2:
        if secSteps[nexts] == 'd':
            return sequence((2*num - 1) / 3,secSteps,nexts+1)
        else: return False

count = 1000000000000000
cad = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
potencia = 0
increment = 3
matriz = []
while True:
    if potencia == len(cad): break
    if sequence(count,cad[:potencia+1],0):
        potencia+=1
        matriz.append(count)
    count+=increment**potencia
for num in matriz:
    if sequence(num,cad,0):
        print (num)
        break

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ==== Sun, 13 Sep 2015, 23:46, mmaximus, Portugal
# I went for a modular arithmetic approach. Working backwards, you work out what the last step is mod 3,
# then you pass it up to work out what the previous step is mod 3**2, then the previous step mod 3**3,
# all the way to working out what a1 is mod 3**len(string).
#
# Then you find the nearest number to the starting point (10**15) that has that remainder mod 3**len(string) and you're done.

def xgcd(a, b):
    if b == 0:
        return [1, 0, a]
    else:
        x, y, d = xgcd(b, a % b)
        return [y, x - (a // b) * y, d]

def mod_inv(a,b):
    return xgcd(a,b)[0] % b

def apply(arg, fxn):
    return [fxn[0]*arg[0], fxn[0]*arg[1]+fxn[1]]

def solve(lhs, rhs):
    return [rhs[0], mod_inv(lhs[0], rhs[0])*(rhs[1]-lhs[1]) % rhs[0]]

#              in,    out
FMAP = {'d': [[3,2], [2,1]],
        'U': [[3,1], [4,2]],
        'D': [[3,0], [1,0]]
}

def munge(string):
    s = string[::-1]
    for i in range(len(s)-1):
        yield [FMAP[s[i+1]][1], FMAP[s[i]][0]]
    yield [[1,0], FMAP[s[-1]][0]]


initial = [1,1]

for t in munge('UDDDUdddDDUDDddDdDddDDUDDdUUDd'):
    initial = solve(t[0], apply(initial, t[1]))

a1 = 10**15
print(a1 + (initial[0] - (a1 % initial[0]) % a1) + initial[1])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ====Sat, 18 Jan 2014, 02:00, dswenson, USA
# Worked right-to-left in the given string, and kept track of the remainder and the modulus at each step.
# The modulus increases by a factor of 3 at each step, and the remainder is re-calculated at each step
# by solving for a_n−1a in terms of a_n (a linear equation in modular arithmetic).
# This requires finding modular inverses for 2 or 4, modulo various powers of 3, which is explained here,
# but I just used the Python module gmpy2 to find the inverses.
#
# Then at the end, adjust the remainder if necessary to make it greater than the lower bound.
#
# No searching required at any stage!

import gmpy2

limit = 10**15
S = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"

def euler_277(string,limit):
	c=string[-1]
	modulus = 3
	if c=='D':
		r=0
	elif c=='d':
		r=2
	else:
		r=1
	i=len(string)-2
	while i>=0:
		c=string[i]
		i-=1
		modulus*=3
		if c=='d':
			r=((3*r+1)*gmpy2.invert(2,modulus))%modulus
		elif c=='D':
			r *= 3
		else:
			r=((3*r-2)*gmpy2.invert(4,modulus))%modulus
	r = limit-(limit%modulus)+r
	if r < limit:
		r+=modulus
	return r

euler_277(S,limit)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# === Mon, 10 Mar 2014, 21:28, marijan, Croatia


t="UDDDUdddDDUDDddDdDddDDUDDdUUDd"
v={0:"D",1:"U",2:"d"}
def coll(n):
    c=""
    while n>1:
        m=n%3
        if m==1: n=4*n+2
        elif m==2: n=2*n-1
        n/=3
        c+=v[m]
    return c+v[1]

n=1
m=3
for l in range(2,len(t)+1):
    while t[:l]!=coll(n)[:l]:
        n+=m
    m*=3
    print (l,n,m,t[:l])
while n<10**15:
    n+=m
print (n)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

