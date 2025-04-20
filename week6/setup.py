from py_ecc.bn128 import G1, G2, curve_order, multiply, pairing, neg, add, FQ12

# 0 = -A_1B_2 +\alpha_1\beta_2 + X_1\gamma_2 + C_1\delta_2  

# I will take arbitrary number and calculate a or b specifying one of them in the end
alpha = 2124634634634223
beta = 124636245745745
gamma = 721317657124187
delta = 261816264818
c = 7657651237657612
x1 = 33242523462
x2 = 3523523523
x3 = 662526412876821412
x = (x1 + x2 + x3) % curve_order
ab = ((alpha * beta) % curve_order + (x * gamma) % curve_order + (c * delta) % curve_order) % curve_order
b = 12365172635712635716517263571623517625367517263571625
a = (ab * pow(b, -1, curve_order)) % curve_order

# check that I haven't done some dumb mistake
assert((a * b) % curve_order == ab)

# now precompute all curve points

# constants
alpha_1 = multiply(G1, alpha)
beta_2 = multiply(G2, beta)
gamma_2 = multiply(G2, gamma)
delta_2 = multiply(G2, delta)

# print(alpha_1)
# print("=====")
# print(beta_2)
# print("=====")
# print(gamma_2)
# print("=====")
# print(delta_2)
# print("=====")

X_1= add(add(multiply(G1, x1), multiply(G1, x2)), multiply(G1, x3))

# print(X_1)

A_1 = multiply(G1, a)
B_2 = multiply(G2, b)
C_1 = multiply(G1, c)

# print(A_1)
# print("====")
# print(B_2)
# print("====")
# print(C_1)

# now compute -A_1B_2 +\alpha_1\beta_2 + X_1\gamma_2 + C_1\delta_2  
# print(A_1)
# print(neg(A_1))
result = pairing(B_2, neg(A_1)) * pairing(beta_2, alpha_1) * pairing(gamma_2, X_1) * pairing(delta_2, C_1)
assert(result == FQ12.one())