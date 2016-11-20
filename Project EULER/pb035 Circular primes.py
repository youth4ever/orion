#!/usr/bin/python3
# Solved by Bogdan Trif @  Completed on Tue, 27 Sep 2016, 00:04
#The  Euler Project  https://projecteuler.net
'''
Circular primes     -       Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
'''
#####################    FUNCTIONS ######################################

import time
t1  = time.time()
my_primes=[]

def circulate_number(A):
      tmp=[]
      for v in range(len(str(A))):
            a , i , s =  str(A), len(str(A)), ''
            for c in range(i):
                  #print(a[(v+c) % j] ,end='  ')
                  s += str(a[(v+c) % i])
            #return s
            tmp.append(int(s))
            #print(s)
            v+= 1
      return tmp #print(tmp)

def detect_prime(n):                # Function which checks if a number is prime
    i = n
    while(i <= n):
        j = 2
        while(j <= (i/j)):
            if not(i%j):
                return False
                break
            j = j + 1
        if (j > i/j) : return True
        i = i + 1

def primes_gen(i=81, END=100 ):
    '''  Prime numbers GENERATOR Function
    i - Sets the starting Prime, First Prime in the list, MAIN VARIABLE
    END - Sets the END Prime, First Prime in the list, MAIN VARIABLE
    '''
    while(i < END):                 # Set the last Prime Number - the Upper Limit
        j = 2
        while(j <= (i/j)):              # This condition checks in the lower list
            if not(i%j): break          # IF  it's TRUE it stops, if FALSE it continues    # VERY IMPORTANT This line checks if the number is PRIME
            j = j + 1                       #Returns FALSE and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
        if (j > i/j) : print( i, end=' ')           # If j > i/j means that the number is not already in the list, therefore must be another prime
        i = i + 1

# Function CIRCULAR PRIMES, Check if the CIRCULAR permutations of a number are primes
def circular_primes(n):
    ''' Function which checks if the permutations of a number are primes
    Depends on the Function detect_prime
    '''
    counter=0
    for x in circulate_number(n):
        if (detect_prime(x) == True ):
            counter+=1
            #print(x)
    if (len(str(n)) == counter): return True    #   print('YES, all permutations are prime !')
    else:  return False                                 #print('NO, only',counter,' are primes')

########################    END FUNCTIONS         ######################################

init_list=[]

for k in range(2,100000):
    if detect_prime(k)== True :
        if ( '0' not in str(k) and '2' not in str(k) and '4' not in str(k) and '5' not in str(k) and '6' not in str(k) and '8' not in str(k) ) :
            if circular_primes(k) == True :
                init_list.append(k)

C= set(init_list)
print('Observation: I excluded 2 & 5 from the list, therefore the length will be + 2. \n\n',init_list)
print(C)
print('\nThere are ',len(C)+2,'primes in the range 1:1000000       ')               # 55 primes between 1-1000000

#print(circular_primes(197))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms')