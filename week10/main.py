# Problem 1

from scipy.interpolate import lagrange
import numpy as np
import random

# Define the matrices
A = np.array([[0,0,3,0,0,0],
               [0,0,0,0,1,0],
               [0,0,1,0,0,0]])

B = np.array([[0,0,1,0,0,0],
               [0,0,0,1,0,0],
               [0,0,0,5,0,0]])

C = np.array([[0,0,0,0,1,0],
               [0,0,0,0,0,1],
               [-3,1,1,2,0,-1]])

# pick values for x and y
x = 1000
y = 1000

# this is our orignal formula
out = 3 * x * x * y + 5 * x * y - x- 2*y + 3# the witness vector with the intermediate variables inside
v1 = 3*x*x
v2 = v1 * y
w = np.array([1, out, x, y, v1, v2])

result = C.dot(w) == np.multiply(A.dot(w),B.dot(w))
assert result.all(), "result contains an inequality"

# helper to convert vector of three constraints
def L(vec):
    return lagrange([1, 2, 3], vec)

# helper to convert matrix of three constraints using "w" witness
def matrix_to_poly(matrix):
    columns = [matrix[:, i] for i in range(matrix.shape[1])]
    result_poly = 0
    for i in range(len(columns)):
        poly = L(columns[i]) * w[i]
        result_poly += poly
    return result_poly

a_poly = matrix_to_poly(A)
b_poly = matrix_to_poly(B)
c_poly = matrix_to_poly(C)

# create tau (x - 1)(x - 2)(x - 3) since we have three constraints
t_poly = np.poly1d([1, -1]) * np.poly1d([1, -2]) * np.poly1d([1, -3])

# and now using symbolic math derive balancing factor h
h_poly, remainder = np.polydiv(a_poly * b_poly - c_poly, t_poly)

# now check that our QAP holds
assert (a_poly * b_poly) == (c_poly + h_poly * t_poly), "non equal polynomials"


num = random.randint(5, 1000)
# random number might not be evaluated correctly because we are using floating point math
assert (a_poly(num) * b_poly(num)) == (c_poly(num) + h_poly(num) * t_poly(num))