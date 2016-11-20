#!/usr/bin/python
# Solved by Bogdan Trif @ 2016-09-0
#The  Euler Project  https://projecteuler.net
''''
Prime permutations
Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?
'''
import itertools

###################    START FUNCTIONS #########################
def unique_digit(X):
    #print(str(set(X)))
    if len(X) == len(set(X)):
        return True
        #print (X)
    else: return False #continue #print ('NOT unique !')

def detect_prime(n):
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


def string_to_list(strng):
   if (type(strng) == str):
      lst = list(strng)
      #print(lst)
      #print('The type of   ',lst, 'is :  ',type(lst))
      return lst
   #else: print('Not a string type !')

def list_to_string(lst):
   if ( type(lst) == list ):
      strng = ''.join(lst)
      #print(strng)
      #print('Type of  ',strng,' is:  ',type(strng))
      return strng
   #else: print('Not a list (array) type !')

def unique_digit_prime(n):
    if (detect_prime(n) is True and unique_digit(str(n)) == True) :
        return True
    else:
        return False

###################    END FUNCTIONS #########################
# Lists Deffinitions:

primes=[]
diff=[]
pairs=[]
selected_pairs=[]
unique_digit_list=[]
ordered_lists=[]
build_list=[]


print('----'*10,'  INITIAL PRIMES NUMBERS LIST ','----'*10)

my_array=[]
counter=1
i = 1000          #Set the starting Prime, First Prime in the list, 1000

while(i <= 9999):         # Set the last Prime Number Up, 9999
    j = 2
    while(j <= (i/j)):
        if not(i % j): break        # IF  it's TRUE it stops, if NOT TRUE it continues
        j = j + 1                       #Returns False and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
    if (j > i/j) :
        my_array.append(i)
    i = i + 1


print (my_array)
print ("First element of the array is: ", my_array[0], "    &     Last element of the array is: ", my_array[-1])
print ("There are   : ", len(my_array),'  prime numbers')

#prime_list = [ i for i in my_array  if i >1000]

print('----'*10,'  TESTS   ','----'*10)

print('test unique digit for 1026 :  ',unique_digit(str(1026)))
print('test unique digit for 1031 :  ',unique_digit(str(1031)) == True)



print('----'*10,'  UNIQUES PRIMES LIST   ','----'*10)


for Y in my_array:
    if (unique_digit(str(Y)) == True):
        unique_digit_list.append(Y)

print('Unique Digit List:      ',unique_digit_list)
print('Length of the Unique Digit List:      ',len(unique_digit_list))
print('\n')

print('Uniques primes transformed into lists :   ')
for Z in unique_digit_list:
    A = str(Z)
    #print(A, type(A))
    B = list(A)
    #print(B, type(B), sorted(B),' --- ' ,end=' ')
    C = ''.join(str(x) for x in sorted(B))
    ordered_lists.append(C)
    print(B, end=' ')
    #for J in B:
      #  print(J)
     #counter +=1


print('\nOrdered lists:   ',ordered_lists)
print('Length:  ',len(ordered_lists), '    Element Nr 2 is: ',ordered_lists[1])

print('----'*10,'  DUPLICATES   ','----'*10)

duplicates = {}
for i in ordered_lists:
    if i in duplicates:
        duplicates[i] += 1
    else:
        duplicates[i] = 1

unique_primes = [x for x, y in duplicates.items() if y >= 3]
print ('There are : ',len(unique_primes),'elements','\n' ,'Elements which are repeated more than 3 times :      \n',unique_primes)
print('Duplicates:    ',duplicates)
#print('Number of duplicates:    ',len(duplicates))

print('Which transformed into lists are :   ')
gold_primes=[]
for i in unique_primes:
    gold_primes.append(string_to_list(i))

print(gold_primes)

print('\n','----'*10,'  PERMUTATIONS (only the primes)','----'*10)
print(primes)

print('\n','----'*5,'  some tests ','----'*5)

A = ["".join(x)  for x in list(itertools.permutations(['1','0','6','9']))]
B = [int(x) for x in A  if int(x) >1000]
C = [x for x in B if detect_prime(x) == True]
print(A)
print(B)
print(C)

print('\n','----'*30)

iterator=0
for Y in gold_primes:
    A = ["".join(x)  for x in list(itertools.permutations(Y))]
    B = [int(x) for x in A  if int(x) >1000]
    C = [x for x in B if detect_prime(x) == True]
    primes.append(C)
    print(str(iterator)+'.',C)
    iterator += 1

primes=sorted(primes)
print('Length:    ',len(primes),'\n',primes)
print('And this is how you access a sub element from the array :    ',primes[1][2])
print('And this is how you access an  element from the array :    ',primes[5])

print('\n','----'*10,'DIFFERENCES','----'*10)
print(range(len(primes)))

counter=0
for z in range(10) :              # range(len(primes))    range(5)
    temp_diff=[]
    temp_pair=[]
    for x in range(len(primes[z])):
        for y in range(x):
            counter += 1
            #print(str(counter)+".  ",primes[z][x],' - ',primes[z][y] ,' =  ',primes[z][x]-primes[z][y])
            temp_pair += [(primes[z][y])]
            temp_pair += [(primes[z][x]-primes[z][y])]
            temp_diff += [(primes[z][x]-primes[z][y])]
    diff.append(temp_diff)
    pairs.append(temp_pair)
print('The total number of combinations between two elements of the multiple array is:  ',counter)
print('Diff :      ',diff)
print('Pairs :     ',pairs)

print('\n','---'*20,'REPEATED NUMBERS','----'*10)

print('JUST FOR TEST the index of the Differences:   ',diff[0],'\n')

diff_duplicates = []
temp_dict={}

#for R in range(len(diff)):
 #   print(R)

for S in range(len(diff)):
    temp_dict={}
    for R in diff[S]:

        #print(R)
        if R in temp_dict:
            temp_dict[R] += 1
        else:
            temp_dict[R] = 1
    #print('Temporary Dictionary:   ',temp_dict)

    only_2_times_diff_duplicates = [x for x, y in temp_dict.items() if y >= 2]
    print('Differences repeated AT LEAST 2 times are : ',only_2_times_diff_duplicates)
    diff_duplicates.append(only_2_times_diff_duplicates)


print('Final Dict:   ',diff_duplicates)
print('Just an index test to Final Dict:   ',diff_duplicates[2])

print('Test if it is not NULL : ',diff_duplicates[2] != [] )

numarator=1
improved_pairs=pairs
improved_diff=diff
for v in range(int(len(diff_duplicates))):
    if diff_duplicates[v] != [] :
        print('Index:',v,'   ' ,diff_duplicates[v])
    elif diff_duplicates[v] == [] :
        improved_pairs.pop(v-numarator)
        improved_diff.pop(v-numarator)
    numarator += 1

print(len(improved_diff),'Improved Differences',improved_diff)
print(len(improved_pairs),'Improved Pairs :  ',improved_pairs)

#NOT YET FINISHED, ANYWAY IT SEEMS THAT THE ALGORITHM IS NOT OK !!!!!!!!!!


'''
for X in diff_duplicates:
    #print(X, end=' ')
    if int(X) in pairs:
        selected_pairs.append(pairs[pairs.index(X)-1])
        selected_pairs.append(pairs[pairs.index(X)])
        print('Potential Number : ',pairs[pairs.index(X)-1], '        Diff nr. : ',pairs[pairs.index(X)] )

print('\nSelected pairs :    ',selected_pairs,'\n')
'''

'''
print ('Differences repeated AT LEAST 2 times are:        ',[x for x, y in diff_duplicates.items() if y >= 2])
print(type(diff_duplicates),'   ALL the differencess :    ',diff_duplicates)
print(' Only the  Number of UNIQUE  differences  :    ',len(diff_duplicates))
only_2_times_diff_duplicates = [x for x, y in diff_duplicates.items() if y >= 2]
'''




print('\n','---'*20,'POTENTIAL NUMBER','----'*10)




'''
for i in range(1,int(len(ordered_lists))):
    counter += 1
    for j in range(0, i):
    if ordered_lists[i] == ordered_lists[i-1]:
        print(ordered_lists[i], end='')
'''


print('\n','-----'*24,'\n')

