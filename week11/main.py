import numpy as np
from py_ecc.bn128 import curve_order
import galois
import random

GF = galois.GF(curve_order, primitive_element=5, verify=False)

# function to construct t(x) depending on the amount of columns in the matrix
def make_t_poly_for_matrix(matrix):
    num_constraints = matrix.shape[0]
    roots = list(range(1, num_constraints + 1))
    poly = galois.Poly([1], field=GF)
    for r in roots:
        # (x - r)
        poly *= galois.Poly([1, -GF(r)], field=GF)
    return poly

# taking from week10 helper functions and actual data
def L_gf(vec):
    vec = np.array(vec, dtype=object)
    mask = []
    for i in range(1, len(vec) + 1):
        mask.append(i)
    for i in range(len(vec)):
        if (vec[i] < 0):
            vec[i] = curve_order + vec[i]
    return galois.lagrange_poly(GF(np.array(mask)), GF(vec))

def matrix_to_poly_gf(matrix):
    columns = [matrix[:, i] for i in range(matrix.shape[1])]
    result_poly = GF(0)
    for i in range(len(columns)):
        poly = L_gf(columns[i]) * GF(int(w[i]))
        result_poly += poly
    return result_poly

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
out = 3 * x * x * y + 5 * x * y - x- 2*y + 3 # the witness vector with the intermediate variables inside
v1 = 3*x*x
v2 = v1 * y
w = np.array([1, out, x, y, v1, v2], dtype=object)

a_poly_gf = matrix_to_poly_gf(A)
b_poly_gf = matrix_to_poly_gf(B)
c_poly_gf = matrix_to_poly_gf(C)

t_poly_gf = make_t_poly_for_matrix(A)

h_poly_gf = (a_poly_gf * b_poly_gf - c_poly_gf) // t_poly_gf

tau = GF(random.randint(0, curve_order - 1))

assert (a_poly_gf * b_poly_gf == c_poly_gf + h_poly_gf * t_poly_gf), "Non equal polynoms"
assert (a_poly_gf(tau) * b_poly_gf(tau) == c_poly_gf(tau) + h_poly_gf(tau) * t_poly_gf(tau)), "Non equal polynoms"

# actual solution for the assignment

from py_ecc.bn128 import G1, G2, multiply, add, pairing, FQ12
from functools import reduce

# degree of polynomial equation
degree = (c_poly_gf + h_poly_gf * t_poly_gf).degree

#  pregenerate G points for pairing
points_G1 = [multiply(G1, int(tau) ** i) for i in range(degree, -1, -1)]
points_G2 = [multiply(G2, int(tau) ** i) for i in range(degree, -1, -1)]

# taking from ZK book inner_product to evaluate polynomial at G points
# and modify it to be generic
def inner_product(polynomial, points):
    coeffs = []
    degreeDif = len(points) - len(polynomial.coeffs)
    for i in range(degreeDif):
        coeffs.append(0)
    for i in range(len(polynomial.coeffs)):
        coeffs.append(int(polynomial.coeffs[i]))
    return reduce(add, map(multiply, points, coeffs))

A_G = inner_product(a_poly_gf, points_G1)
B_G = inner_product(b_poly_gf, points_G2)
C_G = inner_product(c_poly_gf + h_poly_gf * t_poly_gf, points_G1)


result = pairing(B_G, A_G) - pairing(G2, C_G)

# it should be zero
assert(result == FQ12.zero())