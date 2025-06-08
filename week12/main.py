from py_ecc.bn128 import G1, G2, pairing, FQ12

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data import A, B, C, witness
from utils import create_t_poly, GF, matrix_to_polynomial, random_gf, create_srs, evaluate_polynomial

# assume multi-party computation is done properly on
tau = random_gf()
alpha = random_gf()
beta = random_gf()

# continue trusted setup
# srs1 = 