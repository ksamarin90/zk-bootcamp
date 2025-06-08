from py_ecc.bn128 import G1, G2, pairing, FQ12, add, eq, neg, final_exponentiate

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data import A, B, C, witness, srs_g1, srs_g2, alpha_g1, beta_g2, eta_g1, psi
from utils import calculate_psi, create_t_poly, GF, matrix_to_polynomial, random_gf, create_srs, evaluate_polynomial, create_eta

# create polynomials
a_poly_gf = matrix_to_polynomial(A, witness)
b_poly_gf = matrix_to_polynomial(B, witness)
c_poly_gf = matrix_to_polynomial(C, witness)

t_poly_gf = create_t_poly(A.shape[0])
h_poly_gf = (a_poly_gf * b_poly_gf - c_poly_gf) // t_poly_gf

A_G = add(evaluate_polynomial(a_poly_gf, srs_g1), alpha_g1)
B_G = add(evaluate_polynomial(b_poly_gf, srs_g2), beta_g2)

C_prime_G = evaluate_polynomial(c_poly_gf, srs_g1)
HT_G = evaluate_polynomial(h_poly_gf, eta_g1)
psi_sum = calculate_psi(witness, psi)

C_G = add(psi_sum, add(C_prime_G, HT_G))

assert eq(FQ12.one(), final_exponentiate(pairing(B_G, neg(A_G)) * pairing(beta_g2, alpha_g1) * pairing(G2, C_G)))
