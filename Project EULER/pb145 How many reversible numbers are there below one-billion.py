#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Mon, 12 Dec 2016, 00:00
#The  Euler Project  https://projecteuler.net
'''
How many reversible numbers are there below one-billion?        -       Problem 145

Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits.

For instance, 36 + 63 = 99 and 409 + 904 = 1313.

We will call such numbers reversible;   so 36, 63, 409, and 904 are reversible.

Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10**9)?

'''
import time


print('\n--------------------------TESTS------------------------------')



print('\n================  My FIRST SOLUTION,  BRUTE FORCE, 10 min ===============\n')
t1  = time.time()

# N = [1, 2]
# from itertools import count
# while True :
#     for i in range(len(N), 0, -1):
#         if N[0] % 2 == 0 and N


def brute_force() :
    cnt=0
    for m in range(11, 10**8, 2):
        r = int(str(m)[::-1])
        o = [ int(i) for i in str(m+r)   ]
        counter+=1
        if counter %10**7 == 1 : print(counter)
        even  = [ i for i in o if i%2 ==0]
        if len(even) ==0 and str(m)[-1] != '0' :
            cnt+=1
            print(str(cnt)+'.    ',  m, r, '     ',o)

    return print('\nAnswer : ', cnt*2)           #     Answer : 608720

# brute_force()

# RANGES :  7 digits : 50000
# RANGES :  6 digits : 18000
# RANGES :  5 digits : 0
# RANGES :  4 digits : 600
# RANGES :  3 digits : 100
# RANGES :  2 digits : 20



# Answer :  304360 * 2






t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')            # Completed in : 654070.410728 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')

############# IDEAS #############
# I solved this problem with pencil and paper
# I found that
# p(2*n)=20*30^n-1
# p(3)=100
# p(5)=0
# p(7)=20^2*25*5
# p(9)=0
# where p(n) is the number of reversible numbers having n digits

print('\n--------------------------SOLUTION 1, VERY FAST, PATTERN RECOGNITION, mhb038  --------------------------')
t1  = time.time()
# =========   Mon, 14 Nov 2016, 18:08, mbh038, England
# I got there in the end without brute force, in well under 1 ms, by looking at the constraints on digit pairs
# for 2....9 digit solutions, much as many others have done on this thread.
# However i cannot claim to have spotted these constraints from the outset.
# I first used brute force for 1...9 digit candidates and looked for patterns, then worked out the why of these patterns afterwards.

def p145():

    solutions=0
#n=1,5,9 - no solutions, since this would require that twice the middle digit be an odd number
#n=2,4,6,8 - ab,abcd etc: No digit sums can carry, all digit sums must be odd
    #end digits cannot be zero
    end=len([x+y for x in range(1,10) for y in range(1,10) if x+y<10 and (x+y)%2]) #20
    #other digits can be zero
    middle=len([x+y for x in range(0,10) for y in range(0,10) if x+y<10 and (x+y)%2]) #30
    for n in [2,4,6,8]:
        solutions+=end*middle**(n//2-1)
#n=3 : abc: a+c must be odd, a+c>9,b<6
    d13=len([x+y for x in range(1,10) for y in range(1,10) if x+y<10 and (x+y)%2]) #20
    d2=5
    solutions+=d13*d2
#n=7: abcdefg :  a+g must be odd and >10; b+f must be even, b+f<10, d<6
    d17=len([x+y for x in range(1,10) for y in range(1,10) if x+y<10 and (x+y)%2]) #20
    d26=len([x+y for x in range(0,10) for y in range(0,10) if (x+y)%2==0 and x+y<10]) #25
    d35=len([x+y for x in range(0,10) for y in range(0,10) if (x+y)%2==1 and x+y>10]) #20
    d4=5

    solutions+=d17*d26*d35*d4

    print(solutions,)


p145()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, BRUTE FORCE  --------------------------')
t1  = time.time()
# ===========  Mon, 14 Nov 2016, 18:08, mbh038, England
# This is the brute-force-ish solution I used to find the solutions with n-digits.
# It makes just a few exclusions and finds all solutions up to n=108n=108 in 140s.

def p145bf(n):

    rev=0
    for n in range (10**(n-1),10**n):
        flag=True
        if not n%10:
            continue
        nrev=int(str(n)[::-1])
        if n%2 == nrev%2:
            continue
        ns=n+nrev
        while ns>1:
            if not ns%2:
                flag= False
            ns=ns//10
        if flag:
            rev+=1
    print(rev)

# p145bf(10**8)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  INSTANT, MUCH LEARN HERE --------------------------')
t1  = time.time()

# ========== Thu, 24 Sep 2015, 23:43, j123, Canada
#
# The following code should explain better what is happening: to determine whether a number is reversible,
# we peel off a single digit from each end.  Either these two digits carry when they add or they don't.
# Either case forces the possibilities of the next-to-outside digits, and so forth.
# Finally, in the middle, we need either no or a single digit remaining.
# So the count of reversible numbers with i digits is easily done, and adding them up gives the answer.


def do(n = 9):
    '''Find 'reversible' numbers below 10**n'''
    sums = [(a, b, a + b) for a in range(10) for b in range(10)]
    odd_no_carry_init = sum([1 for a, b, s in sums   if s < 10 and s % 2 == 1 and a > 0 and b > 0])
    odd_carry_init = sum([1 for a, b, s in sums  if s >= 10 and s % 2 == 1 and a > 0 and b > 0])
    odd_no_carry = sum([1 for _, _, s in sums if s < 10 and s % 2 == 1])
    odd_carry = sum([1 for _, _, s in sums if s >= 10 and s % 2 == 1])
    even_no_carry = sum([1 for _, _, s in sums if s < 10 and s % 2 == 0])
    single_no_carry = len(range(5))
    def ans(i):
        carrying = (odd_carry_init * \
                    (even_no_carry * odd_carry)**((i - 3) // 4) * \
                    single_no_carry) if i % 4 == 3 else 0
        not_carrying = odd_no_carry_init * odd_no_carry**((i - 2) // 2) \
                       if i % 2 == 0 else 0
        return not_carrying + carrying
    return print(sum(ans(i) for i in range(1, n + 1)))

do()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()
# ====== Fri, 3 Oct 2014, 14:45, Karsten, Belgium
# I have noticed that all even-length reversible numbers sum to a palindrome.
# All odd-length reversible numbers sum to 1 followed by a palindrome.
# There aren't that many palindromes with only odd digits under 10**9.
# My solution iterates over all sums, and for every sum calculates how many reversible numbers sum to it.
#
# I found that the number of even-length reversible numbers that sum to a palindrome are about equal to the product
# of the digits+1 (digit-1 for the outer pair as leading/trailing 0's are disallowed).
# For the number of odd-length numbers that sum to 1-palindrome, a similar relation exists. This finds the solution in about 0.02 seconds.



def combpalin(n): # only half the palindrome is taken as input
  res=1
  while n>10:
    res *= n%10+1; n/=10  # digit+1 combinations for this pair
  return res*(n-1)        # digit-1 for the outermost pair

def combcarrypalin(n): # only half the palindrome is input, the 1 in front is dropped
  res=1
  while n>100:
    res *= 9-(n%10); n/=10 # (9-digit) possibilities for this odd pair
    res *= (n%10); n/=10   # digit possibilities for even pairs
  if n<10: return 0
  return res * (9-(n%10))


s=0; i=1
while i <= 9999:          # loop over all palindromes. Only the first half needs to be generated
  s += combpalin(i)
  #print( int(str(i)+str(rev(i))), combpalin(i))
  s += combcarrypalin(i)
  #print( int('1' + str(i)[:-1]+str(rev(i))), combcarrypalin(i))
  i+=2
  if i%2000 == 1: i+=1000
  if i%200 == 1: i+=100
  if i%20 == 1: i+=10

print(s)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
