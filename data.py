import numpy as np
from py_ecc.bn128 import G1, G2, multiply, add, pairing, FQ12, curve_order
from utils import create_eta, create_psi, create_t_poly, GF, get_private_psi, get_public_psi, matrix_to_polynomial, random_gf, create_srs, evaluate_polynomial, divide_eta_by_delta

# Generated by verifier:
# - R1CS
A = np.array([[0,0,3,0,0,0],
               [0,0,0,0,1,0],
               [0,0,1,0,0,0]])

B = np.array([[0,0,1,0,0,0],
               [0,0,0,1,0,0],
               [0,0,0,5,0,0]])

C = np.array([[0,0,0,0,1,0],
               [0,0,0,0,0,1],
               [-3,1,1,2,0,-1]])
t_poly_gf = create_t_poly(A.shape[0])
# powers of tau
tau = random_gf()
alpha = random_gf()
beta = random_gf()
alpha_g1 = multiply(G1, int(alpha))
beta_g2 = multiply(G2, int(beta))
srs_g1 = create_srs(G1, tau, A.shape[0])
srs_g2 = create_srs(G2, tau, A.shape[0])
eta_g1 = create_eta(G1, tau, A.shape[0], t_poly_gf)
psi = create_psi(A, B, C, alpha, beta, tau)

# data for final task on Groth16
gamma = random_gf()
delta = random_gf()

eta_g1_div_by_delta = divide_eta_by_delta(eta_g1, delta)

public_psi = get_public_psi(psi, gamma, 1)
private_psi = get_private_psi(psi, delta, 2)

beta_g1 = multiply(G1, int(beta))
gamma_g2 = multiply(G2, int(gamma))
delta_g1 = multiply(G1, int(delta))
delta_g2 = multiply(G2, int(delta))



# Prover solves the R1CS
x = 1000
y = 1000

out = 3 * x * x * y + 5 * x * y - x- 2*y + 3
v1 = 3*x*x
v2 = v1 * y

# first two elements are public, others solved by prover and not revealed to the verifier
witness = np.array([1, out, x, y, v1, v2], dtype=object)
