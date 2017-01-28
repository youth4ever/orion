#!/usr/bin/python3
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                            Su Doku     -   Problem 96
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept.
Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar,
and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however,
is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column,
and 3 by 3 box contains each of the digits 1 to 9.
Below is an example of a typical starting puzzle grid and its solution grid.

                +-----------------------+         +-----------------------+
                   | 0 0 3 | 0 2 0 | 6 0 0 |         | 4 8 3 | 9 2 1 | 6 5 7 |
                   | 9 0 0 | 3 0 5 | 0 0 1 |         | 9 6 7 | 3 4 5 | 8 2 1 |
                   | 0 0 1 | 8 0 6 | 4 0 0 |         | 2 5 1 | 8 7 6 | 4 9 3 |
                   |-------+-------+-------|         |-------+-------+-------|
                   | 0 0 8 | 1 0 2 | 9 0 0 |         | 5 4 8 | 1 3 2 | 9 7 6 |
                   | 7 0 0 | 0 0 0 | 0 0 8 |         | 7 2 9 | 5 6 4 | 1 3 8 |
                   | 0 0 6 | 7 0 8 | 2 0 0 |         | 1 3 6 | 7 9 8 | 2 4 5 |
                   |-------+-------+-------|         |-------+-------+-------|
                   | 0 0 2 | 6 0 9 | 5 0 0 |         | 3 7 2 | 6 8 9 | 5 1 4 |
                   | 8 0 0 | 2 0 3 | 0 0 9 |         | 8 1 4 | 2 5 3 | 7 6 9 |
                   | 0 0 5 | 0 1 0 | 3 0 0 |         | 6 9 5 | 4 1 7 | 3 8 2 |
                   +-----------------------+         +-----------------------+

A well constructed Su Doku puzzle has a unique solution and can be solved by logic,
although it may be necessary to employ "guess and test" methods in order to eliminate options
(there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle;
the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles
ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid;
for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
'''
# Generate a 9x9 Matrix
from macpath import split
from copy import copy, deepcopy
from itertools import count
from numpy import transpose
import hashlib, time

#  ::::::::::::::::::::::::::::::         DIFFERENT METHODS TO LOAD A FILE          ::::::::::::::::::::::::::::::  #

filename = "pb096_test_matrix.txt"

def load_file_1(filename):
    M=[]
    with open(filename) as f:
        M = [list(map(int, line.rstrip('\n') )) for line in f.readlines()]
    return M

def load_file_2(filename):
    M=[]
    with open(filename, 'r') as f :
        for line in f :
            # print(line, type(line))
            M.append([ int(i) for i in line.rstrip('\n') ])
    return M

def load_file_3(filename) :
    matrix=[]
    f = open(filename, 'r')
    text = f.read()
    for row in text.split('\n'):
        matrix.append(list(map(int, row)))
    return matrix

M = load_file_1(filename)
print(M)

print('\n-------------  TESTS -----------------')

def status(M):
    digits = {}
    for i in range(len(M)):
        for j in range(1,10):
            #print(M[i],'  ', j ,M[i].count(j))
            if j in M[i] :
                if j not in digits: digits[j] = 1
                else : digits[j] = digits[j]+1
    return digits

print('Status: ',status(M))

digits = {}
for i in range(len(M)):
    for j in range(1,10):
        #print(M[i],'  ', j ,M[i].count(j))
        if j in M[i] :
            if j not in digits: digits[j] = 1
            else : digits[j] = digits[j]+1


def SubMatrix_3x3(x, y, M ):
    '''Function which cuts a given matrix  in 3x3 SubMatrices. In a 9x9 matrix there will be 9 3x3 matrices called Ninants
     Based on the position coordinate (x,y) returns the corresponding Ninant.
     Note: x, y values go from 1 up. 0 is excluded. Don't confuse with referencing matrix like M[0]
    :returns
    Returns the Ninant where the coordinate (x,y) lies in.    '''
    N =  M[((x-1)//3)*3 : ((x-1)//3)*3+3 ]      # This complicated expression do the work of slicing the list into sub pieces
    return [row[((y-1)//3)*3 : ((y-1)//3)*3+3] for row in N]

def intersection(nr, x, y, M):
    ''':Description:    It checks if a number is on the row, column or 3x3 subMatrix of the indexes x,y. The
        function has been made specifically for Sudoku Matrices.
    :param nr:  is the number to test : 1...9
    :param x:   row index   1...9
    :param y:   column index    1...9
    :param M:   the matrix which is tested, Must be a 9x9 matrix
    :return:    Returns boolean : True if the number already exists, False otherwise
    '''
    if ( nr in M[x-1]  or  nr in  transpose(M)[y-1] ) or \
             ( True  if  True in [ nr in row for row in SubMatrix_3x3(x, y, M) ]  else False )    :
        return True
    else : return False

# print('\n SubMatrix :   ',SubMatrix_3x3(5, 6,M),'\n')
# print( [ 8 in row for row in SubMatrix_3x3(5,6)])
print( True  if  True in [ 7 in row for row in SubMatrix_3x3(1,1,M) ]  else False)        # Nice List Comprehension Construction, @Bogdan Trif


# print(((x-1)//3)*3, ((x-1)//3)*3+3)
# print('Get last 3 columns of a matrix : ',  [row[-3:] for row in M])
print('------------ Intersection Test ----------')

print('\nIntersection Test :      ',intersection(1, 3, 7, M),'\n')
for i in range(1,10):
    print(i ,intersection(i, 3 , 5, M), end='  ')


print('\n---------------------------')

def get_to_fill_status(M):
    ''':Description: Important function which get the *FILL STATUS* of the matrix.
    :param M:   the matrix to be tested
    :return:    a **dictionary** in the following format:
        :key: as the *xy* position in the matrix
        :value: as a list of 9 boolean corresponding to each number.
        E.g. :  {'94': [False, False, True, False, True, False, True, False, False], *3-rd* value in list is *False*
         which means that the number *3* at position *x=9, y=4* cannot be filled because of the intersection
     :NOTE:     It depends on the **intersection function** which returns the boolean    '''
    sudoku={}
    for x in range(1,10):
        for y in range(1,10):
            if M[x-1][y-1] == 0 :
                # print('------ Position  ',x, y,'  --------------')
                answer=[]
                sudoku[str(x)+str(y)]=[]
                for n in range(1,10):
                    # print('Nr: ',n , '     x=',x,'  y=',y ,'    ' ,intersection(n, x , y))
                    answer.append(intersection(n, x , y, M))
                    sudoku[str(x)+str(y)].append(intersection(n, x , y, M))
                # print(answer.count(False))
    return sudoku

print('get_to_fill_status Function : ' ,get_to_fill_status(M) ,'\n')


def one_available_spot(M):
    ''':Description:    check if there are positions in the matrix which can be filled **only** with **1**  number
    :return: boolean:   *True* if there are fields with only one possibility to fill a number, otherwise *False*
    :NOTE:  Depends on the function get_to_fill_status    '''
    return 1 in [ h.count(False) for h in  [i for i in get_to_fill_status(M).values()]   ]

def two_available_spots(M):
    ''':Description:    check if there are positions in the matrix which can be filled **only** with **2** numbers
    :return: boolean:   True if there are fields with only one possibility to fill a number, otherwise false
    :NOTE:  Depends on the function get_to_fill_status    '''
    return 2 in [ h.count(False) for h in  [i for i in get_to_fill_status(M).values() ] ]


def no_more_zeros(M):
    '''Returns True if the Matrix is still containing zeros , otherwise False
    '''
    # print('Get 0  non-filled positions : ', [ h.count(0) for h in  [i for i in M]   ]  )
    val = sum([ h.count(0) for h in  [i for i in M] ])
    # val = False in [ i for i in [ val for sublist in get_to_fill_status(M).values() for val in sublist ]  ]
    if val >0 : return False
    else : return True

def get_status(M):
    ''':Description:    Count how many times the  numbers 1-9 have been used.
        If all the numbers have been used returns True, otherwise False.
    :param M:   matrix M
    :return: boolean: True or False
    :NOTE:  Depends on the status function
    '''
    s = status(M).values()
    if  ([i for i in s ].count(9) == 9) == True :
        return True
    else : return False

def validate_final(M):
    ''':Description:    Check if the Matrix has been completed. Check if for every number 1-9
        at every position from (1,1) to (9,9) is a valid choice. The function gives boolean True
        if all the numbers have been filled correctly and thus the sudoku has been solved.
    :param M:   the matrix to test
    :return:    boolean: True or False
    :NOTE:      It depends on the intersection function
    '''
    def All_Positions_Intersection(M):
        V = []
        for x in range(1,10):
            for i in range(1,10):
                for j in range(1,10):
                    V.append( intersection(x, i , j, M) )
        if V.count(True) == 9**3 :  return True
        else : return False
    s = status(M).values()
    if  ([i for i in s ].count(9) == 9) == True and All_Positions_Intersection(M) == True:
        return True
    else : return False


def check_doubles(M):
    ''':Description:    check if there are values 2 times or more at a position. Checks if
        there are >1 numbers on a row, a column or a 3x3 subMatrix. If there are duplicate
        numbers return True, returns False if all the numbers are Unique.
    :param M:   the matrix to test
    :return:    boolean:    True if there are duplicates, False if all are unique    '''
    for x in range(1,10):
        for i in range(1,10):
            row = M[i-1]
            col = transpose(M)[i-1].tolist()
            if row.count(x) > 1 == True or col.count(x) >1 == True :
                res1 = True
            else: return False
            # print(row.count(x) > 1 ,row.count(x) , type(row),x,i )
            # print( col.count(x) >1 , col.count(x) ,type(col),x,i )
        for i in range(2,10,3):
            for j in range(2,10,3):
                submatrix = [val for sublist in SubMatrix_3x3(i,j,M) for val in sublist]
                # print(submatrix, x,  i, j)
                if submatrix.count(x) > 1 == True  :
                    # print('True', x,i,j)
                    res2 = True
                else: return False
        if res1 == True and res2 == True:
            return True


def get_1_choice_position(M):
    ''':Description:    Prints out the positions which have **ONLY  1 CHOICE**     '''
    melodia={}
    sudoku = get_to_fill_status(M)
    for k, v in sudoku.items() :
        # print(k, v , v.count(False)     ,end=' ')
        if v.count(False) ==1 :
            number = v.index(False)+1
            position = [int(i) for i in list(k)]
            melodia[k] = number
            # print('position: ',position , v, '  choice: ',number )
        # else : print('\nNo more 1 Choice')
    if len(melodia) != 0 : print('1 Possibility  :  ',melodia)
    else: print('1 Possibility : None')

def get_2_choices_positions(M):
    ''':Description:    Prints out the positions which have **2 CHOICES**     '''
    memom={}
    sudoku = get_to_fill_status(M)
    for k, v in sudoku.items() :
        # print(k, v , v.count(False)     ,end=' ')
        if v.count(False) == 2 :
            position = [int(i) for i in list(k)]
            z = [i+1 for i, x in enumerate(v) if x == False ]
            memom[k] = z
            # del(memom[k][1])
            # print( 'position: ', position , v,'  choices: ', z )
        # else : print('No more 2 Choices')
    if len(memom) != 0 : print('2 Variants :  ',memom)
    else: print('2 Variants : None')

print( '\n---------------------------- Test for spots ---------------------')
print('Test one_available_spot Function : ', one_available_spot(M))
print('Test two_available_spots Function : ', two_available_spots(M),'\n\n')

print('Prints out the positions which have ONLY  1 CHOICE : ' ) ; get_1_choice_position(M)
print('Prints out the positions which have 2 CHOICES : ' ) ; get_2_choices_positions(M)

print('----------------------------------------------------------- \n')


#############        END    DEFINITIONS        ####################
t1  = time.time()


# @ 2017-01-20, 22:42     I must rebuild the main program as it has many flaws !!! TOO COMPLICATED !!!
# Also, many functions can be simplified !!!




#
# global SuperFlag
# SuperFlag = False

def fill_1_available_position(M):       # CASE 1
    sudoku = get_to_fill_status(M)
    if one_available_spot(M) == True :
        for k, v in sudoku.items() :
            # print(k, v , v.count(False)     ,end=' ')
            if v.count(False) == 1 :        #  if only 1 False it can be completed with the number
                number = v.index(False)+1
                position = [ int(i) for i in list(k) ]
                print(position , ' completed with  value: ',number, '   ', v    ,'           <--   CASE  1 ')
                M[position[0]-1 ] [position[1]-1 ] = number
                return M    # only one at a time
    if one_available_spot(M) == False : return False




memo=[]
def fill_2_available_positions(M, memo ):       # CASE 2
    if two_available_spots(M) == True and one_available_spot(M) == False  :     # <--- Take Care here, Two False
        if len(memo) == 0 :
            A = deepcopy(M)
            print('\n\n      ################         matrix A was created (memo is empty) ############:\n',A)

    sudoku = get_to_fill_status(M)
    for k, v in sudoku.items() :
        # print(k, v , v.count(False)     ,'  % % % % % % % % %% %   ')
        if v.count(False) == 2 :
            position = [int(i) for i in list(k)]
            z = [i+1 for i, x in enumerate(v) if x == False ]
            first_choice = str(k)+str(z[0])
            memo.extend( [ first_choice , str(k)+str(z[1]) ]  )
            print(memo, memo[0][2] ,  position)
            print( 'position :', position , '  choices: ', z , '    ',memo ,'       ' , v, '       <-- CASE 2 False Status  ' )

            # if intersection( int(memo[0][2]) , position[0]-1 , position[1]-1, M ) == False :  # Here we check if the intersection is valid :

            M[position[0]-1 ] [position[1]-1 ] = int(memo[0][2])                             # check row, column and 3x3 SubMatrix
            print(int(memo[0][2]),' added at', position)
            memo.remove( memo[0] )
            print( memo ,M[position[0]-1 ] ,'       <-- CASE 2 False: Confirmation   ' )
            print(M)
            # print(get_to_fill_status(M))
            break   # only one at a time
    return M, memo


while 1 :
    if one_available_spot(M) == True :
        fill_1_available_position(M)
    else :
        print(M)
        fill_2_available_positions(M, memo)
        break



    # if SuperFlag == True  :       # Failed case 2
    #
    #     case_3()

    # return M


def case_3():           # !!!!!!!!!!!!!!   CASE 3     !!!!!!!!!!!!!!!
    sudoku = get_to_fill_status(M)
    for k, v in sudoku.items() :
        # print(k, v , v.count(False)     ,end=' ')
        if v.count(False) == 2 :
            if len(memo) == 0:
                SuperFlag = False    # when finish with the replacement of the failed cases, go back to the normal case
                print('SuperFlag was changed to False  from CASE 3 !!!')
            else :
                key = list(memo.keys())[0]
                position = [int(i) for i in list(key)]
                print( position ,'    ',memo ,'     ',v ,'       <-- CASE 3 False Status   ' )
                # print('==>   Memo Keys :     '  ,memo.keys(), '       ',memo)
                # print('Position:    ==>  ',position,'    ==> ', key)
                # print(intersection( memo[key][0] , position[0]-1 , position[1]-1, M ), memo[key][0], position[0]-1, position[1]-1,'\n',M)
                if intersection( memo[key][0] , position[0]-1 , position[1]-1, M ) == True :       # Here we check if the intersection is valid :
                    M[position[0]-1 ] [position[1]-1 ] = memo[key][0]                                   # check row, column and 3x3 SubMatrix
                    try : memo.pop(str(key), None)
                    except KeyError:   pass
                    print(key,' from this key ', M[position[0]-1 ] [position[1]-1 ],  'was added  at position', position , '        ' ,memo, '        ->1  ' )
                else:
                    try: memo.pop(str(key), None)
                    except KeyError:   pass
                    print(key,' key was deleted. It does not match.             ', memo, '        ->2  ')




            break   # only one at a time
    return M





print('\n------------------------------------------------')
print('Check for remaining zeros : ' ,     [ val for sublist in M for val in sublist ].count(0) > 0        )
print( 'Validate Completion Correct : ', validate_final(M) )


print('\n------------------------------------------------')
print('\n----------------  TEST for CASE 3 -------------------------')

def main_case_3_test():
    global memo, A, M, SuperFlag
    M = [[3, 6, 5, 1, 7, 0, 2, 4, 9], [2, 7, 9, 6, 5, 4, 1, 8, 3], [8, 4, 1, 0, 2, 3, 5, 6, 7], [1, 9, 7, 3, 4, 6, 8, 5, 2], [4, 5, 2, 7, 1, 8, 3, 9, 6], [6, 8, 3, 5, 9, 2, 7, 1, 4], [7, 2, 8, 4, 6, 1, 9, 3, 5], [5, 1, 6, 9, 3, 7, 4, 2, 8], [9, 3, 4, 2, 8, 5, 6, 7, 1]]
    A = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 7, 9, 0, 5, 0, 1, 8, 0], [8, 0, 0, 0, 0, 0, 0, 0, 7], [1, 9, 7, 3, 4, 6, 8, 5, 2], [4, 5, 2, 7, 1, 8, 3, 9, 6], [6, 8, 3, 5, 9, 2, 7, 0, 0], [7, 0, 0, 0, 0, 0, 0, 0, 5], [0, 1, 6, 0, 3, 0, 4, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    M=A.copy()
    print(M,'\n')

    memo = {'97': [9], '17': [5], '36': [9], '99': [3], '18': [6], '14': [8]}
    SuperFlag = True
    case_3()
    print(memo)
    print(M,'\n')
    case_3()
    print(memo)
    print(M, '\n')



def main():         # The MAIN PROGRAM !!!
    global memo, A, SuperFlag, M               # Do not move them from here !!!!
    A,  SIGN, SuperFlag =  [], [] , False
    # memo = {}
    for i in range(1, 50):
        print('\n     =====      STEP ',i,'     =====' ), fill_available_position(M)

        print(M ,'\nMemo:        ' ,memo)
        get_1_choice_position(M) ;  get_2_choices_positions(M)        # just printing the available variants
        print('\nVALIDATIONS        : Validate Final= ',validate_final(M),   ' ;  No more Zeros= ', no_more_zeros(M), ' ;  Check Doubles= ', check_doubles(M))
        # X = M.copy() ;  Y = str(X)              # We want to make md5 hashes to be able to compare
        # signature = hashlib.md5(Y.encode()).hexdigest()
        # SIGN.append(signature)
        # print(SIGN[i-1], SIGN[i-2], ' Condition Check: '  , SIGN[i-1] == SIGN[i-2] ,' --> SuperFlag: ',SuperFlag) #  Now we want to compare the previous signature of the matrix with the current one

        # if len(SIGN)>2 and  SIGN[i-1] == SIGN[i-2] :        # i-1 is the last the current element, & i-2 is the last elem
        #     SuperFlag = True
        #     M = deepcopy(A)
        #     print('\n #########   matrix M was brought back to the initial completion phase #########) :\n\n', M)

        if check_doubles(M) == True : break

        if validate_final(M) == True :
            print('\nCONGRATULATIONS !! SUDOKU Magic Puzzle has been Correctly Solved ! \n ')
            print('=='*15)
            print('  +++++   ', M[0] ,'   +++++  ')
            print('  +++++   ', M[1] ,'   +++++  ')
            print('  +++++   ', M[2] ,'   +++++  ')
            print('  +++++   ', M[3] ,'   +++++  ')
            print('  +++++   ', M[4] ,'   +++++  ')
            print('  +++++   ', M[5] ,'   +++++  ')
            print('  +++++   ', M[6] ,'   +++++  ')
            print('  +++++   ', M[7] ,'   +++++  ')
            print('  +++++   ', M[8] ,'   +++++  ')
            print('=='*15,'\n\n')
            break


# if __name__ == "__main__": main()

print('\n\n--------------------------------------')
print('Final Mecanic:  ',M)
print('\nStatus: ',status(M))
print('Validate Final :  ',validate_final(M))
print(get_status(M))

# while no_more_zeros(M) == False :       # The main loop
#     fill_available_position(M)
#     print('loop   ',M, memo)
#     if validate_final(M) == False :
#         SuperFlag = True
    #     while no_more_zeros(M) == False :
    #         fill_available_position(M)
    #         print('loop   ',M, memo)
    # else: print('\nCONGRATULATIONS !!!')



print('\n===================Mecanic ==============   \n', M)
# memo, A,  SIGN, SuperFlag = {}, [], [] , False
# print('STEP 1  '),fill_available_position(M)
# print('STEP 2  '),fill_available_position(M)
# print('STEP 3  '),fill_available_position(M)
# print('STEP 4  '),fill_available_position(M)
# print('STEP 5  '),fill_available_position(M)
# print('STEP 6  '),fill_available_position(M)
# print('Intermediary:  ',M)
# print('STEP 7  '),fill_available_position(M)
# # # print(M)
# print('STEP 8  '),fill_available_position(M)
# print('STEP 9  '),fill_available_position(M)
# print('CHECK Doubles Test : ',check_doubles(M))
# print('STEP 10  '),fill_available_position(M)
# print('STEP 11  '),fill_available_position(M)
# print('STEP 12  '),fill_available_position(M)
# print('STEP 13  '),fill_available_position(M)
# print('CHECK Doubles Test : ',check_doubles(M), memo)
# print('Intermediary:  ',M)
# print('STEP 14  '),fill_available_position(M)
# print('STEP 15  '),fill_available_position(M)
# print('STEP 16  '),fill_available_position(M)
# print('CHECK Doubles Test : ',check_doubles(M), memo)
# print('STEP 17  '),fill_available_position(M)
# print('STEP 18  '),fill_available_position(M)
# # print('Intermediary:  ',M)
# print('STEP 19  '),fill_available_position(M)
# print('CHECK Doubles Test : ',check_doubles(M), memo)
# print('STEP 20  '),fill_available_position(M)
# print('STEP 21  '),fill_available_position(M)
# print('STEP 22  '),fill_available_position(M)
# print('STEP 24  '),fill_available_position(M)
# print('STEP 25  '),fill_available_position(M)
# print('STEP 26  '),fill_available_position(M)

print('\n-----------------------------------------------')





# print('\n-------------1 FALSE STATUS-----------------------')
#  count_1_false()
#  print('\n-------------2 FALSE STATUS-----------------------')
#  #count_2_false()


print('\n----------------------------------------')


# O = [3, 4, 5, 8, 7, 1, 2, 6, 9], [2, 7, 9, 6, 5, 3, 1, 8, 4], [8, 6, 1, 4, 2, 9, 5, 3, 7], [1, 9, 7, 3, 4, 6, 8, 5, 2], [4, 5, 2, 7, 1, 8, 3, 9, 6], [6, 8, 3, 5, 9, 2, 7, 4, 1], [7, 3, 8, 2, 6, 4, 9, 1, 5], [5, 1, 6, 9, 3, 7, 4, 2, 8], [9, 2, 4, 1, 8, 5, 6, 7, 3]
#
# print('Validate Final :  ',validate_final(O))
# print(get_status(O))
# print('Determine Completion ( no more zeros 0 ): ', no_more_zeros(O)  )
# K = [[3, 0, 0, 0, 0, 0, 0, 0, 9], [0, 7, 9, 0, 5, 3, 1, 8, 4], [8, 0, 0, 0, 0, 0, 0, 0, 7], \
#     [1, 9, 7, 3, 4, 6, 8, 5, 2], [4, 5, 2, 7, 1, 8, 3, 9, 6], [6, 8, 3, 5, 9, 2, 7, 4, 1], \
#     [7, 3, 8, 2, 2, 4, 6, 1, 5], [5, 1, 6, 9, 3, 7, 4, 2, 8], [2, 4, 4, 0, 0, 0, 9, 7, 3]]

# print('No Doubles :  ',intersection(4, 9, 2, K))
# print('Column  test : ', transpose(K)[2-1] )
# print('Row test : ', 4 in (K)[9-1] )
# print('SubMatrix Test :', [row for row in SubMatrix_3x3(9,2,K)] )
# print('SubMatrix Test :', [4 in row for row in SubMatrix_3x3(9,2,K)] )
# print('Flatten the SumMatrix : ',   [val for sublist in SubMatrix_3x3(9,2,K) for val in sublist] )
# print('Intersection  :', True  if  True in [ 4 in row for row in SubMatrix_3x3(3, 8,K) ]  else False  )
# print('Intersection 2 :',  True in [ 5 in row for row in SubMatrix_3x3(3, 8,K) ]   )
# print('Intersection 3 :',   [ row for row in SubMatrix_3x3(3,8 , K) ]   )
# print('CHECK Doubles Function Test : ',check_doubles(M))
# X = [val for sublist in M for val in sublist]


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# print('\n--------------------Hash of a Matrix ----------------')
#
#
# signature = hashlib.md5(b'My Hello World !')
# print('The Test of Hellow World :  ',  signature.hexdigest() )
#
# X = M.copy() ;  Y = str(X)
# print(' The initial  X Matrix Hash Signature :',  hashlib.md5( Y.encode() ).hexdigest())
# X[8][8]= 0 ;  Y = str(X)
# print(X)
# print(' The MODIFIED  X Matrix Hash:',  hashlib.md5(Y.encode()).hexdigest() )


# s = status().values()
# print( 'Validate Completion Correct : ', [i for i in s].count(9) == 9 )
# print("\n What's your story Sudoku ? Are you complete  ?   " ,no_more_zeros(M))
# print('Tel me if there are non-filled positions : ', False in [ i for i in [ val for sublist in get_to_fill_status(M).values() for val in sublist ]  ]  )
# print('Get 2 Unfilled Statuses  non-filled positions : ', [ i for i in get_to_fill_status(M).values()   ]  )
# print('Get Unfilled Statuses  non-filled positions : ',  [ h.count(False) for h in  [i for i in get_to_fill_status(M).values()]   ]  )
# print('Get 0 Unfilled Statuses  non-filled positions : ', 0 in [ h.count(False) for h in  [i for i in get_to_fill_status(M).values()]   ]  )
# print('Get 0  non-filled positions : ', [ h.count(0) for h in  [i for i in M]   ]  )
# print('Get TOTAL number filled of non-filled positions (with 0): ', sum([ h.count(0) for h in  [i for i in M] ])  )
# print('Determine Completion (no more zeros 0 ): ', no_more_zeros(M)  )

