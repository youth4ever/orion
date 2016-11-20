#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Mon, 14 Nov 2016, 23:32
#The  Euler Project  https://projecteuler.net
'''
                                            Roman numerals      -        Problem 89
For a number written in Roman numerals to be considered valid there are basic rules which must be followed.
Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

                                                                                IIIIIIIIIIIIIIII
                                                                                VIIIIIIIIIII
                                                                                VVIIIIII
                                                                                XIIIIII
                                                                                VVVI
                                                                                XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient,
as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid,
but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
Traditional Roman numerals are made up of the following denominations:
                                                                        I = 1
                                                                        V = 5
                                                                        X = 10
                                                                        L = 50
                                                                        C = 100
                                                                        D = 500
                                                                        M = 1000
Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
I can only be placed before V and X.
X can only be placed before L and C.
C can only be placed before D and M.
'''

import time

print('\n--------------------------TESTS------------------------------')

filename = "pb089_roman.txt"
def load_file(filename):
    f = open(filename, 'r')
    text= f.read()
    f.close()
    rom_num = [i for i in text.split('\n')]
    return rom_num

init_rom = load_file(filename)
print(len(init_rom) , init_rom)

            # MMMMCMLXXXXV        ;  LXXXX = XC
            # MMMDCCLXXXVIIII         ;   VIIII = IX
            # DCCCCIIII                       ;   DCCCC = CM
            # DCCCCIIII                        ;     IIII = IV
            # MCCCCLXXIX                  ;   MCCCC = MCD
            # MMMDCCCXXXXV        ;       CXXXX = CXL


def replace_roman(rnum):
    ''':Description: Use the dictionary ROMAN to shorten the roman numerals
    :param rnum:  string,  Must be a roman numeral like : 'MMMMDCCCCXXXXVI'
    :return:    another string which is a shortened version of the numeral    '''
# rnum = 'MMMDCCLXXXVIIII'
    ROMAN = {1: ['MCCCC', 'MCD'], 2: ['DCCCC', 'CM'], 3: ['CCCC', 'CD'], 4: ['LXXXX', 'XC'],\
         5: ['CXXXX', 'CXL'], 6: ['XXXX', 'XL'], 7: ['VIIII', 'IX'], 8: ['IIII', 'IV']}
    for j in ROMAN :
        # print(ROMAN[j][0], ROMAN[j][1] )
        u = rnum.find(ROMAN[j][0])
        if u != -1  :
            s = rnum
            rnum = rnum.replace(ROMAN[j][0], ROMAN[j][1] )
            # print( str(iter) + '.  ' ,  ROMAN[j][0], ROMAN[j][1]    ,u,'   ' , s ,'    ', rnum )
    return rnum


print( '\nTest replace_rom function : ',replace_roman('MMMDCCLXXXVIIII') )
print( 'Test replace_rom function : ',replace_roman('XXXXVIIII') )
print( 'Test replace_rom function : ',replace_roman('MMMMDCCCCXXXXVI') )
print( 'Test replace_rom function : ',replace_roman('MMMDCCCCXXXVIIII') )
print( 'Test replace_rom function : ',replace_roman('MMMCCCXXXXV') )
print( 'Test replace_rom function : ',replace_roman('CLXXXXIX') )
print( 'Test replace_rom function : ',replace_roman('MCCCCXXIIII') )
print( 'Test replace_rom function : ',replace_roman('DLXXXX') )
print( 'Test replace_rom function : ',replace_roman('MMCCCCXXXXV') )
print( 'Test replace_rom function : ',replace_roman('MMMMCCCLXXXXVII') )
print( 'Test replace_rom function : ',replace_roman('MDCCCLXXXX') )
print( 'Test replace_rom function : ',replace_roman('MMCCCLXXXXIX') )
print( 'Test replace_rom function : ',replace_roman('MMMCCCXXVIIII') )


ROMAN = {1: ['MCCCC', 'MCD'], 2: ['DCCCC', 'CM'], 3: ['CCCC', 'CD'], 4: ['LXXXX', 'XC'], \
                    5: ['CXXXX', 'CXL'], 6: ['XXXX', 'XL'], 7: ['VIIII', 'IX'], 8: ['IIII', 'IV']}
# print(ROMAN,'\n')

t = 'MMCCCLXXXXIX'
print( '\nFind Test :  ' ,t.find( 'LXXXX') )
print( 'Find Test : ' ,t.find( ROMAN[1][1]) )
print( 'Find Test : ' ,t.find( ROMAN[1][0]) )
print('\nReplace Test : ',t.replace('LXXXX', 'XC'))
print('Replace Test : ',t.replace(ROMAN[1][0], ROMAN[1][1] ))

print('\n================  My FIRST SOLUTION,  VERY FAST ===============\n')
t1  = time.time()

def pb089():
    final_rom=[]
    iter=0
    for s in init_rom:
        t = replace_roman(s)
        iter+=1
        # print( str(iter) + '.  ' ,  s ,'      ',  t )
        final_rom.append(t)
    # print(final_rom)
    initial = ''.join(init_rom)
    final =  ''.join(final_rom)
    # print('\n', initial,'\n',final)
    res = len(initial) - len(final)
    return print('\nAnswer: ', res)

pb089()                     #   Answer:  743

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')              # Completed in : 9.000778 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  mbh038, England --------------------------')
t1  = time.time()

def PE_0089(filename):

    rnalts=[('IIII','IV'),('VIV','IX'),('XXXX','XL'),('LXL','XC'),('CCCC','CD')
            ,('DCD','CL'),('DDDD','CM')]

    with open(filename,'r') as file:
        data  = file.readlines()
    romans= [''.join([x for x in line.rstrip()]) for line in data]

    initialcount,finalcount=0,0

    for line in romans:
        initialcount+=len(line)
        for kv_pair in rnalts:
            line=line.split(kv_pair[0])
            if len(line)==2:
                line=line[0]+kv_pair[1]+line[1]
            else: line=line[0]
        finalcount+=len(line)
    print(initialcount-finalcount)

PE_0089(filename)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  aolea, Spain --------------------------')
t1  = time.time()

with open(filename) as f:
    roman89 =f.read().splitlines()
print(roman89)
count = 0
for j in roman89:
    if 'IIII' in j:
        count = count + 2
for j in roman89:
    if 'VIIII' in j:
        count = count + 1
for j in roman89:
    if 'XXXX' in j:
        count = count + 2
for j in roman89:
    if 'LXXXX' in j:
        count = count + 1
for j in roman89:
    if 'CCCC' in j:
        count = count + 2
for j in roman89:
    if 'DCCCC' in j:
        count = count + 1
print(count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, deadPix3l  --------------------------')
t1  = time.time()

#!/usr/bin/env python
total=0
with open(filename,'r') as f:
    for line in f:
        orig = line

        line = line.replace('IIIII','V')
        line = line.replace('IIII','IV')
        line = line.replace('VV','X')
        line = line.replace('VIV','IX')
        line = line.replace('XXXXX','L')
        line = line.replace('XXXX','XL')
        line = line.replace('LL','C')
        line = line.replace('LXL','XC')
        line = line.replace('CCCCC','D')
        line = line.replace('CCCC','CD')
        line = line.replace('DD','M')
        line = line.replace('DCD','CM')
        total+=len(orig)-len(line)

print (total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  archeuclid   --------------------------')
t1  = time.time()

from re import search


def space_saved(rom):
    res = 0
    p = {4: 2, 5: 4, 6: 4, 7: 4, 8: 4, 9: 7}
    q = {'I': 'VIIII', 'X': 'LXXXX', 'C': 'DCCCC'}

    for l in ['I', 'X', 'C']:
        for n in range(9, 3, -1):
            if search('%s{%d}'%(l, n), rom) is not None:
                res += p[n]
                if n == 4:
                    if search(q[l], rom) is not None:
                        res += 1
                break

    return res

def p89():
    res = 0
    f = open(filename)
    for rom in f:
        res += space_saved(rom)
    return print(res)

p89()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, bancaldo, Italy  --------------------------')
t1  = time.time()

def filter_romans(path):
    with open(path) as inputfile:
        romans = [num.strip() for num in inputfile]
    startchr = sum([len(r) for r in romans])

    for bad, correct in [("VIIII", "IX"), ("IIII", "IV"),
                         ("LXXXX", "XC"), ("XXXX", "XL"),
                         ("DCCCC", "CM"), ("CCCC", "CD"),]:
        for roman in romans:
            index = romans.index(roman)
            if bad in roman:
                romans[index] = roman.replace(bad, correct)
    return startchr - sum([len(r) for r in romans])


if __name__ == "__main__":
    start = time.time()
    result = filter_romans(filename)
    print ("euler 89: %s\nElapsed time %ss." % (result, time.time() - start))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, charlie_mojocoa  --------------------------')
t1  = time.time()

def minimize_roman_numeral(roman):
  """Returns the minimized roman numeral from a valid roman numeral."""
  translations = [('DCCCC', 'CM'), ('CCCC', 'CD'), ('LXXXX', 'XC'),
                  ('XXXX', 'XL'), ('VIIII', 'IX'), ('IIII', 'IV')]

  for key, value in translations:
    roman = roman.replace(key, value)

  return roman


if __name__ == '__main__':
  diff = 0

  with open(filename, 'r') as f:
    for line in f:
      line = line.strip()
      min_roman = minimize_roman_numeral(line)
      diff += len(line) - len(minimize_roman_numeral(min_roman))

  print (diff)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
