
import random, time, winsound

SET = set()
DICT = dict()

for i in range(1, 10**6) :
    SET.add(i)
    DICT[i]=i


test_nr = [ random.randint(1, 10**8) for i in range(10**3) ]
print(len(test_nr))
###############         SET      ##########
t1  = time.time()

for i in test_nr :
    if i in SET :
        a=0


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*10**6, 6), 'micros\n')


#################   DICTIONARY    ########
t1  = time.time()


for i in test_nr :
    if i in DICT :
        a=0

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*10**6, 6), 'micros\n')

#######################

winsound.MessageBeep()

t1  = time.time()


# Test a matrix of the form 10**6 x 10**6

M=[]
for i in range(10**6) :
    tmp =[ random.randint(1, 10**8) for j in range(10**6) ]
    if i%10**5 == 0 : print(i)
    M.append(tmp)


M=[]

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n')

winsound.MessageBeep()
