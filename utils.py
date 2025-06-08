import numpy as np
import galois
from py_ecc.bn128 import G1, G2, multiply, add, pairing, FQ12, curve_order
from functools import reduce
import random

GF = galois.GF(curve_order, primitive_element=5, verify=False)

# function to construct t(x) depending on the number of constraints
def create_t_poly(num_constraints):
    roots = list(range(1, num_constraints + 1))
    poly = galois.Poly([1], field=GF)
    for r in roots:
        # (x - r)
        poly *= galois.Poly([1, -GF(r)], field=GF)
    return poly

def L_gf(vec):
    vec = np.array(vec, dtype=object)
    mask = []
    for i in range(1, len(vec) + 1):
        mask.append(i)
    for i in range(len(vec)):
        if (vec[i] < 0):
            vec[i] = curve_order + vec[i]
    return galois.lagrange_poly(GF(np.array(mask)), GF(vec))

def matrix_to_polynomial(matrix, witness):
    columns = [matrix[:, i] for i in range(matrix.shape[1])]
    result_poly = GF(0)
    for i in range(len(columns)):
        poly = L_gf(columns[i]) * GF(int(witness[i]))
        result_poly += poly
    return result_poly

def random_gf():
    return GF(random.randint(0, curve_order - 1))

def create_srs(G, tau, degree):
    return [multiply(G, int(tau) ** i) for i in range(degree, -1, -1)]


# taking from ZK book inner_product to evaluate polynomial at G points
# and modify it to be generic
def evaluate_polynomial(polynomial, points):
    coeffs = []
    degreeDif = len(points) - len(polynomial.coeffs)
    for i in range(degreeDif):
        coeffs.append(0)
    for i in range(len(polynomial.coeffs)):
        coeffs.append(int(polynomial.coeffs[i]))
    return reduce(add, map(multiply, points, coeffs))