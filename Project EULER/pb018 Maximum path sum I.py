#!/usr/bin/python
# Solved by Bogdan Trif @  Corrected @ 2016-09-25, 11:53
#The  Euler Project  https://projecteuler.net
'''
Maximum path sum I      -       Problem 18
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
'''

print('------------------ MY SOLUTION, after studying the algorithm with dynamic programming ----------------------')

f = open('pb018.txt', 'r')
text = f.read()
f.close()
# Initialize and populate triangle
triangle = []
print(text,'        ',type(text),'\n')

for row in text.split('\n'):
    triangle.append(list(map(int, row.split(' '))))         # This maps the strings into ints on the run, SMART TECHNIQUE
    #print(row, type(row))
#print(len(triangle), triangle)


for i in range(len(triangle)-2, -1,-1):
    for j in range(0,i+1):
        triangle[i][j] +=  max(triangle[i+1][j], triangle[i+1][j+1])
        #print(triangle[i][j])
        #print(max(triangle[i+1][j], triangle[i+1][j+1]))
    print(triangle[i], end=' \n ')

print('\n And the largest path is :   ',triangle[0][0])


print('----------'*15)

########################################################



print('\n=================     OTHER  SOLUTIONS FROM EULER FORUM      =======================')
print('\n---------- FIRST SOLUTION - DYNAMICS PROGRAMING, by dugar_ab-----------------')
# dynamic programming. From bottom to top
#Won't lie, had a little help from the internet

a=[[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

for i in range(len(a)-2,-1,-1):
        for j in range(0,i+1):
                a[i][j] += max(a[i+1][j] , a[i+1][j+1])

print ('\nThe SOLUTION  :',a[0][0])


print (triangle[0][0])

print('\n---------------------- SECOND SOLUTION ----------------------')

triangle = [
    ['75'],
    ['95', '64'],
    ['17', '47', '82'],
    ['18', '35', '87', '10'],
    ['20', '04', '82', '47', '65'],
    ['19', '01', '23', '75', '03', '34'],
    ['88', '02', '77', '73', '07', '63', '67'],
    ['99', '65', '04', '28', '06', '16', '70', '92'],
    ['41', '41', '26', '56', '83', '40', '80', '70', '33'],
    ['41', '48', '72', '33', '47', '32', '37', '16', '94', '29'],
    ['53', '71', '44', '65', '25', '43', '91', '52', '97', '51', '14'],
    ['70', '11', '33', '28', '77', '73', '17', '78', '39', '68', '17', '57'],
    ['91', '71', '52', '38', '17', '14', '91', '43', '58', '50', '27', '29', '48'],
    ['63', '66', '04', '68', '89', '53', '67', '30', '73', '16', '69', '87', '40', '31'],
    ['04', '62', '98', '27', '23', '09', '70', '98', '73', '93', '38', '53', '60', '04', '23']]

def eval_hops(last_row, cur_row):
    new_row = []
    for i in range(len(cur_row)):
        options = [int(last_row[i]), int(last_row[i + 1])]
        new_row.append(str(max(options) + int(cur_row[i])))
    return new_row


def find_path(triangle):
    while len(triangle) > 1:
        last_row = triangle.pop(-1)
        cur_row = triangle.pop(-1)
        triangle.append(eval_hops(last_row, cur_row))
    return triangle[0][0]

print('highest cost path = {}'.format(find_path(triangle)))

print('\n---------------------- THIRD SOLUTION ----------------------')
# Starts from the bottom
file = open('pb018.txt')
array = []

for i in range(15):    # Builds the array
    array.append([])
    line = file.readline()
    for j in range(0,len(line),3):
        array[i].append(int(line[j:j+2]))

#print(array)

for i in range(13,-1,-1):    # Calculates max sums
    print('---'*10)
    for j in range(len(array[i])):
        array[i][j] = max(array[i][j] + array[i+1][j], array[i][j] + array[i+1][j+1])
        #print(array[i][j], array[i+1][j] , array[i][j] + array[i+1][j], ' , ',array[i][j], array[i+1][j+1], array[i][j] + array[i+1][j+1],  ' , Max =',array[i][j] ,  end = '  >>  ')

    print(array[i])
file.close()


print('\n----------------------  FOURTH SOLUTION - DYNAMIC PROGRAMMING, by elmiguel   USA ----------------------')
matrix = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

t = matrix[-1]
for i in range(len(matrix) - 2, -1, -1):
    t = [max(matrix[i][j] + t[j], matrix[i][j] + t[j+1]) for j in range(len(matrix[i]))]

print(t[0])

print('\n---------------------- FIFTH SOLUTION - DYNAMICS PROGRAMING , by ehaavindberman   ----------------------')
'''
#The trick is that we work from the bottom up to the top and we don't need
 #to keep track of the path because we only want the max sum, not the path.
#Essentially we are choosing a path from the bottom up, at the 14th row first number we have 63
#and it has two paths 4 or 62. We would always choose 62 so we replace 63 with 63+62 = 125.
#We do this for each entry in line 14 then move to line 13 and do the same until we get to the first line which will be the max path.
'''

a = [[75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

for i in reversed(range(len(a)-1)):
    #print('\nFirst elem  :   ' , a[i][j])
    for j in reversed(range(len(a[i]))):
        a[i][j] += max(a[i+1][j],a[i+1][j+1])
print(a[0][0])


print('\n---------------------- SIXTH SOLUTION - BACKWARDS INDUCTION, by nprichardson, England ----------------------')

# Backwards Induction (also does problem 67):

filePath = r'pb018.txt'
data = [(line.rstrip('\n')).split(' ') for line in open(filePath)]

for i,line in enumerate(data):
    data[i] = [int(num) for num in line]

numRows = len(data)
for rowIndex in range(numRows-2,-1,-1): #start at second to last row
    for node,entry in enumerate(data[rowIndex]):
        data[rowIndex][node] = (entry
                                + max (data[rowIndex+1][node],data[rowIndex+1][node+1]))

print ('max path length='+ str(data[0][0]))

print('\n---------------------- SEVENTH SOLUTION - BRUTE FORCE, by Zalaetus, Spain ----------------------')


piramide = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
piramide = (int(i) for i in piramide.replace("\n", " ").split(" "))
triangulo = bytes(piramide)
altura = 15

def recorredor(x = 0, h = 0):
    if h == altura - 1: return triangulo[x]
    valor = triangulo[x]
    valor += max(recorredor(x + h + 1, h + 1), recorredor(x + h + 2, h + 1))
    return valor

print(recorredor())

print('\n---------------------- EIGHTH SOLUTION - by untrue, Russia ----------------------')

import time
t_ = time.clock()

r = [[75],
     [95, 64],
     [17, 47, 82],
     [18, 35, 87, 10],
     [20, 4, 82, 47, 65],
     [19, 1, 23, 75, 3, 34],
     [88, 2, 77, 73, 7, 63, 67],
     [99, 65, 4, 28, 6, 16, 70, 92],
     [41, 41, 26, 56, 83, 40, 80, 70, 33],
     [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
     [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
     [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
     [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
     [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
     [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

total = [[]]
row = []

for i in range(len(r) - 1, -1, -1):
    if i == len(r) - 1:
        total[0] = r[i]
    else:
        for n in range(0, len(r[i])):
            row.append(r[i][n] + max(total[0][n], total[0][n + 1]))
        total[0] = row[0:99]
        row[0:99] = []

print(total[0][0])
print('Time taken = ', time.clock() - t_,' seconds.')


print('\n---------------------- NINETH SOLUTION , bu Sahexa ----------------------')

triangular = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split("\n")


def data(triangular=triangular):
    new = [i.split(" ") for i in triangular]
    return new[1:len(new) + 1]


# below to top...
def solve():
    numbers = data()
    # for start 2. row from below...
    for i in reversed(range(len(numbers) - 1)):
        for j in range(i + 1):
            a = int(numbers[i][j])
            # numbers[13][0] = 63
            b = int(max(numbers[i + 1][j], numbers[i + 1][j + 1]))
            # numbers[14][0] = 04, numbers[14][1] = 62, (max=62)
            c = a + b
            # 125 = 63 + 62
            numbers[i][j] = str(c)
            # number[13][0] = 125
    return numbers[0][0]
