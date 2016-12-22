
def unique_permutations(lst):       # VERY EFFECTIVE
    ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
        If one tries itertools.permutations on a list with 14 elements ==> BANG, computer freezes
    :Usage: list(unique_permutations([1,1,1,3]))
    :param lst: type list
    :return:    a list of lists containing all the permutations
    '''
    if len(lst) == 1:
        yield (lst[0],)
    else:
        unique_lst = set(lst)
        for first_element in unique_lst:
            remaining_lst = list(lst)
            remaining_lst.remove(first_element)
            for sub_permutation in unique_permutations(remaining_lst):
                yield (first_element,) + sub_permutation

# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]  #	   1-case
# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3]  #	   2-case
# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 3, 5]         #     3-case
# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 5, 3, 4] 	                #     4-case
# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3]             #     5-case
# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3]         #     6-case
# L = [1, 1, 1, 1, 1, 3  4, 5, 6, 6]                                       #     custom case  three == one
# L = [1, 1, 1, 1,  3,  4, 5, 6, 6]                                       #     custom case  threes = ones + 1
# L =  [1, 1, 1, 1, 1, 1, 1, 3, 3]
L = [1, 1, 1, 1, 3, 3, 3]


def get_block_combinations(L):

    threes = [i for i in L if i >= 3]
    ones = L.count(1)
    threes_nr = len(threes)
    up_range=len(L)-2*(threes_nr-1)
    M, mark = [], 0

    def count_unique_perm_rec(ones, threes_nr):
        ''':Description: Recursion Function to count blocks separated by one tile

        :param ones: int , the number of ones from the list
        :param threes_nr: int, numbers of threes(numbers >= 3 in the list)
        :return: int, the number of possible configurations
        '''
        nonlocal  mark, up_range
        tmp = []
        if threes_nr == 1 : return ones+threes_nr

        if threes_nr > 2 :
            count_unique_perm_rec(ones, threes_nr-1)
            mark+=1
            for j in range(1, up_range+1):
                tmp.append( sum( M[mark-1][0:j] ) )
            M.append(tmp)
            print(M)

        elif threes_nr == 2 :
            for i in range(1, up_range+1):
                tmp.append(i)
            M.append(tmp)
            print(M)

        return sum(M[mark])
    return count_unique_perm_rec(ones, threes_nr)


########################




class GET_ROD_VARIATIONS(object):
    ''':Description: depends on the unique_permutations function.
            *Made by Bogdan Trif @ 2016-12-06, 22:00*
    :param lst: the list to analyze
    :return: int, the final number of available configurations
    '''
    def __init__( self, lst ):
        self.lst = lst
        self.threes = [i for i in self.lst if i >= 3]
        self.threes_nr = len(self.threes)
        self.ones = self.lst.count(1)
        self.mark = 0
        self.M = []
        # self.N = list(unique_permutations(self.threes ))
        self.up_range = len(self.lst)-2*(self.threes_nr-1)+1

    def unique_permutations(self):       # VERY EFFECTIVE
        ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
            If one tries itertools.permutations on a list with 14 elements ==> BANG, computer freezes
        :Usage: list(unique_permutations([1,1,1,3]))
        :param lst: type list
        :return:    a list of lists containing all the permutations
        '''
        if len(self.lst) == 1:
            yield (self.lst[0],)
        else:
            unique_lst = set(self.lst)
            for first_element in unique_lst:
                remaining_lst = list(self.lst)
                remaining_lst.remove(first_element)
                for sub_permutation in unique_permutations(remaining_lst):
                    yield (first_element,) + sub_permutation

    def get_multiplier(self) :
        N = list(unique_permutations(self.threes ))
        # print(N)
        return len(N)

    def count_unique_perm(self, ones, threes_nr ) :
        ''':Description: Recursion Function to count blocks separated by one tile.
        :param ones: int , the number of ones from the list
        :param threes_nr: int, numbers of threes(numbers >= 3 in the list)
        :return: int, the number of possible configurations
        '''
        tmp = []

        if self.threes_nr > 2 :
            self.threes_nr = self.threes_nr-1
            self.count_unique_perm(  self.ones , self.threes_nr )
            self.mark+=1
            for j in range(1, self.up_range):
                tmp.append( sum( self.M[self.mark-1][0:j] ) )
                # print(tmp)
            self.M.append(tmp)
            # print(self.M)

        elif self.threes_nr == 2 :
            for i in range(1, self.up_range):
                tmp.append(i)
            self.M.append(tmp)
            # print(self.M)

        return sum(self.M[self.mark])

    def __str__(self):
        return self.lst

    def get_result(self):
        if self.threes_nr == 1 : return len(self.lst)
        if self.threes_nr -1 == self.ones :  return (1* self.get_multiplier() )
        if self.threes_nr  == self.ones :  return ( (self.ones +1 )* self.get_multiplier())
        if self.threes_nr  == 0 :  return 1
        if self.ones  == 0 :  return 1

        else :
            return self.count_unique_perm(self.ones, self.threes_nr) * self.get_multiplier()


L=[1, 1, 1, 1, 3, 3, 3]
# print('\nCLASS __str__ TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).__str__() )
print('\n CLASS get_multiplier TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).get_multiplier() )
print('\n CLASS unique_permutations TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).unique_permutations() )
print('CLASS TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).threes_nr )
print('CLASS TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).ones )
# print('\nCLASS count_unique_perm TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).count_unique_perm(ones, threes) )
print('\nCLASS get_result TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).get_result() )


print('\n FUNCTION count_unique_perm_rec : ',get_block_combinations(L),'\n\n' )

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


RODS = []
def count_block_combinations(rod_length) :
    cnt = 0
    for K in partitions(rod_length):
        if K.count(2) == 0 :
            ones = K.count(1)
            threes_nr = len([ i for i in K if i>=3 ])
            if  threes_nr <= ones +1 :
                RODS.append(K)
                a = GET_ROD_VARIATIONS(K).get_result()
                b = GET_ROD_VARIATIONS(K).get_multiplier()
                c = GET_ROD_VARIATIONS(K).ones
                d = GET_ROD_VARIATIONS(K).threes_nr
                e = GET_ROD_VARIATIONS(K).up_range

                print(a,'\t', K, b, '  ; ones, threes :',c, d,'  ',e)
                cnt += a
    return print('\nAnswer : ', cnt)

count_block_combinations(15)

print('\n\n',RODS)

RODS = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3], [1, 1, 1, 1, 1, 1, 1, 3, 3], [1, 1, 1, 1, 3, 3, 3], \
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 4], [1, 1, 1, 1, 1, 1, 3, 4], [1, 1, 1, 3, 3, 4], [1, 1, 1, 1, 1, 4, 4], [1, 1, 3, 4, 4], [1, 1, 1, 1, 1, 1, 1, 1, 5],\
        [1, 1, 1, 1, 1, 3, 5], [1, 1, 3, 3, 5], [1, 1, 1, 1, 4, 5], [1, 1, 1, 5, 5], [1, 1, 1, 1, 1, 1, 1, 6], [1, 1, 1, 1, 3, 6], [1, 1, 1, 4, 6],\
        [1, 1, 5, 6], [1, 6, 6], [1, 1, 1, 1, 1, 1, 7], [1, 1, 1, 3, 7], [1, 1, 4, 7], [1, 5, 7], [1, 1, 1, 1, 1, 8], [1, 1, 3, 8], [1, 4, 8],\
        [1, 1, 1, 1, 9], [1, 3, 9], [1, 1, 1, 10], [1, 1, 11], [1, 12], [13]]



# for i in RODS:
#     print(i)
#     B = get_block_combinations(i)