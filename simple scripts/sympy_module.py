import sympy

sympy.ntheory.totient(8)
sympy.ntheory.binomial_coefficients_list(15)

print('------------------ Divisors ------------------------')
sympy.ntheory.divisors(12)
sympy.ntheory.divisor_count(12)
sympy.ntheory.divisor_sigma(12)

sympy.ntheory.primefactors(90)



sympy.ntheory.multinomial_coefficients(2,3)
sympy.ntheory.multinomial_coefficients(2,2)

print('----------------------- Primes ------------------------')

sympy.ntheory.primerange(3,18)
sympy.ntheory.primepi(100)
sympy.ntheory.primorial(2)


print('----------------------- Partitions ------------------------')

sympy.ntheory.npartitions(4)

print('----------------------- Continued Fractions ------------------------')

sympy.ntheory.continued_fraction_reduce([1,1,2,4])
sympy.ntheory.continued_fraction_periodic(13,6)


sympy.ntheory.is_nthpow_residue(2,3, 8)
sympy.ntheory.is_primitive_root(12,23)


sympy.expand_mul(exp(x+y)*(x+y)*log(x*y**2))
sympy.expand_power_base((x*y)**z)
sympy.expand_trig(sin(x+y)*(x+y))

from sympy import factor, sqrt
from sympy.abc import x, y
sympy.factor(2*x**5 + 2*x**4*y + 4*x**3 + 4*x**2*y + 2*x + 2*y)


sympy.dict_merge






