print('====================COINS WAYS PROBLEM ===================')

print('---------------------- ITERATION -----------------------')

total = 5
combinations = [1] + [0]*total
monies = [1,2,5,10,20,50,100,200]

for x in monies:
    for i in range(x, total+1):
        combinations[i] += combinations[i-x]
        #print(combinations)

print (combinations[total])

##########################################
print('\n---------------------- ITERATION -----------------------')


def coinsum(value):

    coins = [1,2,5,10,20,50,100,200]

    ways = [0] * (value+1)
    ways[0] = 1

    while coins[-1] > value:
        del(coins[-1])

    for i in range(len(coins)):
        for j in range (coins[i],value + 1):
            ways[j] += ways[j - coins[i]]

    print (ways[-1])

coinsum(10)

##########################################

print('\n---------------------- RECURSION with Memoization -----------------------')

coin = [1,2,5,10,20,50,100,200]

def pb031(n,arr):
    last = arr[-1]
    if len(arr) == 1:
        return 1
    return sum(pb031(n-last*i,arr[:-1]) for i in range(n//last+1))

print(pb031(200,coin))

###################################

print('\n================= NUMBER PARTITIONING =============================')

val = 100
partitions = [1] +  [0]* val
cons = [i for i in range(1,val+1)]
#print([i for i in range(1,val+1)])

for i in cons:
    for j in range (i, val+1):
        #print(i, j , partitions)
        partitions[j] +=  partitions[j - i]

print('\n',partitions)
print(partitions[-1])

# for i in range(3500, len(partitions)):
#     print(str(i)+'.   ', partitions[i])



def number_partition(n):
    ''':Description:     Function which returns the partition number decomposition value for a number.
        :NOTE:  It can be used to many partitions not only for consecutive numbers
        :Examples:       :1:  consecutives = [i for i in range(1,n+1)] --> for consecutive numbers
                            :2:  coins = [1,2,5,10,20,50,100,200....] --> for coins possible partitions
                            :3:  primes = [2,3,5,7,11...] --> for possible partitions of primes
        :param n: is an integer, the number to get partitions for
        :return: a number, integer
    '''
    partitions = [1] +  [0]* n
    cons = [i for i in range(1,n+1)]

    for i in cons:
        for j in range (i, n+1):
            #print(i, j , partitions)
            partitions[j] +=  partitions[j - i]
    return partitions[-1]

print('\nOur desired Result  : ',number_partition(71))

print('\n------------------NUMBER PARTITION ALGORITHM DETAILED DECOMPOSITION ------------------')
print('This is a generator which generates the list with the possible decompositions \n')

def partitions(n):
    '''     Taken from http://code.activestate.com/recipes/218332-generator-for-integer-partitions/
            Created by David Eppstein on Wed, 27 Aug 2003
    :What it is:    A generator of number partition
    :Usage:     Example:    for i in partitions(5):    print(i)
    :param n:   the number you want the partitions
    :return:    set of lists with all the possible combinations                                                 '''
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return

    # modify partitions of n-1 to form partitions of n
    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]


for i in partitions(5):    print(i)



#############################

def aP(n):
    """Generate partitions of n as ordered lists in ascending
    lexicographical order.

    This highly efficient routine is based on the delightful
    work of Kelleher and O'Sullivan.

    Examples
    ========

    #>>> for i in aP(6): i

    [1, 1, 1, 1, 1, 1]
    [1, 1, 1, 1, 2]
    [1, 1, 1, 3]
    [1, 1, 2, 2]
    [1, 1, 4]
    [1, 2, 3]
    [1, 5]
    [2, 2, 2]
    [2, 4]
    [3, 3]
    [6]

    #>>> for i in aP(0): i


    References
    ==========

    .. [1] Generating Integer Partitions, [online],
        Available: http://jeromekelleher.net/generating-integer-partitions.html
    .. [2] Jerome Kelleher and Barry O'Sullivan, "Generating All
        Partitions: A Comparison Of Two Encodings", [online],
        Available: http://arxiv.org/pdf/0909.2331v2.pdf

    """
    # The list `a`'s leading elements contain the partition in which
    # y is the biggest element and x is either the same as y or the
    # 2nd largest element; v and w are adjacent element indices
    # to which x and y are being assigned, respectively.
    a = [1]*n
    y = -1
    v = n
    while v > 0:
        v -= 1
        x = a[v] + 1
        while y >= 2 * x:
            a[v] = x
            y -= x
            v += 1
        w = v + 1
        while x <= y:
            a[v] = x
            a[w] = y
            yield a[:w + 1]
            x += 1
            y -= 1
        a[v] = x + y
        y = a[v] - 1
        yield a[:w]

for i in aP(5): print(i)