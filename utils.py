from operator import mul
import numpy as np
import galois
from py_ecc.bn128 import G1, Z1, G2, multiply, add, pairing, FQ12, curve_order
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
        poly = L_gf(columns[i]) * GF(witness[i])
        result_poly += poly
    return result_poly

def random_gf():
    return GF(random.randint(0, curve_order - 1))

def create_srs(G, tau, constraints):
    return [multiply(G, int(tau) ** i) for i in range(constraints - 1, -1, -1)]

def create_eta(G, tau, constraints, t):
    return [multiply(G, (int(tau) ** i) * int(t(tau))) for i in range(constraints - 2, -1, -1)]

def create_psi(U, V, W, alpha, beta, tau): 
    u_columns = [U[:, i] for i in range(U.shape[1])]
    v_columns = [V[:, i] for i in range(V.shape[1])]
    w_columns = [W[:, i] for i in range(W.shape[1])]
    psi = []
    for i in range(len(u_columns)):
        u_poly = L_gf(u_columns[i])
        v_poly = L_gf(v_columns[i])
        w_poly = L_gf(w_columns[i])
        value = w_poly(tau) + alpha * v_poly(tau) + beta * u_poly(tau)
        psi.append(multiply(G1, int(value)))
    return psi

def calculate_psi(witness, psi):
    result = Z1
    for i in range(len(witness)):
        result = add(result, multiply(psi[i], int(witness[i])))
    return result

# taking from ZK book inner_product to evaluate polynomial at G points
# and modify it to be generic
def evaluate_polynomial(polynomial, points):
    coeffs = []
    for i in range(len(polynomial.coeffs)):
        coeffs.append(int(polynomial.coeffs[i]))
    return reduce(add, map(multiply, points, coeffs))