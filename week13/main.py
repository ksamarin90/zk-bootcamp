from py_ecc.bn128 import G1, G2, pairing, FQ12, add, eq, neg, final_exponentiate, multiply

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data import A, B, C, witness, srs_g1, srs_g2, alpha_g1, beta_g1, beta_g2, delta_g1, delta_g2, private_psi, eta_g1_div_by_delta, private_psi, gamma_g2, public_psi
from utils import calculate_psi_with_offset, create_t_poly, matrix_to_polynomial, random_gf, evaluate_polynomial

# create polynomials
a_poly_gf = matrix_to_polynomial(A, witness)
b_poly_gf = matrix_to_polynomial(B, witness)
c_poly_gf = matrix_to_polynomial(C, witness)

t_poly_gf = create_t_poly(A.shape[0])
h_poly_gf = (a_poly_gf * b_poly_gf - c_poly_gf) // t_poly_gf

r = random_gf()
s = random_gf()

A_G1 = add(add(evaluate_polynomial(a_poly_gf, srs_g1), alpha_g1), multiply(delta_g1, int(r)))
B_G1 = add(add(evaluate_polynomial(b_poly_gf, srs_g1), beta_g1), multiply(delta_g1, int(s)))
B_G2 = add(add(evaluate_polynomial(b_poly_gf, srs_g2), beta_g2), multiply(delta_g2, int(s)))


private_psi_sum = calculate_psi_with_offset(witness, private_psi, 2)
HT_G1 = evaluate_polynomial(h_poly_gf, eta_g1_div_by_delta)
A1_s = multiply(A_G1, int(s))
B1_r = multiply(B_G1, int(r))
r_s_delta = neg(multiply(delta_g1, int(r * s)))

C_G1 = add(add(add(add(private_psi_sum, HT_G1), A1_s), B1_r), r_s_delta)

# prover has calculated everything 
# now it's verifier turn

X_G1 = calculate_psi_with_offset(witness, public_psi, 0)

assert(eq(FQ12.one(), final_exponentiate(pairing(B_G2, neg(A_G1)) * pairing(beta_g2, alpha_g1) * pairing(gamma_g2, X_G1) * pairing(delta_g2, C_G1))))
