def Blum_Blum_Shub_gen():           # EFFICIENT GENERATOR
    '''     s_0 = 290797
            s_(n+1) = s_n×s_n (modulo 50515093)
            t_n = s_n (modulo 500)                  '''
    s = 290797
    while True :
        s = pow(s, 2 , 50515093 )
        t = s % 500
        yield t

B = Blum_Blum_Shub_gen()
for i in range(12):    print( next(B),end=' ;  ')
print(next(B), next(B), next(B), next(B) )


print('\n---------------- Same Generator in a simpler way ---------------------')

SMOD = 50515093
TMOD = 500
def blum(pmod=TMOD):
    s = 290797
    while True:
        s = pow(s, 2, SMOD)
        yield s % pmod
B2 = blum()

for i in range(16) : print(next(B2), end=' ;  ')


def bbs_prng(s=290797, m_s=50515093, m_t=500):
    while 1:
        s = (s * s) % m_s
        yield s % m_t

