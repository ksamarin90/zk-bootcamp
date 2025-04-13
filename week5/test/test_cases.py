from py_ecc.bn128 import G1, add, multiply, curve_order, is_on_curve
# from fractions import Fraction

# a + b = c

# # 12 + 97 = 109
# a = 12
# b = 97
# c = a + b

# A = multiply(G1, a)
# B = multiply(G1, b)

# C = add(A, B)
# C_derived = multiply(G1, c)

# 12/47 + 33/48 = 709/752
a = 12 * pow(47, -1, curve_order) % curve_order
b = 33 * pow(48, -1, curve_order) % curve_order
c = (a + b) % curve_order
# print(a)

A = multiply(G1, a)
B = multiply(G1, b)

print(A)
print(B)

C = add(A, B)
C_derived = multiply(G1, c)

assert(C == C_derived);