import time

# Only unique permutations
def unique_permutations(lst):       # VERY EFFECTIVE
    ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
        If one tries itertools.permutations on a list with 14 elements ==> BANG, computer freezes
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


# PERMUTATIONS WITHOUT REPETITION           #! MUST COMPARE THE TWO VERSIONS
# Luka Rahne @ http://stackoverflow.com/questions/6284396/permutations-with-unique-values/6285203#6285203
# (modified)
def permutations_wor(elements): # permutations without repetitions
    def recurse(listunique,p_list,d):
        if d < 0:
            yield tuple(p_list)
        else:
            for i in [j for j in listunique if j[1] > 0]:
                p_list[d] = i[0]
                i[1] -= 1
                for g in recurse(listunique,p_list,d-1):
                    yield g
                i[1] += 1
    listunique = [[i,elements.count(i)] for i in set(elements)]
    l = len(elements)
    return recurse(listunique,[0]*l,l-1)



L = [7, 7, 7, 11, 7, 5, 5, 5, 5, 5, 5, 5 ]

print('\n------------------ 1  ----------------')
t1  = time.time()


print('\n\nTest with unique_permutations Function : ',  list(unique_permutations(L)))
print( 'Length' ,len(list(unique_permutations(L))) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#################### #####################

print('\n--------------- 2 ------------------')
t1  = time.time()


print('\n\nTest with unique_permutations Function : ',  list(permutations_wor(L)))
print( 'Length' ,len(list(permutations_wor(L))) )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#################### #####################