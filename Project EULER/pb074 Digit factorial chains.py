#!/usr/bin/python3
# Solved by Bogdan Trif @   Completed on Thu, 27 Oct 2016, 19:30
#The  Euler Project  https://projecteuler.net
'''
                                Digit factorial chains      -       Problem 74
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

                                    1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
it turns out that there are only three such loops that exist:

                                    169 → 363601 → 1454 → 169
                                    871 → 45361 → 871
                                    872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

                                69 → 363600 → 1454 → 169 → 363601 (→ 1454)
                                78 → 45360 → 871 → 45361 (→ 871)
                                540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain
with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''
from math import factorial
import time

fs=[1,1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

# for i in '43545':    print(fs[int(i)])

class chain_factor(object):

    def __init__(self, nr):
        self.nr = nr

    def chain_factor(n):
        n, S = list(str(n)), 0
        for i in n:
            S += fs[int(i)]      # Using pre-calculated factorials
            # S += factorial(int(i))
        return print(S)


print('\n------------------------- MY SOLUTION, BRUTE FORCE, Can be optimized ! ---------------------------------------')
t1  = time.time()

chain=[]
def chain_factor(n):
    while n not in chain:
        chain.append(n)
        #print(chain)
        n, S = str(n), 0
        for i in n:
            # S += factorial(int(i))
            S += fs[int(i)]       # Using pre-calculated factorials
        n = S
        chain_factor(n)
    return len(chain)

print(chain_factor(169))

iter = 0
maxv = 0
for i in range(1,1000000):
    chain=[]
    iter +=1
    if iter %100000 == 0:
        print(iter)
    if chain_factor(i) == 60 :
        maxv +=1
        print(i, chain_factor(i))

print('\nResult:',maxv)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')      #Completed in : 213949.237108 ms



print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1 , VERY GOOD, mbh038, England --------------------------')
t1  = time.time()

# About 150 ms, in Python.
# I only check for numbers with integers that increase in order, then find the number of valid permutations of those digits -
# all permutations must have the same chain length. To speed things up when working through chains,
# I develop a dictionary of the chain lengths found for all numbers that have appeared in chains before,
# and stop when I get to one of these numbers, because the chain length of the present number can now be calculated directly.
# This saves a lot of time.
# When I first solved the problem using brute force, my code required 70 s.
# Getting the dictionary/cache method to work correctly brought that down to 3.5 s,
# then the realisation that digit order did not matter brought the time down to 150 ms.
import itertools
import math

def cl(n):
    fs=[1,1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    chainlengths={169:3,871:2,872:2,145:1,69:5,78:4,540:2}
    fd=set()
    for number in itertools.combinations_with_replacement('0123456789',len(str(n-1))):
        nx=int(''.join([x for x in number]))
        for number in [nx,10*nx]:
            if number>n:
                continue
            chain=[number]
            while 1:
                candidate=sum([fs[int(x)] for x in str(chain[-1])])
                if candidate in set(chain):
                    chainlengths[candidate]=len(chain)-chain.index(candidate)
                    break
                if candidate in chainlengths:
                    chainlengths[number]=len(chain)+chainlengths[candidate]
                    break
                chain.append(candidate)

            for j in range(len(chain)):
                if chain[j] in chainlengths:
                    continue
                if candidate in set(chain):
                    chainlengths[chain[j]]=chainlengths[candidate]+chain.index(candidate)-j
                else:
                    chainlengths[chain[j]]=chainlengths[candidate]+len(chain)-j

            if chainlengths[number]==60:
                fd.add(number)

    #how many permutations are there of each of these numbers?
    ysum=[]
    for x in fd:
        y=[i for i in str(x)]
        ysum.append(math.factorial(len(y)))
        if '0' in y:
            ysum[-1]-=math.factorial(len(y)-1)
        y=''.join([i for i in y])
        xdic={}
        for digit in y:
            xdic[digit]=xdic.get(digit,0)+1
        for k,v in xdic.items():
            ysum[-1]=ysum[-1]//math.factorial(v)

    print(sum(ysum))

cl(1000000)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      #  Completed in : 144.008398 ms

print('\n--------------------------SOLUTION 2 , GOOD, mr.unease , Sweden   --------------------------')
t1  = time.time()

# Clean well formated python3, 4.2s on my i3 10years old faithful laptop.
# Just cut the caching when the loop starts.
# Sorry for short var names.

def factorial(x):
    return 1 if x < 2 else x*factorial(x-1)

def main():
    s = 69
    limit = 10**6
    dig_fact = {str(x): factorial(x) for x in range(10)}
    cache = {x: 0 for x in range(1, limit)}

    for num in range(s, limit):
        if cache[num] != 0:
            continue
        c = [num]
        i = 1
        while True:
            num = sum(dig_fact[n] for n in str(num))
            if num < limit and cache[num] != 0:
                c += [num]
                i += cache[num]
                break
            if num in c:
                c += [num]
                break
            c += [num]
            i += 1

        for n in c:
            if n == c[-1]:
                break
            cache[n] = i
            i -= 1
    print( sum(1 for x in cache.values() if x == 60))


if __name__ == '__main__':
    main()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      #  Completed in : 6839.391232 ms

print('\n--------------------------SOLUTION 3 , GOOD , punkninja, Taiwan --------------------------')
t1  = time.time()

# My python solution, it memorizes the length of the chains that have been calculated and marked
# the start of that chain as calculated. When later calculation encounters that number it just adds the calculated
# chain length and stops. It runs about 3.8s on my machine.
# I haven't worked out the proof why this works, so it could be case specific.

factorials = {'0': 1,'1': 1,'2': 2,'3': 6,'4': 24,'5': 120,'6': 720,'7': 5040,'8':40320,'9':362880}
isCalculated = []
calculated_chains_length = []

#Initialize
for i in range(0,1000000):
        isCalculated.append(False)
        calculated_chains_length.append(0)

def getNextNumber(number):
    number_string = str(number)
    next_number = 0
    for index in range(len(number_string)):
        next_number += factorials[number_string[index]]
    return next_number;


def calculateChainLength(number):
    number_in_chain = [number]
    chain_length = 0
    is_repeated = False

    while(is_repeated != True):
            next_number = getNextNumber(number_in_chain[chain_length])
            if(next_number < 1000000):
                if(isCalculated[next_number] == True):
                    isCalculated[number] = True
                    calculated_chains_length[number] = chain_length + calculated_chains_length[next_number] + 1
                    return  calculated_chains_length[number]
            #print("next number is " + str(next_number) + "\n")
            for index in range(len(number_in_chain)):
                #print(str(number_in_chain[index]) + "\n")
                if(number_in_chain[index] == next_number):
                    #print("repeated\n")
                    is_repeated = True
                    break;
                #else:
                   #print("not repeated\n")
            if(is_repeated != True):
                number_in_chain.append(next_number)
                chain_length += 1

    #plus one to compenstate for the first number added to the chain
    isCalculated[number] = True
    calculated_chains_length[number] = chain_length + 1
    return calculated_chains_length[number]

def solve():
    sol = 0
    for index in range (0,1000000):
        length = calculateChainLength(index)
        if(length == 60):
            sol += 1
    return sol

print(str(solve()))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 8796.503067 ms

print('\n--------------------------SOLUTION 4 , mthomas81, Sweden  --------------------------')
t1  = time.time()

# I initially ran it with brute force in Python which took 228s, but I knew there was plenty of easy optimization to do.
# After optimization got down to 13s
# I created a dictionary with numbers where I knew the length of the chain.
# There are two conditions in my if statement.
# If a number already exists in the chain (this was kept from the brute force solution) then the chain is finished
# and add all numbers to the dictionary with the appropriate chain length.
# If a number in the chain already exists in the dictionary, then stop iterating and add the chain to the dictionary with the appropriate length.
# I'm mostly a beginner to python so my code is a bit verbose and can be cleaned up. (Figuring out how to do that slowly)

from math import factorial

def digit_factorial_sum(number):
    strnum = str(number)
    digit_sum = 0
    for digit in strnum:
        digit_sum += factorial(int(digit))
    return digit_sum

def create_dictionary(iter,curr_chain):
    dict = {}
    nrepeat = curr_chain.index(iter)
    len_chain = len(curr_chain)
    for i,key in enumerate(curr_chain):
        if i < nrepeat:
            dict[key] = len_chain-i
        else:
            dict[key] = len_chain-nrepeat
    return dict

def create_dictionary2(iter_val,curr_chain):
    dict = {}
    len_chain = len(curr_chain)
    for i,key in enumerate(curr_chain):
        dict[key] = len_chain-i+iter_val
    return dict




all_chains = {}
len_chains = []
for start_no in range(1,1000000):
    #print 'start number ', start_no
    curr_chain = []
    exist_in_curr_chain = False
    next_iter = start_no
    while exist_in_curr_chain == False:
        if next_iter in curr_chain:
            exist_in_curr_chain = True
            len_chains.append(len(curr_chain))
            ## add local dict to global dict
            local_dict = create_dictionary(next_iter,curr_chain)
            all_chains.update(local_dict)
        elif next_iter in all_chains:
            exist_in_curr_chain = True
            iter_val_in_all_chain = all_chains[next_iter]
            # all_chains = add curr_chain to global dictionary
            local_dict = create_dictionary2(iter_val_in_all_chain,curr_chain)
            all_chains.update(local_dict)
        else:
            curr_chain.append(next_iter)
        next_iter = digit_factorial_sum(next_iter)

#print all_chains
exactly_60 = 0
for key in all_chains:
    if all_chains[key] == 60:
        exactly_60 += 1

print ('exaclty chain of 60 : ', exactly_60)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      #  Completed in : 19129.094124 ms

