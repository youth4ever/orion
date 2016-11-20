# MAde by Bogdan Trif @ 2016-09-13, 11:07
import itertools

###################    START FUNCTIONS #########################
def unique_digit(X):                    # Function which checks if a number has unique digits
    #print(str(set(X)))
    if len(X) == len(set(X)):
        return True
        #print (X)
    else: return False #continue #print ('NOT unique !')

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


def string_to_list(strng):        # Converts a string into a list,      Usage :   string_to_list('1487')
   if (type(strng) == str):
      lst = list(strng)
      #print(lst)
      #print('The type of   ',lst, 'is :  ',type(lst))
      return lst
   #else: print('Not a string type !')

def list_to_string(lst):        # Converts a list into a string, usage :  list_to_string(['1','4','8','7'])
   if ( type(lst) == list ):
      strng = ''.join(lst)
      #print(strng)
      #print('Type of  ',strng,' is:  ',type(strng))
      return strng
   #else: print('Not a list (array) type !')

def unique_digit_prime(n):          # Calls the other function which checks if a number is prime:
    if (detect_prime(n) is True and unique_digit(str(n)) == True) :
        return True
    else:
        return False

def is_candidate(alph):     # this function computes diff of three of a four digit number to be equal
    beta=str(alph)
    alph=sorted(beta)
    if (int(alph[2])-int(alph[1]) == int(alph[1])-int(alph[0])): return True
        #print ('There are three equally spaced numbers : ', alph[0],alph[1],alph[2])
    elif (int(alph[3])-int(alph[2]) == int(alph[2])-int(alph[0])): return True
        #print ('There are three equally spaced numbers : ', alph[0],alph[2],alph[3])
    elif (int(alph[3])-int(alph[2]) == int(alph[2])-int(alph[1])): return True
        #print ('There are three equally spaced numbers : ', alph[1],alph[2],alph[3])
    elif (int(alph[3])-int(alph[1]) == int(alph[1])-int(alph[0])): return True
        #print ('There are three equally spaced numbers : ', alph[1],alph[2],alph[3])
    else : return False
        #print('NOT a good choice')


###################    END FUNCTIONS #########################
# Lists Deffinitions:

primes=[]
diff=[]
pairs=[]
selected_pairs=[]

print('-----'*10, 'TESTS ','-----'*10)

list_to_string(['1','4','8','7'])
print('Conversion from list to string :   ',type(list_to_string(['1','4','8','7'])),list_to_string(['1','4','8','7']))

string_to_list('1487')
print('Conversion from string to list :  ',type(string_to_list('1487')), string_to_list('1487'))

n=4817             # 7121      4817
unique_digit(str(4871))
detect_prime(4871)
print('test unique digit for 1026 :  ',unique_digit(str(1026)))

if detect_prime(n) is True  :# and  unique_digit(str(n)) == True) :
    if unique_digit(str(n)) == True:
        print(n,'  is prime &  has unique digits')
    elif unique_digit(str(n)) == False :
        print(n,'   is prime, but has not unique digits')
else:
    print (n, '  NOT prime !')

print('Unique Digit prime check for 8147 :    ',unique_digit_prime(8147))                 # 7121      4817

itertools.permutations(['1','4','8','7'])
list(itertools.permutations(['1','4','8','7']))
print(type(list(itertools.permutations(['1','4','8','7']))),list(itertools.permutations(['1','4','8','7'])))

print('Test which Checks if the number has equally spaced digits :  ',is_candidate(4751))




print('----'*10,'  UNIQUES PRIMES LIST   ','----'*10)

for Y in ten_thousand_primes:
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

print('\nOrdered lists:   \n',ordered_lists)
print('Length:  ',len(ordered_lists), '    Element Nr 2 is: ',ordered_lists[1], print(type(ordered_lists[1])))


print('----'*10,'  DUPLICATES   ','----'*10)

duplicates = {}
for elem in ordered_lists:
    if elem in duplicates:
        duplicates[elem] += 1
    else:
        duplicates[elem] = 1

unique_primes = [x for x, y in duplicates.items() if y >= 3]
print ('There are : ',len(unique_primes),'elements','\n' ,'Elements which are repeated more than 3 times :      \n',unique_primes)
#print('Duplicates:    ',duplicates)
#print('Number of duplicates:    ',len(duplicates))

print('Which transformed into lists are :   ')
gold_primes=[]
for i in unique_primes:
    gold_primes.append(string_to_list(i))

print('Gold Primes are :  ',gold_primes)

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


for X in diff_duplicates:
    #print(X, end=' ')
    if int(X) in pairs:
        selected_pairs.append(pairs[pairs.index(X)-1])
        selected_pairs.append(pairs[pairs.index(X)])
        print('Potential Number : ',pairs[pairs.index(X)-1], '        Diff nr. : ',pairs[pairs.index(X)] )

print('\nSelected pairs :    ',selected_pairs,'\n')



print ('Differences repeated AT LEAST 2 times are:        ',[x for x, y in diff_duplicates.items() if y >= 2])
print(type(diff_duplicates),'   ALL the differencess :    ',diff_duplicates)
print(' Only the  Number of UNIQUE  differences  :    ',len(diff_duplicates))
only_2_times_diff_duplicates = [x for x, y in diff_duplicates.items() if y >= 2]



for i in range(1,int(len(ordered_lists))):
    counter += 1
    for j in range(0, i):
        if ordered_lists[i] == ordered_lists[i-1]:
            print(ordered_lists[i], end='')





#THE ALGORITHM IS NOT CORRECT !!!!!!!!!!!!!!!!!!! even if it works for the case  n = 1487

print('\n','===='*10,'  START HERE  ','===='*10)

print('\n','----'*10,'  PERMUTATIONS (only the primes)','----'*10)


alpha = '6379'
print('Digits in ascending order :  ',sorted(alpha))
alph = sorted(alpha)

# Test to check if a number is good candidate, has three equally spaced digits:
if (int(alph[2])-int(alph[1]) == int(alph[1])-int(alph[0])): #return True
    print ('There are three equally spaced numbers : ', alph[0],alph[1],alph[2])
elif (int(alph[3])-int(alph[2]) == int(alph[2])-int(alph[0])): #return True
    print ('There are three equally spaced numbers : ', alph[0],alph[2],alph[3])
elif (int(alph[3])-int(alph[2]) == int(alph[2])-int(alph[1])): #return True
    print ('There are three equally spaced numbers : ', alph[1],alph[2],alph[3])
elif (int(alph[3])-int(alph[1]) == int(alph[1])-int(alph[0])): #return True
    print ('There are three equally spaced numbers : ', alph[1],alph[2],alph[3])
else : #return False
    print('NOT a good choice')


beta = string_to_list(alpha)
print(beta)

for x in list(itertools.permutations(beta)):
    #print (x,end=' ')
    x = ''.join(x)
    #print(x, type(x), end='')
    x= int(x)
    if (detect_prime(x) == True and x > 1000 and is_candidate(x) == True) :
        primes.append(x)

primes=sorted(primes)
print('Ascending / sorted primes :        ',primes)

print('\n','----'*10,'DIFFERENCES','----'*10)

counter=0
for x in range(len(primes)):
    for y in range(x):
        counter += 1
        print(str(counter)+".  ",primes[x],' - ',primes[y] ,' =  ',primes[x]-primes[y])
        pairs.append(primes[y])
        pairs.append(primes[x]-primes[y])
        diff.append(primes[x]-primes[y])
print('The number of combinations between two elemets of the array is:  ',counter)
print('Diff :      ',diff)
print('Pairs :     ',pairs)

print('\n','---'*20,'REPEATED NUMBERS','----'*10)

diff_duplicates = {}
for elem in diff:
    if elem in diff_duplicates:
        diff_duplicates[elem] += 1
    else:
        diff_duplicates[elem] = 1

print ('Differences repeated AT LEAST 2 times are:        ',[x for x, y in diff_duplicates.items() if y >= 2])
print(type(diff_duplicates),'   ALL the differencess :    ',diff_duplicates)
print(' Only the  Number of UNIQUE  differences  :    ',len(diff_duplicates))
only_2_times_diff_duplicates = [x for x, y in diff_duplicates.items() if y >= 2]

print('\n','---'*20,'POTENTIAL NUMBER','----'*10)

for X in only_2_times_diff_duplicates:
    #print(X, end=' ')
    if int(X) in pairs:
        selected_pairs.append(pairs[pairs.index(X)-1])
        selected_pairs.append(pairs[pairs.index(X)])
        print('Potential Number : ',pairs[pairs.index(X)-1], '        Diff nr. : ',pairs[pairs.index(X)] )

print('\nSelected pairs :    ',selected_pairs,'\n')

for R in range(1,len(selected_pairs),2):
    a = selected_pairs[R-1]+ selected_pairs[R]
    b = a + selected_pairs[R]
    if unique_digit_prime(b) == True:
        print('!!!!   AND THE NUMBERS ARE :     ',selected_pairs[R-1],a,b,'             !!!!!!!')


# print('\n','Test for 3330 in pairs :    ',3330 in pairs, pairs.index(3330))


'''
arr = list(itertools.permutations(('1','4','8','7')))
print(type(arr),arr)
counter=0

for i in ['3','6','7','9','2']:
    print(i)
'''

#3467 4637 5807
#print(detect_prime(3467))