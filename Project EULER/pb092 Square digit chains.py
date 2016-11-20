#!/usr/bin/python
# Solved by Bogdan Trif @ Completed on Wed, 21 Sep 2016, 20:45
#The  Euler Project  https://projecteuler.net
'''
Square digit chains        -        Problem 92
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
For example,
44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
How many starting numbers below ten million will arrive at 89?
'''
import time
t1  = time.time()
print('------------------MY SOLUTION ------------------------')

eighty_nines=[14, 16, 17, 20, 25, 29, 30, 34, 37, 40, 42, 50, 53, 58, 61, 65, 73, 85, 89]
ones = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103,
            109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230,
            236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331,
            338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440,
            446, 464, 469, 478, 487, 490, 496, 536, 556, 563, 565, 566, 608, 617, 622, 623,
            632, 635, 637, 638, 644, 649, 653, 655, 656, 665, 671, 673, 680, 683, 694, 700,
            709, 716, 736, 739, 748, 761, 763, 784, 790, 793, 802, 806, 818, 820, 833, 836,
            847, 860, 863, 874, 881, 888, 899, 901, 904, 907, 910, 912, 913, 921, 923, 931,
            932, 937, 940, 946, 964, 970, 973, 989, 998]
chosen_ones=[]




counter =1
for i in range(1,10000000):
    #print('\n----------',i,'-----------')
    a,b,c,d,e,f,g,h = 0,0,0,0,0,0,0,0
    for j in str(i):
        a += int(j)**2
    for x in ones:
        if x == a: chosen_ones.append(i)
    #print (str(counter)+'.  ',a, end='   ')
    counter+=1

''''''
'''
    for k in str(a):
        b +=  int(k)**2
    for y in ones:
        if y == b: chosen_ones.append(i)
    print (b, end='   ')

    for l in str(b):
        c +=  int(l)**2
    for w in ones:
        if w == c: chosen_ones.append(i)
    print (c, end='   ')


    for m in str(c):
        d +=  int(m)**2
    for w in ones:
        if w == d: chosen_ones.append(i)
    print (d, end='   ')
    for n in str(d):
        e +=  int(n)**2
    for w in ones:
        if w == e: chosen_ones.append(i)
    print (e, end='   ')
    for o in str(e):
        f +=  int(o)**2
    for w in ones:
        if w == f: chosen_ones.append(i)
    print (f, end='   ')
    for p in str(f):
        g +=  int(p)**2
    for w in ones:
        if w == g: chosen_ones.append(i)
    print (g, end='   ')
'''

chosen_ones_set = set(sorted(chosen_ones))
chosen_ones = sorted(list(chosen_ones_set))
lngth = len(chosen_ones)

#print('\n'*2,chosen_ones)
print('\n'*2,'Length :',lngth, '   ',chosen_ones[-5:-1])

print('\nEighty-nines are : ', 10000000-lngth-1)            #  There are :  8581146    numbers which end in 89

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')      #  Completed in : 391754.4069 ms



print('\n================  OTHER SOLUTIONS FROM THE EULER FORUM  ==================')
print('-------------------SOLUTION 1  - REALLY FAST SOLUTION - WOW, by Sandamnit USA  -----------------------------')
'''
The key observation here is that the sum of the squares of the digits remains invariant under rearrangement.
That said, it suffices to generate all weakly increasing sequences of digits 0-9.
For each sequence, compute the sum of squares, and determine the terminal value of the chain.
 If 1, skip this sequence; otherwise, determine the number of rearrangements, and add this value to a running tally.
When the program terminates, you have your answer.
'''
t1  = time.time()

sqr = [ n**2 for n in range(10) ]
fac = [ 1, 1, 2, 6, 24, 120, 720, 5040 ]
term = [0]*568
term[1] = 1
term[89] = 89

def frequency(S):
   f = [1]
   for n in range(1,len(S)):
      if S[n] == S[n-1]: f[-1] += 1
      else: f += [1]
   return f

def chain(n):
   if term[n] > 0: return term[n]
   term[n] = chain(sum([ int(c)**2 for c in str(n) ]))
   return term[n]

def count89(S=[]):
   if len(S) == 7:
      value = sum([ sqr[n] for n in S ])
      if value == 0 or chain(value) != 89: return 0
      freq = frequency(S)
      count = fac[7]
      for n in freq: count //= fac[n]
      return count

   start = S[-1] if len(S) > 0 else 0
   count = 0
   for n in range(start,10):
      count += count89(S + [n])
   return count

print(count89())
t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')                 # Completed in : 148.0086 ms

print('\n-------------------SOLUTION 2  - INCREDIBLE FAST , by markus.obi, Germany -----------------------------')
'''
After programming a naive (working but slow) approach, which searched the whole range 1..10^7,
I also reduced the search space to exclude permutations.
Python's itertools.combinations_with_replacement comes in really handy.
The second optimization (inspired by Sandamnit) was to precalculate all possible digit sums, which end in 89.
Since there are only 9^2 * 7 = 567 different sums, the precalculation takes only about a millisecond.
'''
import itertools
import math

def square_digit_sum(n):
    sum1 = 0
    while n != 0:
        digit = n % 10
        n //= 10
        sum1 += digit * digit
    return sum1

def chain_ending(n):
    while n not in (1, 89):
        n = square_digit_sum(n)
    return n

def powerful_digit_counts(expo = 7):
    max_sum = 9**2 * expo
    ending89 = set(i for i in range(1, max_sum + 1) if chain_ending(i) == 89)

    for t in itertools.combinations_with_replacement(range(10), r = expo):
        digit_sq_sum = sum(i*i for i in t)
        if digit_sq_sum in ending89:
            histogram = [0] * 10
            for digit in t:
                histogram[digit] += 1
            permutations = math.factorial(len(t))
            for i in histogram:
                if i > 1:
                    permutations /= math.factorial(i)
            yield permutations

def solve():
    print(sum(powerful_digit_counts()))

def main():
    import time
    start = time.time()
    solve()
    end = time.time()
    elapsed = end - start
    print("elapsed: {:.1f} ms".format(elapsed * 1000))                  # elapsed: 87.0 ms

main()