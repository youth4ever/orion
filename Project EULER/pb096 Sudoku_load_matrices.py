filename = "pb096_sudoku.txt"

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

    f = open(filename, 'r')
    text = f.read()
    for row in text.split('\n'):
        if row[0] == 'G' :
            matrix = []
            Mall[row] = matrix
        else :
            matrix.append(list(map(int, row)))
    return matrix

Mall = {}
M = load_file_3(filename)
cnt= 0
for k,v in Mall.items() :
    cnt+=1
    print(str(cnt)+'.    ' , k,'    ' ,v)