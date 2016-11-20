def guess_seq_len_orig(seq):
    ''' Original Sequence Guess'''
    guess = 1
    max_len = len(seq) // 2
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2*x] :
#             if seq[0:x][0] == seq[0:x][-1] :
#                 return seq[0:x][0]
#             else : return seq[x:2*x]
            return seq[x:2*x]
    return seq[0]







print('---------TEST CASES ------------')


list_a = [111, 0, 3, 1, 111, 0, 3, 1, 111, 0, 3, 1 ]
list_b = [7, 14, 7, 14, 7, 14, 7, 14, 7, 14, 7, 14, 7, 11, 4, 2, 1, 6, 4, 1, 3, 4, 7, 1, 1, 5, 1, 1, 1, 1, 21, 62, 2, 1, 2, 1, 1, 1, 8] # 51
list_c = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,23,18,10]
list_d = [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 17, 1, 24, 1, 7, 7, 1, 1, 4, 3, 1, 1, 1, 1, 2, 15, 2, 5, 1]
list_e = [1, 7, 1, 16, 1, 7, 1, 16, 1, 7, 1, 16, 1, 7, 1, 16, 1, 7, 1, 16, 1, 7, 1, 16, 1, 2, 1, 22, 28]
list_f =[1, 2, 3, 1, 1, 5, 1, 8, 1, 5, 1, 1, 3, 2, 1, 18, 1, 2, 3, 1, 1, 5, 1, 8, 1, 5, 1,1, 3, 2, 1, 18, 1, 2, 2, 5, 2, 9, 2] # 94
list_g=[1, 1, 1, 4, 6, 4, 1, 1, 1, 18, 1, 1, 1, 4, 6, 4, 1, 1, 1, 18, 1, 1, 1, 4, 6, 4, 1, 1, 1] # 93
list_h = [2, 2, 2, 14, 2, 2, 2, 14, 2, 2, 2, 14, 2, 2, 2, 14, 2, 2, 2, 14, 2, 2, 2, 14, 1, 1, 1, 1, 3, 2, 4, 1, 6, 1, 1, 16, 3, 1, 8]
list_i= [3, 1, 1, 3, 14, 3, 1, 1, 3, 14, 3, 1, 1, 3, 14, 3, 1, 1, 3, 14, 3, 1, 1, 3, 14, 3, 1, 4, 1, 1, 1, 4, 2, 2, 16, 2, 1, 1, 1]  # 53
list_j = [1, 1, 1, 1, 6, 1, 1, 1, 1, 6, 1, 1, 1, 1, 6, 1, 1, 1, 1, 6, 1, 1, 1, 1, 6, 1, 1, 1, 1, 6, 1, 1]  #13
list_k = [1, 1, 1, 1, 1, 1, 14, 1, 1, 1, 1, 1, 1, 14, 1, 1, 1, 1, 1, 1, 14, 1, 1, 1, 1, 1, 1, 14, 1, 1, 1, 1]
list_l=[1, 4, 3, 1, 2, 2, 1, 3, 4, 1, 14, 1, 4, 3, 1, 2, 2, 1, 3, 4, 1, 14, 1, 4, 3, 1, 2, 2, 1, 3, 4, 1, 15, 5, 2, 1, 2, 6, 3]
list_m=[2, 3, 3, 2, 18, 2, 3, 3, 2, 18, 2, 3, 3, 2, 18, 2, 3, 3, 2, 18, 2, 3, 3, 4, 1, 1, 13, 1, 25, 3, 8, 6, 1, 11, 1, 1, 1, 14, 2]
list_n = [2, 3, 1, 2, 4, 1, 6, 6, 1, 4, 2, 1, 3, 2, 20, 2, 3, 1, 2, 4, 1, 6, 6, 1, 4, 2, 1, 3, 2, 1, 5, 1, 6, 1, 2, 1, 2, 1, 4] # 109
list_o = [9, 2, 1, 2, 2, 5, 4, 1, 1, 13, 1, 1, 4, 5, 2, 2, 1, 2, 9, 28, 9, 2, 1, 2, 2, 4, 2, 2, 1, 1, 8, 1364, 1, 2, 1, 1, 1, 3, 3] # 199
list_p = [1, 4, 1, 1, 3, 2, 2, 13, 2, 2, 3, 1, 1, 4, 1, 26, 1, 4, 1, 1, 3, 2, 2, 13, 2, 2, 3, 1, 1, 5, 2, 1, 339, 1, 1, 1, 4, 1, 8] # 191
list_q = [2, 4, 1, 8, 6, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 6, 8, 1, 4, 2, 26, 2, 4, 1, 8, 6, 1, 1, 1, 1, 3, 1, 51, 1, 7, 1, 1, 1, 42] #181


L = [ list_a, list_b, list_c, list_d, list_e, list_f, list_g, list_h, list_i, list_j, list_k, list_l, list_m, list_n , list_o, list_p, list_q ]


def inside_loop(seq):
    guess = len(seq)//2
    for guess in range(guess, 1, -1 ):
        guess-=1
        s1, s2 = seq[0:guess], seq[guess: 2*guess ]
        # print(s1)
        # print(s2)
        if s1 == s2 : break
    return s1


def seq_from_list_in_another(L1, L2) :
        s1 = ''.join( str(i) for i in  L1 )
        s2 = ''.join( str(i) for i in  L2 )
        if s1 in s2 :
            return L1

# print(seq_from_list_in_another( [111, 0, 3, 1] , list_a ))


def guess_seq_len(seq):         # MY FUNCTION
    '''    :SCOPE: Functions which returns a repeating sequence within a list of integers.
        If  it not finds a sequence it will return just the first element of the sequence
        Observation : It may not work properly if the sub sequence ends with double, triple ... of the same digit.
        In this case it needs adjustments. However, in the case of lists of partial fractions where the function was used,
        this never happens.
    :param:
        :seq:     List of integers
        :return:     The unique  sequence of numbers from the list        '''
    def inside_loop(seq):
        guess = len(seq)//2
        for guess in range(guess, 1, -1 ):
            guess-=1
            s1, s2 = seq[0:guess], seq[guess: 2*guess ]
            # print(len(s1), s1, end='     ')
            # print(len(s2) , s2)
            if s1 == s2 : break
        if s1 != s2 :  return seq
        else: return s1

    s = inside_loop(seq)
    if len(list(set(s))) == 1 :
        return [s[0]]
    else:                   #return  s
        l1 = len (list(set(s)))
        lst=[]
        for i in range(len(s)):
            lst.append(s[i])
            if l1 == len(list(set(lst))) :
                break
        return lst


for i in L :     print( len(guess_seq_len(i)) ,guess_seq_len(i) ,'                        ',i)

print('\n-------------------------')
# print(guess_seq_len(list_q))



# print('\n---------------------------')
# s = guess_seq_len(list_h)
# l1 = len (list(set(s)))
# lst=[]
# for i in range(len(s)):
#     lst.append(s[i])
#     if l1 == len(list(set(lst))) :
#         break
# print(lst)

