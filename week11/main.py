from py_ecc.bn128 import G1, G2, pairing, FQ12

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data import A, B, C, witness
from utils import create_t_poly, GF, matrix_to_polynomial, random_gf, create_srs, evaluate_polynomial

a_poly_gf = matrix_to_polynomial(A, witness)
b_poly_gf = matrix_to_polynomial(B, witness)
c_poly_gf = matrix_to_polynomial(C, witness)

t_poly_gf = create_t_poly(A.shape[0])

h_poly_gf = (a_poly_gf * b_poly_gf - c_poly_gf) // t_poly_gf

tau = random_gf()

assert (a_poly_gf * b_poly_gf == c_poly_gf + h_poly_gf * t_poly_gf), "Non equal polynoms"
assert (a_poly_gf(tau) * b_poly_gf(tau) == c_poly_gf(tau) + h_poly_gf(tau) * t_poly_gf(tau)), "Non equal polynoms"

# degree of polynomial equation
degree = a_poly_gf.degree + b_poly_gf.degree

#  pregenerate G points for pairing
points_G1 = create_srs(G1, int(tau), degree)
points_G2 = create_srs(G2, int(tau), degree)

A_G = evaluate_polynomial(a_poly_gf, points_G1)
B_G = evaluate_polynomial(b_poly_gf, points_G2)
C_G = evaluate_polynomial(c_poly_gf + h_poly_gf * t_poly_gf, points_G1)


result = pairing(B_G, A_G) - pairing(G2, C_G)

# it should be zero
assert(result == FQ12.zero())