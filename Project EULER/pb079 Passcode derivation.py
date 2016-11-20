#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Thu, 17 Nov 2016, 20:16
#The  Euler Project  https://projecteuler.net
'''
                            Passcode derivation     -       Problem 79
A common security method used for online banking is to ask the user for three random characters from a passcode.
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
The text file, keylog.txt, contains fifty successful login attempts.
Given that the three characters are always asked for in order,analyse the file so as to determine
the shortest possible secret passcode of unknown length.
'''
import time

filename = "pb079_keylog.txt"
def load_file(filename):
    f = open(filename, 'r')
    text= f.read()
    f.close()
    L = [i for i in text.split('\n')]
    return L

P = load_file(filename)
print(len(P) , '\n',P)

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

E=[]        # a list where we will put the password numbers
for i in P:
    e0, e1, e2 = int(i[0]), int(i[1]), int(i[2])
    if e0 not in E :
        E.append(e0)
    if e1 not in E :
        E.append(e1)
    if e2 not in E :
        E.append(e2)
    else :
        if E.index(e0) > E.index(e1):       # Here we swap indexes
            E[E.index(e0)], E[E.index(e1)] = E[E.index(e1)] , E[E.index(e0)]
        if E.index(e1) > E.index(e2):       # Here we swap indexes
            E[E.index(e1)], E[E.index(e2)] = E[E.index(e2)] , E[E.index(e1)]
    print(E)

res = ''.join( str(i) for i in E )
print('\nAnswer :  ',res)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

digits = [ set() for x in range(10) ]
hasDigit = set()
with open( filename, 'r' ) as f:
    for line in f:
        code = list( map( int, list( line.strip() ) ) )
        hasDigit.add(code[0])
        hasDigit.add(code[1])
        hasDigit.add(code[2])
        digits[code[1]].add(code[0])
        digits[code[2]].add(code[0])
        digits[code[2]].add(code[1])
res = [0] * len( hasDigit )
for d in hasDigit:
    res[len(digits[d])] = d
print( ''.join(map(str, res)) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, pedrotari7, Portugal  --------------------------')
t1  = time.time()
# Assuming that there are no digit repetitions, I just checked all the permutations for
#     the digits that show up in the keylog, until I found a valid sequence.

from itertools import chain,permutations

def check_valid(num,logins):
    for login in logins:
        if not (num.index(login[0]) < num.index(login[1]) < num.index(login[2])):
            return False
    return True

with open(filename,'r') as f:
    logins = set([tuple([int(d) for d in  ele]) for ele in f.read().split()])

for num in permutations(set(list(chain(*logins)))):
    if check_valid(num,logins):
        print (''.join([str(i) for i in num]))
        break

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, Complicated ,  muttonchops --------------------------')
t1  = time.time()

from itertools import permutations

def validate_passcode(passcode, login_num):
    """Check if candidate passcode matches a login_num(3x digits)"""
    c_nums = list(str(login_num))
    indexpos = []
    for i in c_nums:
        indexpos.append(passcode.index(i))
    # We only need to check if they are in correct order
    if indexpos[0] < indexpos[1] and indexpos[1] < indexpos[2]:
        return True
    else:
        return False

login_nums = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710,
              720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729,
              729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718,
              729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319,
              728, 716]

# No repeated digits implies that the passcode should contain one of each digit found in nums
digitset = set()
for num in login_nums:
    for d in list(str(num)):
        digitset.add(d)

print('Number of digits in passcode: ', len(digitset))

# check all permutations of the digits in the set of possible digits
for pcode in permutations(digitset):
    is_valid = True
    for num in login_nums:
        if not validate_passcode(pcode, num):
            is_valid = False
            break
    if is_valid:
        passcode = ''.join(list([str(n) for n in pcode]))
        print('Passcode: ', passcode)
t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, charlie_mojocoa, USA  --------------------------')
t1  = time.time()
# I created a directed graph and did a topological sort. Then I removed the disconnected nodes to create the shortest possible key.

import networkx as nx


def create_graph():
  graph = nx.DiGraph()
  for i in range(10):
    graph.add_node(str(i))

  return graph


if __name__ == '__main__':
  with open(filename, 'r') as f:
    graph = create_graph()
    for line in f:
      numbers = line.strip()
      for i in range(len(numbers) - 1):
        if numbers[i + 1] not in graph[numbers[i]]:
          graph.add_edge(numbers[i], numbers[i + 1])
    top_sort = nx.algorithms.topological_sort(graph)

    # remove disconnected nodes
    print( ''.join([x for x in top_sort if len(graph.in_edges(x)) != 0 or len(graph.out_edges(x)) != 0]))

create_graph()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, mnmaggs, England  --------------------------')
t1  = time.time()
# As there are 8 digits used in the attempts - no 4 or 5 - it's likely that the shortest passcode/key will have 8 digits.
# Let's assume that and see if it works: it does. None of the attempts use duplicates which means that the key
# doesn't either (or else it would not be the shortest possible).
# Create an ordered list of all the possible keys, and check each key against the 50 attempts.
# If any attempt fails, go on to the next key.
# The check is done by comparing the current attempt againts a reduced key, namely the key with all the digits removed
# except those in the attempt (retaining the order). The check passes if attempt == reducedkey.

from itertools import permutations

digits = ['0','1','2','3','6','7','8','9']

keys = permutations(digits, 8)
keys = [list(key) for key in keys]

with open(filename) as f:
    text = f.read().splitlines()

attempts = [[char for char in attempt] for attempt in text]

for key in keys:
    for attempt in attempts:
        reducedkey = [digit for digit in key if digit in attempt]
        if reducedkey != attempt:
            break
    else:                               # Executes only if for loop has completed
        print('Answer is {}'.format(key))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  calebchiam, Singapore  --------------------------')
t1  = time.time()
# Made use of the observation that the first digit of the sequence will only ever appear in the first 'column' of each digit.
# Add that to the passcode answer, then remove all mention of this digit in the 50 sequences.
# Repeat to find the 'first digit' of the remaining sequence, i.e. the 2nd, then 3rd, 4th and so on digits.
# I also notice euler already mentioned it on the first page, and yes the problem with this approach is
# that it can't handle situations where a digit appears in the passcode more than once.

ans = ''

num = open(filename, 'r')
nums = (num.read()).split("\n")

while len(nums) > 0:
    d_1st_column = set([n[0] for n in nums])
    d_2nd_column = set([n[1] for n in nums if len(n) > 1])
    d_3rd_column = set([n[2] for n in nums if len(n) > 2])

    not_1st_column = d_2nd_column.union(d_3rd_column)

    for d in not_1st_column:
        d_1st_column.discard(d)
    print(d_1st_column)
    digit = d_1st_column.pop()
    ans += digit
    for idx, seq in enumerate(nums):   # remove all mention of identified digit
        if seq[0] == digit:
            nums[idx] = seq[1:]
    nums = [x for x in nums if x != '']  # delete all sequences that have run out of digits

print(ans)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#
# print('\n--------------------------SOLUTION 7,    --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

