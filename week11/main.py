from py_ecc.bn128 import G1, G2, pairing, FQ12, add

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data import A, B, C, witness, srs_g1, srs_g2, eta_g1, t_poly_gf
from utils import create_t_poly, GF, matrix_to_polynomial, evaluate_polynomial

a_poly_gf = matrix_to_polynomial(A, witness)
b_poly_gf = matrix_to_polynomial(B, witness)
c_poly_gf = matrix_to_polynomial(C, witness)

h_poly_gf = (a_poly_gf * b_poly_gf - c_poly_gf) // t_poly_gf

assert (a_poly_gf * b_poly_gf == c_poly_gf + h_poly_gf * t_poly_gf), "Non equal polynoms"

A_G = evaluate_polynomial(a_poly_gf, srs_g1)
B_G = evaluate_polynomial(b_poly_gf, srs_g2)

C_prime_G = evaluate_polynomial(c_poly_gf, srs_g1)
HT_G = evaluate_polynomial(h_poly_gf, eta_g1)

C_G = add(C_prime_G, HT_G)

result = pairing(B_G, A_G) - pairing(G2, C_G)

# it should be zero
assert(result == FQ12.zero())