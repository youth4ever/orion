#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Mon, 14 Nov 2016, 13:39
#The  Euler Project  https://projecteuler.net
'''
                                            Anagramic squares       -       Problem 98
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 36**2.
What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 96**2.
We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted,
neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words,
find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
'''
import time
import string
from math import sqrt

dd = dict(enumerate(string.ascii_uppercase, start=1))       # Construct the dictionary of letters
# print(dict(enumerate(string.ascii_uppercase, start=1)))
D = dict(zip(dd.values(),dd.keys()))                    # Invert the dictionary
# print(D)

filename = "pb098_words.txt"
def load_file(filename):
    f = open(filename, 'r')
    line= f.readline()
    words = [i.strip('"') for i in line.split(',')]
    return words

words = load_file(filename)
print(words)

print('WORDS'[::-1])        # Backwards string

sq3 = [i*i for i in range(11, 31) if  len(set(str(i*i))) == 3 ]
sq4 = [i*i for i in range(32, 100) if  len(set(str(i*i))) == 4 ]        # if  len(set(str(i*i))) == 4 states for :  In general we want non-reapeating numbers, BUT:
sq5 = [i*i for i in range(101, 316) if  len(set(str(i*i))) >= 4 ]      # we put >=4 to account also the repeating letters of : THESE SHEET
sq6 = [i*i for i in range(102, 1000) if  len(set(str(i*i))) >= 5 ]     #  we put >=5 because  of : EXPECT EXCEPT, RECENT CENTRE, REFORM FORMER
sq7 = [i*i for i in range(1001, 3162) if  len(set(str(i*i))) == 7 ]
sq8 = [i*i for i in range(3163, 10000)  if  len(set(str(i*i))) == 8 ]
sq9 = [i*i for i in range(10001, 31622) if  len(set(str(i*i))) == 9 ]
print(sq5)

SQ={ 3 : sq3, 4 : sq4, 5: sq5 , 6 : sq6, 7: sq7 , 8 : sq8, 9: sq9 }


def anagramic_word(word1, word2, number):
    ''':Description:    This function works IIF word1 & word2 are anagramic  &
    number has the same number of digits as the letters in word1 & word2 . For the current purpose is ok. '''
    if len(str(number)) == len(word1) == len(word2):
        d = dict(zip(list(word1) , list(int(i) for i in str(number)) ) )
        # print(d)
        s = ''
        for i in word2:
            # print(d[i])
            s += str(d[i])
        return int(s)
    else : return 'Not ok !', number

print('--------------------------TESTS------------------------------')
print('\nTest for anagramic_word function  ',anagramic_word('WORTH' , 'THROW', 13689 ))


# Now I need to construct temp dictionary on each iteration mapping words with squares and
# then check if the second words arrange in a square

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def pb098():
    maxv, counter=0, 0
    for i in range(len(words)-1,-1,-1):
        for j in range(1 , i):                            # With first Element included is :     for z in range(0,y):
            a = sorted(words[i])
            b = sorted(words[j])
            if a == b    and words[i][::-1] != words[j] :       # Exclude palindrome words
                counter += 1
                # print(str(counter)+".  ",words[i],words[j])
                w1, w2 = words[i], words[j]
                # if len(set(str(words[i]))) != len(words[i]) :
                #     print('                                                      AHHHAAAAAA !')
                nrs = SQ[len(w1)]
                for k in range(len(nrs)):
                    if len(set(list(int(i) for i in str(nrs[k])))) == len(w1):      # Exclude repeating digits number not fitting the words unique letters
                        f =anagramic_word(w1, w2, nrs[k])
                        # print(w1,w2,nrs[k] ,f)
                        if sqrt(f) % 1 ==0 and len(str(f)) == len(str(nrs[k])):
                            print(w1, w2, nrs[k] ,f)
                            if maxv < max( nrs[k] ,f ):
                                maxv = max( nrs[k] ,f )
    return print('\n\nResult: ',maxv)

# pb098()                                     #  Result:  18769

print('\nCompleted in :', round( (time.time()- t1)*1000,6), 'ms\n\n')       # Completed in : 6426.367521 ms

print('\n================  My SECOND SOLUTION,  FAST ===============\n')

t1  = time.time()

wd4=[i for i in words if len(i)==4]
wd5=[i for i in words if len(i)==5]
wd6=[i for i in words if len(i)==6]
wd7=[i for i in words if len(i)==7]
wd8=[i for i in words if len(i)==8]
wd9=[i for i in words if len(i)==9]
WD={4 : wd4, 5: wd5 , 6 : wd6, 7: wd7 , 8 : wd8, 9: wd9 }

# print(len(wd4), wd4)

def pb098_upgraded():
    maxv, counter=0, 0
    for h in range(4,10):
        word_set = WD[h]
        for i in range(len(word_set)-1,-1,-1):
            for j in range(1 , i):                            # With first Element included is :     for z in range(0,y):
                a = sorted(word_set[i])
                b = sorted(word_set[j])
                if a == b    and word_set[i][::-1] != word_set[j] :       # Exclude palindrome words
                    counter += 1
                    # print(str(counter)+".  ",word_set[i],word_set[j])
                    w1, w2 = word_set[i], word_set[j]
                    nrs = SQ[len(w1)]
                    for k in range(len(nrs)):
                        if len(set(list(int(i) for i in str(nrs[k])))) == len(w1):      # Exclude repeating digits number not fitting the words unique letters
                            f =anagramic_word(w1, w2, nrs[k])
                            # print(w1,w2,nrs[k] ,f)
                            if sqrt(f) % 1 ==0 and len(str(f)) == len(str(nrs[k])):
                                # print(w1, w2, nrs[k] ,f)
                                if maxv < max( nrs[k] ,f ):
                                    maxv = max( nrs[k] ,f )
    return print('\n\nResult: ',maxv)

pb098_upgraded()                                     #  Result:  18769

print('\nCompleted in :', round( (time.time()- t1)*1000,6), 'ms\n\n')       # Completed in : 816.046715 ms
'''
print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, mbh038, England  --------------------------')
t1  = time.time()
# About 50 ms in Python. I find the anagrams in the word list and put them into a dictionary.
# I also create a dictionary of anagram square numbers, keyed by number of digits,
# keeping only those where all the digits are distinct. Doing this cuts down the number of matches
# that have to be made of anagram squares to anagram words by a factor of 30 or so.
# Then I match up the anagram words with the anagram square numbers of the same length,
# and note when I get a pair where one word maps the other to a square.

def asq(filename):
    wdic=readWords(filename)
    ags=anagrams(wdic)
    sqs={digits:asquares(digits) for digits in range(1+max([len(k) for k,v in ags.items()]))}
    sqmax=0
    for k,v in ags.items():
        asqs=sqs[len(k)]
        for x,y in asqs.items():
            w={v[0][i]:y[0][i] for i in range (len(v[0]))}
            nstr=''.join([w.get(v[j][kk],'X')for j in range(1,len(v)) for kk in range (len(v[j]))])
            if nstr in y and int(nstr)>sqmax:
                sqmax=int(nstr)
    print(sqmax)

def readWords(filename='p098_words.txt'):
    """returns dict of words in file, keyed by word length"""
    with open(filename) as f:
        words= [word for line in f for word in line.split('","')]
        maxlen=max([len(word) for word in words])
        return {l:[word for word in words if len(word)==l ] for l in range(1,maxlen+1) }

def anagrams(wdic):
    """returns dict of anagrams keyed by ordered string of letters in the anagram"""
    allwords={}
    for k,v in wdic.items():
        for j in range(len(v)):
            x="".join(sorted(v[j]))
            allwords.setdefault(x,[]).append(v[j])
    return {k:v for (k,v) in allwords.items() if len(v)>1}

def asquares(n):
    """returns dict of all anagramic integer squares with n digits, all digits being different"""
    squares = [str(x**2) for x in range(int(10**((n-1)/2))+(n+1)%2,int(10**(n/2))+n%2)]
    allsqs={}
    for square in squares:
        if len(square)>len(set(square)): #only take those where all digits are different
            continue
        x="".join(sorted(square))
        allsqs.setdefault(x,[]).append(square)
    return {k:v for (k,v) in allsqs.items() if len(v)>1}

asq(filename)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      #   Completed in : 123.007059 ms

print('\n--------------------------SOLUTION 2, froycard, Venezuela   --------------------------')
t1  = time.time()
# I had some trouble in understanding this problem... since I included 0 in my permutations,
# but it was not good way to solve this problem... anyway, after sorting out this issue,
# this is my coding (ugly but fast) in Python, it finds the solution in less that 0.2 seconds

f=open(filename)
wordFile=f.readline()

words={}
tmp=''
for i in wordFile:
	if i == '"':continue
	if i != ',':
		tmp+=i
		#print tmp
	else:
		#print tmp
		if len(tmp) in words:
			words[len(tmp)].append(tmp)
		else:
			words[len(tmp)]=[tmp]
		tmp=''


def findAnagrams(word):
	tmp=[]
	for i in range(len(word)-1):
		for j in range(i+1,len(word)):
			if sorted(list(word[i]))==sorted(list(word[j])):
				tmp.append((word[i], word[j]))
	return tmp


anagrams={}
for key in words:
    wordList=words[key]
    tmp=findAnagrams(wordList)
    if len(tmp)==0: continue
    if key in anagrams:
        anagrams[key]+=tmp
    else:
        anagrams[key]=tmp


var2=[i*i for i in range(4,10) if '0' not in str(i*i)]
var3=[i*i for i in range(10,32) if '0' not in str(i*i)]
var4=[i*i for i in range(32,100) if '0' not in str(i*i)]
var5=[i*i for i in range(100,317) if '0' not in str(i*i)]
var6=[i*i for i in range(317,1000) if '0' not in str(i*i)]
var8=[i*i for i in range(3163,10000) if '0' not in str(i*i)]
var9=[i*i for i in range(10000,31622) if '0' not in str(i*i)]

perm={}

for key in anagrams:
    if key == 2:
        perm[2]=var2
    if key == 3:
        perm[3]=var3
    if key == 4:
        perm[4]=var4
    if key == 5:
        perm[5]=var5
    if key == 6:
        perm[6]=var6
    if key == 8:
        perm[8]=var8
    if key == 9:
        perm[9]=var9

squares=[]
for key in anagrams:
    for i in anagrams[key]:
        for j in perm[key]:
            tmpDic={}
            tmp1=str(j)
            k=0
            for x in i[0]:
                tmpDic[x]=tmp1[k]
                k+=1
            if len(set(''.join(tmpDic.values()))) != len(''.join(tmpDic.values())):continue
            tmpStr=''
            for x in i[1]:
                tmpStr+=tmpDic[x]
            tmpStr=int(tmpStr)
            sqr=tmpStr**(.5)
            if sqr==int(sqr):
                squares+=[j]
                squares+=[tmpStr]

print (max(squares))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  Avi Levy, USA --------------------------')
t1  = time.time()
# Most of my code feels like "boilerplate", except for line 47. In this line, I permute the digits in a number
# according to a given pair of anagrams. It came out cleaner that expected!
from math import sqrt, floor

def digits(n): # exits early if there are repeated digits
  l = []
  while n:
    j = n % 10
    if j in l:
      return False
    l = [j] + l
    n//=10
  return l

def num(l): # turn digit list into a number
  n = 0
  while True:
    n += l.pop(0)
    if not l:
      break
    n *= 10
  return n

d = {} # hash a word to its letter multiset
for line in open(filename):
  for word in line.replace('"','').split(','):
    l = tuple(sorted(word))
    d[l] = [word] + d[l] if l in d else [word]

d = {k:v for k,v in d.items() if len(v) == 2}

best = 0
def checkSquare(anagram, nagaram):
  global best
  length = len(anagram)
  i = floor(sqrt(10**(length-1)))
  while True:
    j = i**2
    i += 1
    if j < 10**(length-1):
      continue
    if j >= 10**length:
      break
    p = digits(j)
    if not p or 0 in p:
      continue
    q = [0]*length
    for index, char in enumerate(anagram):
      q[nagaram.index(char)] = p[index]
    q = num(q)
    if q == int(sqrt(q))**2:
      best = max(best, q, j)

for k,v in d.items():
  checkSquare(v[0],v[1])
print(best)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, THE FASTEST  hansaplast, Switzerland --------------------------')
t1  = time.time()

from collections import defaultdict, Counter
from itertools import combinations as comb

def anagrams(words):
  anagrams = defaultdict(list)
  for word in words:
    anagrams["".join(sorted(word))].append(word)
  return [(len(anagrams[k][0]), anagrams[k]) for k in anagrams.keys() if len(anagrams[k]) > 1]

squares = [str(i*i) for i in range(1,round(10**7**0.5))]
max_square = 0
for length,anag in anagrams(eval("["+open(filename).read()+"]")):
  for length,squa in [s for s in anagrams(squares) if s[0] == length]:
    for a1,a2,s1,s2 in [(a1,a2,s1,s2) for a1,a2 in comb(anag,2) for s1,s2 in comb(squa,2)]:
      mapping = dict(zip(s1,a1))
      if "".join(map(lambda k:mapping[k],s2)) == a2:
        max_square = max(max_square,int(s1),int(s2))

print(max_square)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#

'''