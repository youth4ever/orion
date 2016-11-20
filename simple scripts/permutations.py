import itertools

#  Permutation (order matters):
print ('Permutation:     ', list(itertools.permutations([1,2,3,4], 1)))      #  Last number specifies the group number of elements it should take
print ('Permutation without the last argument:     ', list(itertools.permutations([1,2,3,4])))    #  Without last argument it assumes permutation of all elements
print ('Permutation:     ', list(itertools.permutations([1,2,3,4], 2)))      #  Last number specifies the group number of elements it should take
print ('Permutation:     ', list(itertools.permutations([1,2,3,4], 3)))      #  Last number specifies the group number of elements it should take
x=print ('Permutation:     ', list(itertools.permutations([1,2,3,4,7], 4)))      # This takes all 4 elements

B=[7,1,6,9]
print ('Permutation:     ', list(itertools.permutations(B, 4)))      # This takes all 4 elements

for X in list(itertools.permutations(B, 4)):
   print(X)

x=list(itertools.permutations([1,2,3,4,5], 1))
print('Number of permutations: ', len(x),'     ', x)



#Combination (order does NOT matter):
print ('Combination:    ', list(itertools.combinations('123', 2)))


#Cartesian product (with several iterables):
print ('Cartesian Product:   ', list(itertools.product([1,2,3], [4,5,6])))       # combines two groups

# Cartesian product (with one iterable and itself):
print ('Cartesian product 2:    ', list(itertools.product([1,2], repeat=3)))

print('-------'*20)
print('........................Function which generates permutations:   ....................')

#function which generate permutations,  Better DON'T USE IT !!
def perm(a,k=0):
   if(k==len(a)):
      print (a)
   else:
      for i in range(k,len(a)):
         a[k],a[i] = a[i],a[k]
         perm(a, k+1)
         a[k],a[i] = a[i],a[k]

perm([7,2,3])

#     Make all possible permutations of the two lists:
list1 = ['square','circle','triangle']
list2 = ['red','green']
#Method I
print(list(map(' '.join, itertools.chain(itertools.product(list1, list2), itertools.product(list2, list1)))))
#Method II
print([x + y for x in list1 for y in list2] + [y + x for x in list1 for y in list2])        # Using list comprehensions

print('----------'*13)
# method, which will give you the Cartesian product of both lists :
for r in itertools.product(list1, list2): print (r[0] + r[1])

print('----------'*13)
# Transform a string into a list (array:
my_string='3567'
print(my_string,'    Type:   ',type(my_string))

my_list=list(my_string)                                                         # Transform string into a list
print(my_list,'    Type:   ',type(my_list))

# Transform a list  into a string:
string2 = ''.join(my_list)                                                        # Transform back the list into a string
print(string2,'    Type:   ',type(string2))


print('----------'*13)
print('........................Function which transforms a string into a list:   ....................')
def string_to_list(strng):
   if (type(strng) == str):
      lst = list(strng)
      print(lst)
      print('The type of   ',lst, 'is :  ',type(lst))
      return lst
   else: print('Not a string type !')

string_to_list('1218565')

print('----------'*13)
print('........................Function which transforms a list into a string:   ....................')

def list_to_string(lst):
   if ( type(lst) == list ):
      strng = ''.join(lst)
      print(strng)
      print('Type of  ',strng,' is:  ',type(strng))
      return strng
   else: print('Not a list (array) type !')

list_to_string(['4','5','7','9','1','8'])

print('====='*25)


ten_digits= list(itertools.permutations([0,1,2,3,4,5,6,7,8,9], 4))      # This takes all 4 elements  , generates a list of tuples
print ('There are', len(ten_digits),' unique Permutations between the ten digits :     \n', ten_digits)
print('And this is how you access a sub element from the array ::    ',ten_digits[4][3])

print('----'*15,'   PERMUTATION CHECK ','----'*15)


A, B =7418, 7814 ; print(A,B, type(A)) ; A, B =str(A),  str(B)  ; print(A,B,type(A)); print(sorted(A), sorted(B))#    (''7814)
print(type(A), type(B) == int)

def check_permutation(A , B):
   if ( type(A), type(B) == int ) :
      A, B = str(A), str(B)
      if ( type(A), type(B) == str ) :
         if ( sorted(A) == sorted(B) ) :
            print(A,' is a permutation of ', B)
            return True
         else:
            print(A,' is NOT a permutation of ', B)
            return False
      else: print('Not a string type !')

check_permutation('7152' , '2571')
print(check_permutation('7152' , '2571') == True)
print(check_permutation('8152' , '2571') == False)


print('----'*15,'   CIRCULAR NUMBER ','----'*15)
print('----'*10,'   testing ','----'*10)

print(0%4, 1%4, 2%4, 3%4)
print(1%4, 2%4, 3%4, 4%4)
print(2%4, 3%4, 4%4, 5%4)
print(3%4, 4%4, 5%4, 6%4)
print('\n')

A=6789
if len(str(A)) == 4: print("Yes. it is")

for v in range(len(str(A))):           # Loop for test, don't delete it because you may need it again
      a , i, j =  str(A), len(str(A)), len(str(A))
      s=''
      for c in range(j):
            print(a[(v+c) % j] ,end='  ')
            s += str((v+c) % j)
      print(s)
      v+= 1

print('\n','-------'*10)

def circulate_number(A):         # completed by Bogdan Trif @ 2016-09-15, 20:40
      for v in range(len(str(A))):
            a , i , s =  str(A), len(str(A)), ''
            for c in range(i):
                  #print(a[(v+c) % j] ,end='  ')
                  s += str(a[(v+c) % i])
            print(s)
            v+= 1

circulate_number(1234569)
#print([i for i in range(4)])

print('\n','===='*20)

