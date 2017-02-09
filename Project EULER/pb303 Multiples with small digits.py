#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Tue, 31 Jan 2017, 19:44
#The  Euler Project  https://projecteuler.net
'''
                    Multiples with small digits     -       Problem 303

For a positive integer n, define f(n) as the least positive multiple of n that, written in base 10, uses only digits ≤ 2.

Thus f(2)=2, f(3)=12, f(7)=21, f(42)=210, f(89)=1121222.

Also,               ∑{n=1, 100} f(n) / n = 11363107

Find ,              ∑{n=1, 10000} f(n) / n = ????

'''
import time

def toStr(n, base):
   '''Very elegant. Works Fine.
   '''
   convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg"
   # print(len(convertString))
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print('toStr Function : \t', toStr(43, 3) , type (toStr(43, 3) ), '\n\n')


def get_small_digit_multiple(n):
    # N = [ int(i) for i in str(n) if int(i)<=2 ]
    # if len(N) == len(str(n)) :  return n
    M = [ int(i) for i in str(n) if int(i) >=8 ]
    if len(M) == len(str(n)) :
        if sum(M) / len(M) == 9 :
            return int( str(1)*len(M) +str(2)*4*len(M) )
    if n == 1998 : return 111222222222222
    if n == 2997 or n == 5994 : return 112222221222222
    if n == 3996 : return 121222222222212
    if n == 4995 or n== 9990 : return 1112222222222220
    if n == 6993 : return 122211222222222
    if n == 7992 : return 221222222222112
    if n == 8991 : return 122212222222221
    if n == 9899 : return 11112221222222

    i = 1
    while True :
        x = toStr(i , 3)
        if int(x) % n == 0 : return int(x)
        # print(x, n)
        i+=1

print('\nget_small_digit_multiple :\t', get_small_digit_multiple(99))

print('\n--------------------------INITIAL VERIFICATION TEST------------------------------')
t1  = time.time( )


def small_digits_multiple(n):
    N = [ int(i) for i in str(n) if int(i)<=2 ]
    if len(N) == len(str(n)) :  return n
    l = len(str(n))
    m = n
    while n < 10**l :
        n+=n

    M = [ int(i) for i in str(n) if int(i) >=8 ]
    if len(M) == len(str(n)) :
        if sum(M) / len(M) == 9 :
            return int( str(1)*len(M) +str(2)*4*len(M) )
    #     if sum(M) / len(M) > 8 :
    #         l = M.count(9)*4+1

    up_rng = 2.3
    while True :
        n0 = pow(10,l) + n - pow(10, l, n)
        print(n0, l ,'     ' ,n0 / n, '    ', len(str(n0)))

        while n0 < up_rng * 10**l :
            # print(n0)
            N = [ int(i) for i in str(n0) if int(i)<=2 ]
            if len(N) == len(str(n0)) :
                return n0
            n0 += n
        l+=1

# print('small_digits_multiple : \t', small_digits_multiple(25))

# 9 -->  1 2222
# 99  --> 11 2222 2222
# 89  -->112 1222
# 988 --> 222 2012
# 989 --> 112 1220 2012
# 998 --> 1 1122 1112


t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')

print('\n================  My FIRST SOLUTION, 9 min   ===============\n')
t1  = time.time()

def initial_solution(up) :
    S = 0
    for n in range(1, up+1):
        f = get_small_digit_multiple(n)
        x = f // n
        print(str(n)+'.       Multiple = ', f , '              f(n)/n = ',x )
        S+=x

    return print('\n\nAnswer : \t', S)

# initial_solution(10**4)                     #       Answer : 	 1111981904675169


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  22 sec, NICE SOLUTION --------------------------')
t1  = time.time()

# ==== Wed, 31 Dec 2014, 23:10, candells, USA

# I don't normally post comments, but I didn't see others with the same approach and it seems simple.
#
# This code builds up a dictionary of every possible reachable remainder for a given n.
# It starts with one digit numbers, and adds one digit at a time.
# The contents of the dictionary elements is the smallest number (comprised of only 0s,1s,or 2s)
# that has the remainder of the index.
# Before adding the next digit, it simply checks to see if a remainder exists that will cancel the new power of 10,
# or 2x that power (1xxx or 2xxx).
# If it exists, then we're done.
# Otherwise, add any new remainders by working through the whole dictionary.
#
# Runs in about 10sec, with no special cases for 9999

def f012(n):
    reach={ 0:0 }
    p = 1
    while True:
        if -p%n in reach:
            return p+reach[-p % n]
        if -2*p % n in reach:
            return 2*p+reach[-2*p % n]
        #No matches...add any new remainders with an appended 1 or 2
        rl = list(reach)
        for r in rl:
            if (r+p)%n not in reach:
                reach[(r+p)%n]=reach[r]+p
        for r in rl:
            if (r+2*p)%n not in reach:
                reach[(r+2*p)%n]=reach[r]+2*p
        p*=10


# s = 0
# for k in range(1, 10001):
#     s+=f012(k)/k
# print (s)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  4 sec , SUPER FAST --------------------------')
t1  = time.time()

# =====   Mon, 19 Aug 2013, 22:24, Animus, Germany

# Many good approaches to this problem have been posted, here's one more,
# since it's unique and very fast up to the asked for boundary of 10^4.
#
# Much alike Lucy Hedgehog (very well done again!) I implemented a DP algorithm keeping only the
# smallest number for each remainder  and like her I implemented a "man in the middle" approach,
# however very different to her solution:
# While Lucy divides the number into an upper and a lower part,
# I use the fact that every number consisting only of ones and twos (and zeros of course)
# is representable as the sum of two numbers consisting only of ones.
# Therefore I just generate these numbers (growing by the factor of 2 instead of 3 for each digit)
# respective add those with a new remainder in a list until the negative of that remainder
# (-r)%n is found to be alreaddy present in my list, since the sum of both will give the desired remainder of 0.
#
# Runs in 0.4 sec.

def f(n):
    rest = [0] *n
    found = 0
    used = []
    bas = 1
    while not found:
        r = bas % n
        if r == 0:
            found = bas
            break
        lu=len(used)

        if rest[r] == 0:
            used.append(r)
            rest[r] = bas
            cr=(-r)%n
            if rest[cr] > 0:
                found = rest[r] + rest[cr]

        for i in range(lu):
            xr = used[i]
            nr = (xr + r)%n
            if rest[nr] > 0:
                continue
            rest[nr] = bas + rest[xr]
            used.append(nr)
            cr=(-nr)%n
            if rest[cr] > 0:
                if found == 0:
                    found = rest[nr] + rest[cr]
                else:
                    found = min(found, rest[nr] + rest[cr])
        bas *= 10
    return found

su = 0
for i in range(1, 10001):
    su+=f(i)/i
print (su)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, 2 sec,  FASTEST  --------------------------')
t1  = time.time()

# ==== Sun, 26 Sep 2010, 20:13, Lucy_Hedgehog. Switzerland
# I'm also keeping the smallest integer for a given remainder.
# Additionaly I'm doing a meet-in-the-middle trick.
# Summing f(i)/i up to 10^5 gives 11118068951730109624.
# And summing f(i)/i up to 10^6 gives 111175300197493765805173


def f(m):
    if m < 3: return m
    k = 0
    # remainders[ r ] is the smallest n, which is composed from at most
    # k digits (0, 1, 2) and which satisfies n % m == r
    remainders = {0:0}
    best = None
    while best == None:
        k += 1
        for i in list(remainders.values()):
            for d in range(3):
                n = 10*i+d
                r = n % m
                if r not in remainders or n < remainders[ r ] :
                    remainders[ r ] = n
        # Find the smallest integer n with at most 2*k digits composed
        # from the digits 0, 1 and 2 which satisfies n % m == 0.
        mult = (-pow(10, k, m))%m
        for r in remainders:
            u = r * mult % m
            if u in remainders:
                n = 10**k * remainders[ r ] + remainders[ u ]
                if best == None or n < best:
                    if n != 0:
                      best = n
    return best

def P303(n=10000):
    return sum(f(i)//i for i in range(1, n+1))

P303()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
