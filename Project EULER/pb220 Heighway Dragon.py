#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                            Heighway Dragon     -       Problem 220

Let D0 be the two-letter string "Fa". For n≥1, derive Dn from Dn-1 by the string-rewriting rules:

"a" → "aRbFR"
"b" → "LFaLb"

Thus, D0 = "Fa", D1 = "FaRbFR", D2 = "FaRbFRRLFaLbFR", and so on.

These strings can be interpreted as instructions to a computer graphics program,
with "F" meaning "draw forward one unit", "L" meaning "turn left 90 degrees",
"R" meaning "turn right 90 degrees", and "a" and "b" being ignored.
The initial position of the computer cursor is (0,0), pointing up towards (0,1).

Then Dn is an exotic drawing known as the Heighway Dragon of order n.
For example, D10 is shown below; counting each "F" as one step,
the highlighted spot at (18,16) is the position reached after 500 steps.

What is the position of the cursor after 1012 steps in D50 ?
Give your answer in the form x,y with no spaces.
'''

import time
import math

def findnth(source, target, n):
    num = 0
    start = -1
    while num < n:
        start = source.find(target, start+1)
        if start == -1: return -1
        num += 1
    return start

def replacenth(source, old, new, n):
    p = findnth(source, old, n)
    if n == -1: return source
    return source[:p] + new + source[p+len(old):]


def get_next_orientation( current_orientation, operation):
    # Left, Righ, Up, Down - L, R, U, D
    o = 'RULD'
    if operation == 'L' :
        i = o.find(current_orientation)
        return o[ (i+1)%4 ]
    if operation == 'R' :
        i = o.find(current_orientation)
        return o[(i-1)%4]


def path_sequence_gen(iterations) :
    a =  'aRbFR'
    b = 'LFaLb'
    H = 'FaRbFR'

    for d in range(1, iterations) :
        a_cnt = H.count('a')
        ind =1
        for i in range(a_cnt):
            # print('before -- >   ' ,H, len(H))
            H = replacenth(H, "a", a, ind)
            # print(ind,    H, len(H), '   <-- a  after')
            ind+=1
            # print('before -- >   ',  H, len(H) )
            H = replacenth(H, "b", b, ind)
            # print(ind,  H, len(H),  '   <-- b   after')
            ind+=1
    return H



def log_spiral_pow_of_2( power_lim ) :
    LOG2 = { 0 : (0,1) , 1:( 1, 1 ) ,2 : ( 2,0 ) }
    i=2
    x, y = 2, 0
    r = math.sqrt(x**2+y**2 )
    theta = 0*math.pi/180
    # print(str(i)+'.   ( x,y ) = ', x, y, '     angle= ', theta, '    r=', r)

    while i < power_lim :
        theta = (theta - 45)%360
        r *= math.sqrt(2)
        x = round(r * math.cos(theta*math.pi/180))
        y = round(r * math.sin(theta*math.pi/180))
        i+=1
        # print(str(i)+ '.   ( x,y ) = ', x, y, '     ;  theta =', theta, '  ;    r=', r)
        LOG2[i] = (x,y)
    return LOG2


nr = 10**12 - 2**39
print('\nLeft number : ', nr,'\n')

def decompose_in_2_powers(nr):
    X = []
    while nr > 0 :
        l = math.floor(math.log2(nr))
        # print('power = ',l, '     ', nr , '          ',2**l, )
        nr -= 2**l
        X.append(l)
    # print('\nVerification Sum :\t', sum([2**i for i in X]), X,'\n')

    return X

print('decompose_in_2_powers : \t' ,decompose_in_2_powers(6384) )

def get_point_coord(nr_of_steps) :

    N = decompose_in_2_powers(nr_of_steps)
    L = log_spiral_pow_of_2(int(math.log2(nr_of_steps)))
    # print(N, '\n',L)
    x , y = L[N[0]][0],  L[N[0]][1]
    for i in range(1, len(N) ):
        # print('(x , y) = ', (x, y))
        x -= L[N[i]][0]
        y -= L[N[i]][1]
    return x, y

n= 971
print('\n get_point_coord ', n ,'steps : \t' , get_point_coord(n) )




print('log_spiral_pow_of_2 : \t', log_spiral_pow_of_2(40))




print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# D15 = the Generated Sequence :  131070




# print('\n-------- Next Orientation Tests ------------')
# print('\nget_next_orientation : \t', get_next_orientation('R', 'L' ))
# print('get_next_orientation : \t', get_next_orientation('R', 'R' ))
# print('get_next_orientation : \t', get_next_orientation('L', 'R' ))
# print('get_next_orientation : \t', get_next_orientation('L', 'L' ))
# print('get_next_orientation : \t', get_next_orientation('D', 'L' ))
# print('get_next_orientation : \t', get_next_orientation('D', 'R' ))
# print('get_next_orientation : \t', get_next_orientation('U', 'L' ))
# print('get_next_orientation : \t', get_next_orientation('U', 'R' ))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n================  My Initial Testing SOLUTION,   ===============\n')
t1  = time.time()


def construct_path(iterations) :
    H = path_sequence_gen(iterations)
    # print('\nthe Generated Sequence : ', len(H) , '\n', H[:1000] ,'\n\n\n')
    # [2, 6, 14, 30, 62, 126, 254, 510, 1022, 2046, 4094]

    orientation = 'U'
    pos = [0, 0]
    cnt = 0
    for s in H :
        if s == 'a' or s=='b' : continue
        if s == 'F' :
            if orientation == 'U' :             pos[1]+=1
            if orientation == 'D' :            pos[1]-=1
            if orientation == 'R' :            pos[0]+=1
            if orientation == 'L' :            pos[0]-=1
            cnt+=1
            coord = get_point_coord(cnt)
            if pos[0] != coord[0] or pos[1] != coord[1] :
            # if pos[0] == coord[0] and pos[1] == coord[1] :
                print(str(cnt)+'.      Orientation : ', orientation,'      Position : \t', pos, '   ' ,coord ,' = get_point_coord  ' )
            # if pos == [18,16] :             print(str(cnt)+'.      =====>    Position', pos)

            if cnt == 10000 :
                print(str(cnt)+'.      =====>    Position', pos)
                break

        if s == 'L' or s =='R' :         orientation = get_next_orientation( orientation  , s )


construct_path(10)

print('\n--------------TEST OF FUNCTIONS --------------------\n')


nr_of_steps = 59

N = decompose_in_2_powers(nr_of_steps)
L = log_spiral_pow_of_2(int(math.log2(nr_of_steps)))
print('pow of 2 : \t\t', N , '\ncoord at 2 powers : \t\t', L)

x , y = L[N[0]][0],  L[N[0]][1]

for i in range(1, len(N) ):
    print('(x , y) = ', (x, y) )
    x -= L[N[i]][0]
    y -= L[N[i]][1]
    # if N[0] % 2 == 1 :
    #     if N[i] %2 == 1 :
    #         x += L[N[i]][0]
    #         y += L[N[i]][1]
    #     if N[i] %2 == 0 :
    #         x -= L[N[i]][0]
    #         y -= L[N[i]][1]
    #
    # if N[0] % 2 == 0 :
    #     if N[i] %2 == 1 :
    #         x -= L[N[i]][0]
    #         y -= L[N[i]][1]
    #     if N[i] %2 == 0 :
    #         x += L[N[i]][0]
    #         y += L[N[i]][1]



print('\n The Coordinates after  ', nr_of_steps ,'steps : \t' , ( x, y ) )


print('\n------------------------------')
#############


# The final steps to complete . Calculations fail for some values. Find why & calibrate :
# @2017-01-25, 11:53   -->  I must calibrate the function

######################
print('\n--------------- FINAL CALCULATIONS')




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# H = path_sequence_gen(2)		4.      Orientation :  R       Position : 	 [2, 0]
# H = path_sequence_gen(3)		8.      Orientation :  R       Position : 	 [2, -2]
# H = path_sequence_gen(4)		16.      Orientation :  R       Position : 	 [0, -4]
# H = path_sequence_gen(5)		32.      Orientation :  R       Position : 	 [-4, -4]
# H = path_sequence_gen(6)		64.      Orientation :  R       Position : 	 [-8, 0]
# H = path_sequence_gen(7)		128.      Orientation :  R       Position : 	 [-8, 8]
# H = path_sequence_gen(8)		256.      Orientation :  R       Position : 	 [0, 16]
# H = path_sequence_gen(9)		512.      Orientation :  R       Position : 	 [16, 16]
# H = path_sequence_gen(10)		1024.      Orientation :  R       Position : 	 [32, 0]
# H = path_sequence_gen(11)		2048.      Orientation :  R       Position : 	 [32, -32]
# H = path_sequence_gen(12)		4096.      Orientation :  R       Position : 	 [0, -64]
# H = path_sequence_gen(13)		8192.      Orientation :  R       Position : 	 [-64, -64]
# H = path_sequence_gen(14)		16384.      Orientation :  R       Position : 	 [-128, 0]

# @ iter = 549755813888 = 2**39 --> pos = [-524288 , 524288 ]
# need to find the difference : 10**12 - 2**39
# I know how to solve this problem, I work only with differences !!!



# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#




