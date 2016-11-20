#!/usr/bin/python
# Solved by Bogdan Trif @   Tue, 27 Sep 2016, 11:51
#The  Euler Project  https://projecteuler.net
'''
Names scores        -       Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
'''

f = open(r'pb022_names.txt', 'r')
line= f.readline()
#print(line)
names = [i.strip('"') for i in line.split(',')]
print(names)
names = sorted(names)
print(names)
#for i in names: print(i, end=' ')

alphabet={'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13,\
          'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26, }
#for i, j in alphabet.items(): print(i, end = ' ' )

a, b  = alphabet.keys(), alphabet.values() ; print(a, b)
print('\n------------------THE COMPUTATION --------------------')


big_SUM=0
counter=0
for nm in names:
    counter+=1
    S=0
    for j in nm:
        S+= alphabet[j]
    #print(str(counter)+'.   ',' Sum : ',S ,type(nm), nm,' ;   Score:   ' ,counter*S, ' ; ', big_SUM)       # Detailed information
    big_SUM += counter*S

print('\n The Total Sum of all the  Score of all names  is : ',big_SUM)
