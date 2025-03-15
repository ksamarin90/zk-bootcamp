import galois
import numpy as np

p = 71

def mod(number):
    return number % p

def inv(number):
     return pow(number, -1, p)

# Problem 1
print('')
print('Problem 1')
print('')

# Find the elements in a finite field that are congruent to the following values:
input = [-1, -4, -160, 500]

for x in input:
     print(f'For {x}, congruent is {mod(x)}')

# Problem 2
print('')
print('Problem 2')
print('')

# Find the elements that are congruent to a = 5/6, b = 11/12, and c = 21/12
# Verify your answer by checking that a + b = c (in the finite field)
a = mod(5 * inv(6))
b = mod(11 * inv(12))
c = mod(21 * inv(12))
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
print(f'a + b = {mod(a + b)}')
assert(mod(a + b) == c)

# Problem 3
print('')
print('Problem 3')
print('')

# Find the elements that are congruent to a = 2/3, b = 1/2, and c = 1/3.
# Verify your answer by checking that a * b = c (in the finite field)
a = mod(2 * inv(3))
b = inv(2)
c = inv(3)
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
print(f'a * b = {mod(a * b)}')
assert(mod(a * b) == c)

# Problem 4
print('')
print('Problem 4')
print('')

a = 1
b = 1
c = 1
d = 4
A = [[a, b], [c, d]]
print(f'A: {A}')
det = mod(mod(a * d) - mod(b * c))
print(f'Determinant: {det}')
A_inverse = [[mod(inv(det) * d), mod(inv(det) * -b)], [mod(inv(det) * -c), mod(inv(det) * a)]]
print(f'A_inverse: {A_inverse}')

identity = [[mod(A[0][0] * A_inverse[0][0] + A[0][1] * A_inverse[1][0]),
             mod(A[0][0] * A_inverse[0][1] + A[0][1] * A_inverse[1][1])],
            [mod(A[1][0] * A_inverse[0][0] + A[1][1] * A_inverse[1][0]),
             mod(A[1][0] * A_inverse[0][1] + A[1][1] * A_inverse[1][1])]]
print(f'Identity: {identity}')


## Problem 5
print('')
print('Problem 5')
print('')

# What is the modular square root of 12?
# Verify your answer by checking that x * x = 12 (mod 71)
# Use brute force to find the answer (in Python)
for x in range(p - 1):
    if mod(x * x) == 12:
        print(f'x * x = 12, for x = {x}')
        # (15 + x) mod 71 = 0
        # x = 56 => 71 % 71 = 0
        # p - a = a_inverse
        break


## Problem 6
print('')
print('Problem 6')
print('')

# Suppose we have the following polynomials:

# p(x)=52x^2+24x+61
# q(x)=40x^2+40x+58

# What is p(x) + q(x)? What is p(x) * q(x)?
# Use the `galois` library in Python to find the roots of p(x) and q(x).
# What are the roots of p(x)q(x)?

GF = galois.GF(p)

p = galois.Poly([52, 24, 61], field=GF)
q = galois.Poly([40, 40, 58], field=GF)

print("p(x):", p)
print("q(x):", q)

print("p(x) + q(x):", p + q)
print("p(x) * q(x):", p * q)

print("p(x) roots:", p.roots())
print("q(x) roots:", q.roots())
print("p(x) * q(x) roots:", (p * q).roots())


## Problem 7
print('')
print('Problem 7')
print('')

# Find a polynomial f(x) that crosses the points (10, 15), (23, 29).
# Since these are two points, the polynomial will be of degree 1 and be the equation for a line (y = ax + b).
# Verify your answer by checking that f(10) = 15 and f(23) = 29.

# Define the system of equations: 15 = 10a + b, 29 = 23a + b in GF(71)
# {
#    15 = 10a + b
#     29 = 23a + b 
# }
A = GF([[10, 1], [23, 1]])
B = GF([15, 29])
(a, b) = np.linalg.solve(A, B)
print(f"a: {a}, b: {b}")

f = galois.Poly([a, b], GF)

# # (p - 1)(p - 1) = p^2 - 2p + 1
# mod 5 => 4 * 4
# mod 7 => 6 * 6
# mod 11 => 10 * 10
# # 4 + 4 + 4 + 4
# # 3 + 3

print(f"f(10): {f(10)}")
print(f"f(23): {f(23)}")


## Problem 8

print('')
print('Problem 8')
print('')

# What is Lagrange interpolation and what does it do?
# Find a polynomial that crosses through the points (0, 1), (1, 2), (2, 1).
# Use this Stackoverflow answer as a starting point: https://stackoverflow.com/a/73434775

polynomial = galois.lagrange_poly(GF([0, 1, 2]), GF([1, 2, 1]))

print(polynomial)
print(polynomial(0))
print(polynomial(1))
print(polynomial(2))
