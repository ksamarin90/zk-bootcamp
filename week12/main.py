# from py_ecc.bn128 import G1, G2, pairing, FQ12

# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from data import A, B, C, witness
# from utils import create_t_poly, GF, matrix_to_polynomial, random_gf, create_srs, evaluate_polynomial, create_eta

# # create polynomials
# a_poly_gf = matrix_to_polynomial(A, witness)
# b_poly_gf = matrix_to_polynomial(B, witness)
# c_poly_gf = matrix_to_polynomial(C, witness)

# t_poly_gf = create_t_poly(A.shape[0])
# h_poly_gf = (a_poly_gf * b_poly_gf - c_poly_gf) // t_poly_gf

# # continue trusted setup

