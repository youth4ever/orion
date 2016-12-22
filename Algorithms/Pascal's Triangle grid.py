
grid = []
n = 7
for i in range(n+1):
    grid.append([1] * (n+1))

for i in range(n):
    for j in range(n):
        grid[i+1][j+1] = grid[i][j+1] + grid[i+1][j]
    print(grid)

print(str(grid[n][n]))

'''
                                               1
                                            1     1
                                         1     2     1
                                      1     3     3     1
                                   1     4     6     4     1
                                1     5    10   10    5     1
                            1     6    15    20    15    6    1
                         1     7   21    35    35    21   7     1
'''

print('\n--------------')
def main():
    size = 3
    grid_points_count = size + 1
    grid = []
    for x in range(grid_points_count):
        cur_row = []
        for y in range(grid_points_count):
            if x > 0 and y > 0:
                cur_row.append(cur_row[y - 1] + grid[x - 1][y])
            else:
                cur_row.append(1)
        grid.append(cur_row)
        print(grid)
    print(grid[size][size])

main()

print('\n-------------------- OnE MATRIX ROW - PASCAL TRIANGLE----------------------\n')


def generate_Pascal_Triangle(row_nr) :
    '''**©** Made by Bogdan Trif @ 2016-12-20, 21:20.

        :Description: Generates the Pascal Triangle , Binomial Coefficients
        :param row_nr: int, the row number, int
        :return: nested list, matrix in the form of Pascal's Triangle       '''
    blueprint = [1]*(row_nr+1)
    Pascal= [blueprint]
    for i in range(row_nr) :
        tmp=[]
        for j in range(0, row_nr-i) :
            tmp.append(sum(Pascal[-1][0:j+1]) )
        # print(tmp)
        Pascal.append(tmp)
    return Pascal


print('\n-----------Pascal s Triangle --------------' )

Pasc = generate_Pascal_Triangle(7)
print(Pasc,'\n')
for i in range(len(Pasc)):
    print(Pasc[i])

# print(T)

# for i in Pascal:
#     for j in range(i, rows+1):
#         comb[j] += comb[j-i]
#     print(comb)
#
# print(comb)









#
# rows = 7
# comb = [1] + [0]*rows
# # print(comb)
# Pascal = [1]*rows
# # print(Pascal)
#
# for i in Pascal:
#     for j in range(i, rows+1):
#         comb[j] += comb[j-i]
#     print(comb)
#
# print(comb)

