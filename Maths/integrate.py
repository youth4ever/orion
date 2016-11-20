from scipy.integrate import quad


def integrand(x, a, b):
    return 1

a = 0
b =1
I=quad(integrand, 0, 1, args=(a,b))
print(I)



##############################################

def integrand(x, a, b):
     return a * x + b

a =2
b =1
I=quad(integrand, 0, 1, args=(a,b))
print(I)

def integrand(t, n, x):
    return exp(-x*t) / t**n