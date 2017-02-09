# Binary counter
for x in range(16):
    print (bin(x)[2:].zfill(4), end='  ')
print()

print('\n------------------- Binary counter Generator --------------------\n')

def binary_counter( digits):
    ''' Binary counter

    :param: digits: int, represents the padding, digits = 4 gives 0001
    :return: a binary number
    :Usage:     B = binary_counter(3), print(next(B)
    '''
    x=0
    while True :
        yield (bin(x)[2:].zfill(digits))
        x+=1

B = binary_counter(3)

for i in range(20):
    print(str(i)+'.', next(B), end='   ')

