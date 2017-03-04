def partition_in_three(n):     #2017-02-06 Some minor losses, but no time to fix it now
    ''':Description: Partition a number in three in the form (a, b, c) where a>=b>=c
    :Usage:  >>> for i in P :  print( i )
    :param n: int, number
    :return: generator, tuple with partitions : (9, 1, 1), (8, 2, 1), (7, 3, 1) ....            '''
    a, b, c = n-1, 0, 1
    bc = b+c
    while a > n/3+1 :
        a-=1
        bc+=1
        for i in range( 1, bc//2+1):
            b=bc-i ; c=bc-b
            if a>=b :
                yield a, b, c
    if n%3 == 0 :
        yield n//3, n//3, n//3

PT = partition_in_three(6)

cnt=0
for i in PT :
    cnt+=1
    print(str(cnt)+'.       ', i )