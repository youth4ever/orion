def compute_quare_root(n, decimals=4) :
    ''' Algorithm to compute custom number of digits of square roots using powers.
    The dot is omitted. If you want the exact result just divide return by / 10**(decimals*2).

    :param:    :n: root to be calculated
                    :decimals: the number of decimal desired    '''

    n = n*10**(decimals*2)
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

root_2 = compute_quare_root(2, 99)
print(root_2, 'Sum of the digits : ',sum([int(i) for i in str(root_2)]) )