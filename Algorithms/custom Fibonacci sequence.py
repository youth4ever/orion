
#### Here by modifying the starting values we can build Custom fibonacci sequences :
def custom_Fibo_gen(a1, a2):
    #   Fibonacci GENERATOR , while loop
    while True:
        a = a1 + a2
        yield a
        a1, a2 = a2, a

FG1 = custom_Fibo_gen(1, 0)
print('FG1 : \t', [next(FG1) for i in range(20)])

FG2 = custom_Fibo_gen( -2, 3)
print('FG2 : \t', [next(FG2) for i in range(20)])

FG3 = custom_Fibo_gen( -1, 3)
print('FG3 : \t', [next(FG3) for i in range(20)])

### OBSERVATION :       FG1 + FG2 = FG3 ,
# example :  (3-rd term in FG1 = 2) + (3-rd term in FG2 = 5 ) = ( 3-rd term in FG3 = 7 )


