#!/usr/bin/python3
# Solved by Bogdan Trif @ Completed on Sun, 18 Sep 2016, 12:35
#The  Euler Project  https://projecteuler.net
'''
Digit cancelling fractions      -       Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
natural=[x for x in range(10,100) if ( x%10!=0 )]
#print(natural)
frac=[]

counter=0
for x in range(len(natural)):
    for y in range(x):
        counter += 1
        a = int(str(natural[y])[0])
        b = int(str(natural[x])[1])
        c = int(str(natural[y])[1])
        d = int(str(natural[x])[0])
        if (a/b <1 and natural[y]/natural[x] == a/b and c==d) :
            frac.append(a/b)
            print(str(counter)+".  ",natural[y],natural[x],'   ',a,b,'  ',a/b)

el_nr=len(natural)
print('The number of combinations between two elements of the array is:  ',el_nr*(el_nr-1)/2, counter)
x=1
for i in frac:
    x *=i
    print('Term  : ', x)
print('The answer is :', round(1/x))


##################################################

print('\n------------- OTHER SOLUTIONS FROM THE FORUM : ---------------')

def solution():
    result = float(1)
    for n1 in range(1,10):
        for n2 in range(1,10):
            for d1 in range(1,10):
                n = n1*10+n2
                if n1/d1 in (n/(d1*10+n2),n/(n2*10+d1)) and n1/d1 < 1:
                    result *= n1
                    result /= d1
                if n2/d1 == (n/(d1*10+n1),n/(n1*10+d1)) and n2/d1 < 1:
                    result *= n2
                    result /= d1
    return(1/result)
print(solution())