#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Wed, 12 Oct 2016, 18:46
#The  Euler Project  https://projecteuler.net
'''
Prime digit replacements    -   Problem 51
By replacing the 1-st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3-rd and 4-th digits of 56**3 with the same digit, this 5-digit number is the first example having
seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
with the same digit, is part of an eight prime value family.
'''
import time
from itertools import combinations


def sieve(lower, upper_bound):         # THE FASTEST  !!!!!!!!!!!
    # sieve of Eratosthenes
    n = upper_bound + 1
    check = [True] * n
    check[0] = check[1] = False
    for i in range(2, int(upper_bound**0.5) + 1):
        if check[i]:
            for j in range(i**2, upper_bound + 1, i):
                check[j] = False
    primes = [i for i, flag in enumerate(check) if flag and i > lower ]
    return primes

def is_prime(n):
    # Function which checks if a number is prime
    for i in range(2, int(pow(n,1.0/2))+1):
        if n%i==0:
            return 0
    return 1

X=1979 #510510             # Type the  number you want to check       132499
if is_prime(X) == True : print('YES, is a prime !')
else : print('Not a prime ')

#for i in range(4,6,1):    print(len([0]*i), [0]*i, end=' ')

print('\n\n----------------------------   MY  SOLUTION -------------------------------')


t1  = time.time()
#
# def get_indexes (A):
#     indexes=[]
#     for i in range(1, len(A)):
#         Comb = list(combinations(A[0:len(A)-1],i))
#         #print('->  ',Comb)
#         for j in Comb:
#             #print(j)
#             indexes.append(j)
#     return indexes      #print(  indexes)
#
#
# def replace_indexes(nr):
#         global seeked, tmp, maxnr
#         for g in range(len(indexes)) :
#             tst = list(str(nr))
#             #print('----')
#             tmp=[]
#             for i in range(10):
#                 for h in range(len(indexes[g])):
#                     tst[indexes[g][h]] = str(i)
#                     #print(indexes[g][h])
#                 #print(tst, int(''.join(tst)))
#                 lk =  int(''.join(tst))
#                 if is_prime(lk) == 1 and len(str(lk)) == len(A) :
#                     tmp.append(lk)
#                     #print(tmp, len(tmp), maxnr)
#             #if len(tmp) > 3 : print('-->  ',maxnr ,  len(tmp) , tmp)
#             if len(tmp) > maxnr :
#                 seeked.append(tmp)
#                 maxnr = len(tmp)
#                 #print('  SEEEEEEEEEEEEEEEEEEKED ',seeked)
#             if len(tmp) == 8: break
#
# # Here we start by setting the range of primes we want to analyze :
# primes = sieve(100000, 1000000)
# print(len(str(primes[0])),primes[0:20])
#
# global maxnr, seeked
# seeked, maxnr =[] , 0
#
# #A = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# A = A[0:len(str(primes[0]))]
# #A = A[0:6]
# print(A)
#
# indexes = get_indexes(A)
# print('INDEXES  :     ',indexes,'\n\n')
#
# for i in primes:
#     replace_indexes(i)
#
# print('\n\n',seeked)                       # [121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393]

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')        # 1083.619979 s

#string2=''.join(my_list)                                                        # Transform back the list into a string

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1 ,  FAST , INTERESTING SOLUTION , aolea , Spain --------------------------')

t1  = time.time()

import pyprimes
flag = False
for i in pyprimes.primes_above(2):
    if flag == True:
        break
    count1 = []
    count2 = []
    listI = list(str(i))
    if len(set(listI)) != len(listI):
        for k in listI:
            if k not in count1:
                count1.append(k)
                count2.append(1)
            else:
                count1.index
                count2[count1.index(k)] += 1
        for l in range(0,len(count1)):
            if count2[l] > 1:
                count = 0
                for m in range (0,10):
                    aux = count2[l]
                    while aux > 0:
                        listI[listI.index(count1[l])] = m
                        aux = aux - 1
                    count1[l] = m
                    iModStr = ''.join(str(e) for e in listI)
                    iMod = int(iModStr)
                    if pyprimes.isprime(iMod) == True and len(str(i))==len(str(iMod)):
                        count = count + 1
                        #if count > 5 : print(i,iMod,count)
                        if count == 8:
                            print(i, count1,listI,count)
                            flag = True
                            break

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')        # 3.932225 s

print('\n--------------------------SOLUTION 2 ,  FAST, NICE FUNCTIONS , mdingens, USA --------------------------')

# Wow you guys are good at this. I was pumped with 5.828 seconds.
# Basically I just went from prime to prime looking for repeating digits, then when I found them I created 'families'
# will all possible combinations of repeating digit indices looking for an 8 prime value family.

t1  = time.time()

primes = sieve(100000, 1000000)
from math import floor
from itertools import combinations


def is_prime(n):
    """
    Tests if a number n is prime
    :param n: Number to be tested
    :return: True if n is prime, False if not
    """

    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, floor(n ** .5) + 1):
            if n % x == 0:
                return False
        return True


def count_primes(lst):
    """
    Return the number of prime numbers in a list
    :param lst: List to be examined
    :return: Number of prime numbers in lst
    """
    count = 0
    for element in lst:
        if is_prime(int(element)):
            count += 1
    return count


def index_duplicates(prime):
    """
    Returns all index combinations of all duplicate digits for a given prime; in the case that there are N indices
    containing the same digit and N > 2, will include all combinations of indices with 2 to N members
    :param prime: Prime number to be examined
    :return: List of all combinations of duplicate digits in list form
    """

    string = str(prime)
    dup_digits = []
    indices_w_dup = []
    combos = []
    if len(string) == 2:
        return [(0,), (1,)]
    else:
        for x in range(len(string)):
            digit = string[x]
            if digit not in dup_digits:
                rest = string[:x] + string[x + 1:]
                if digit in rest:
                    dup_digits.append(digit)
                    indices_w_dup.append([x for x in range(len(string)) if string[x] == digit])
        for group in indices_w_dup:
            for r in range(1, len(group) + 1):
                for combination in combinations(group, r):
                    combos.append(combination)
        return combos


def build_family(prime, indices):
    """
    Will return a list of all numbers created by replacing the given indices of the given prime with the same number
    :param prime: Prime to be changed
    :param indices: Indices that will be altered
    :return: List of all possible numbers
    """

    family_str = []
    family = []
    for x in range(10):
        lst_str = [x for x in str(prime)]
        for index in indices:
            lst_str[index] = str(x)
        family_str.append(''.join(lst_str))
    for string in family_str:
        if string[0] != '0':
            family.append(int(string))
    return family


def main():
    """
    Main function that will determine and print the smallest prime which, by replacing part of the number (not
    necessarily adjacent digits) with the same digit, is part of an eight prime value family
    :return: None
    """
    target = 8
    spot = 3
    while True:
        if is_prime(spot):
            for index_group in index_duplicates(spot):
                family = build_family(spot, index_group)
                if count_primes(family) == target:
                    print([x for x in family if is_prime(x)], index_group)
                    return None
            spot += 2
        else:
            spot += 2

main()

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')        # 11.726671 s

print('\n--------------------------SOLUTION 3 , NICE  BRUTE FORCE,  FJ_Sevilla , Spain --- --------------------------')
# Python 3 pure brute force, proving since 11 all possible replacements digit :)

t1  = time.time()
from itertools import permutations
from math import sqrt

class Euler():
    def __init__(self, familiars):
        self.familiars = familiars
        self.lbreak = 10-self.familiars
        self.permuts={}
        self.sieve = self.Eratosthenes_sieve(1000000)

    def Eratosthenes_sieve(self, lim):
        sieve = [True] * lim
        sieve[0:2]=[False]*2
        sieve[2]=True
        sieve[4::2]=[False]*len(sieve[4::2])
        for num in range(3,int(sqrt(lim))+1,2):
            if sieve[num]:
                sieve[num*num::2*num]=[False]*int((lim-num*num-1)/(2*num)+1)
        return sieve

    def primes_gen(self, init):
        while True:
            if self.sieve[init]:
                yield init
            init+=1

    def gen_permut(self,digits):
        self.permuts[str(digits)]=set()
        for r in range(1,digits):
            bList = [True]*r +[False]*(digits-r)
            p=[p for p in permutations(bList,digits) if p.count(True)==r]
            self.permuts[str(digits)].update(p)


    def num_permut(self, num):
        num = list(str(num))
        l = len(num)

        if not str(len(num)) in self.permuts:
            self.gen_permut(l)

        for p in self.permuts[str(l)]:
            aux=num.copy()
            nofam=0
            per=0
            fam = []


            for m in range(0,10):
                for index,dig in enumerate(p):
                    if dig == True:
                        aux[index]=str(m)
                per = int(''.join(aux))
                if len(str(per))!= l:
                    continue

                if self.sieve[per]:
                    fam.append(per)
                    if len(fam)==self.familiars:
                        return fam
                else:
                    nofam+=1
                    if nofam > self.lbreak:
                        break

    def solve(self):
        gen = self.primes_gen(11)
        res = None
        while not res:
            res = self.num_permut(next(gen))
        print(res)


if __name__ == '__main__':

    r=Euler(8)
    r.solve()

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')        # 10.053575038909912

print('\n--------------------------SOLUTION 4 ,  NICE & INTERESTING, MatthewDonovan, Canada  ------------------------------')

#I was able to identify that the number of digits needing to be replaced was going to be a multiple of three.
# Otherwise there would only be a max of 7 possible replacement combinations as the others would result in multiples of 3.
# I opted to manually create each of these possibilities instead of creating a list of primes and working through that.
# Initially I didn't know how many digits the answer would be and I know I have difficulty computing all primes larger than ~10,000,000.

t1  = time.time()

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def six_digits():
    lst = []
    for i in ['1','3','7','9']:
        for j in range(1,10):
            j = str(j)
            for r in range(10):
                r = str(r)
                lst.append(j + r + '---' + i)
                lst.append(j + '-' + r + '--' + i)
                lst.append(j + '--' + r + '-' + i)
                lst.append(j + '---' + r + i)
        for q in range(10):
            q = str(q)
            for r in range(10):
                r = str(r)
                lst.append('-' + q + r + '--' + i)
                lst.append('-' + q + '-' + r + '-' + i)
                lst.append('-' + q + '--' + r + i)
                lst.append('--' + q + r + '-' + i)
                lst.append('--' + q + '-' + r + i)
                lst.append('---' + q + r + i)
    return lst

primes = six_digits()

def possibility(n, special="no"):
    counter = 0
    options = []
    for j in range(10):
        number = ''
        for i in n:
            if i != '-':
                number += i
            else:
                number += str(j)
        if is_prime(int(number)):
            if special != "no":
                options.append(number)
            if number[0] != '0':
                counter += 1
    if special != 'no':
        return options
    if counter == 8:
        return n
    else:
        return False

potential = []
for i in primes:
    if possibility(i) != False:
        potential.append(i)

numbers = []
for i in potential:
    numbers += possibility(i, 'yes')

numbers.sort()
print(numbers[0])

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')        # 7. 4 sec

print('\n--------------------------SOLUTION 5 ,  INCREDIBLE FAST , mbh038, England    ------------------------------')

# I don't yet understand why there must be three, not two or four replaced digits.
# I read that otherwise the number would be divisible by three. Why?

t1  = time.time()

import numpy as np
import itertools as it

def p51():

    limit=1000000
    while 1:
        primes=set(primesfrom2to(limit))

        for n in primes:
            if len(str(n))-len(set(str(n)))!=3:
                continue
            for pos in it.combinations(range(len(str(n))),3):
                count=0
                primlist=[]
                for replacewith in range(10):
                    a=[x for x in str(n)]
                    for i in pos:
                        a[i]=str(replacewith)
                    if (int(''.join(a))) in primes:
                        count+=1
                        primlist.append(int(''.join(a)))
                if count >7 and primlist[0]>100000:
                    print (n,count,min(primlist))
                    return
            if count>7:
                break
        limit*=2

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

p51()

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')        #  0.424024 s

