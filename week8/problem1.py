# **Problem 1**
# Create a graph with 2 nodes and 1 edge and write constraints for a 3-coloring. 
# T the 3-coloring to a rank 1 constraint system. If you forgot how to do this, consult the chapter on arithmetic circuits.

# Solution:

# Red - 1, Blue - 2, Green - 3

# Invalid nodes
# 1 * 1 = 1
# 2 * 2 = 4
# 3 * 3 = 9
# Valid nodes
# 1 * 2 = 2
# 2 * 3 = 6
# 3 * 1 = 3
# 2 * 1 = 2
# 3 * 2 = 6

# Constraints:
# (x - 1)(x - 2)(x - 3) = 0
# (y - 1)(y - 2)(y - 3) = 0
# (xy - 2)(xy - 3)(xy - 6) = 0

# R1CS:
# p = (x - 1)(x - 2)
# 0 = p(x - 3)
# q = (y - 1)(y - 2)
# 0 = q(y - 3)
# r = xy
# s = (r - 2)(r - 3)
# 0 = s(r - 6)

# [1, x, y, p, q, r, s]

# O
# [0, 0, 0, 1, 0, 0, 0]
# [0, 0, 0, 0, 0 ,0 ,0]
# [0, 0, 0, 0, 1, 0, 0]
# [0, 0, 0, 0, 0 ,0 ,0]
# [0, 0, 0, 0, 0, 1, 0]
# [0, 0, 0, 0, 0, 0, 1]
# [0, 0, 0, 0, 0 ,0 ,0]

# L 
# [-1, 1, 0, 0, 0, 0, 0]
# [0, 0, 0, 1, 0, 0, 0]
# [-1, 0, 1, 0, 0, 0 ,0]
# [0, 0, 0, 0, 1, 0, 0]
# [0, 1, 0, 0, 0, 0 ,0]
# [-2, 0, 0, 0, 0, 1, 0]
# [0, 0, 0, 0, 0, 0, 1]

# R
# [-2, 1, 0, 0, 0, 0, 0]
# [-3, 1, 0, 0, 0, 0, 0]
# [-2, 0, 1, 0, 0 ,0, 0]
# [-3, 0, 1, 0, 0, 0, 0]
# [0, 0, 1, 0, 0, 0, 0]
# [-3, 0, 0, 0, 0, 1, 0]
# [-6, 0, 0, 0, 0, 1, 0]

import numpy as np

O = np.matrix([[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0 ,0 ,0],
[0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0 ,0 ,0],
[0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0 ,0 ,0]])

L = np.matrix([[-1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0],
[-1, 0, 1, 0, 0, 0 ,0],
[0, 0, 0, 0, 1, 0, 0],
[0, 1, 0, 0, 0, 0 ,0],
[-2, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 1]])

R = np.matrix([[-2, 1, 0, 0, 0, 0, 0],
[-3, 1, 0, 0, 0, 0, 0],
[-2, 0, 1, 0, 0 ,0, 0],
[-3, 0, 1, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0],
[-3, 0, 0, 0, 0, 1, 0],
[-6, 0, 0, 0, 0, 1, 0]])


def validate(x, y):
    p = (x - 1) * (x - 2)
    q = (y - 1) * (y - 2)
    r = x * y
    s = (r - 2) * (r - 3)
    # [1, x, y, p, q, r, s]
    witness = np.array([1, x, y, p, q, r, s])
    result = np.matmul(O, witness) == np.multiply(np.matmul(L, witness), np.matmul(R, witness))
    return result.all()

print("Wrong solutions")
print(validate(0, 1))
print(validate(1, 4))
print(validate(1, 1))
print(validate(2, 2))
print(validate(3, 3))
print("")
print("Valid solutions")
print(validate(1, 2))
print(validate(2, 3))
print(validate(3, 1))