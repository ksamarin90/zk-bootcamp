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


def validateScalar(x, y):
    p = (x - 1) * (x - 2)
    q = (y - 1) * (y - 2)
    r = x * y
    s = (r - 2) * (r - 3)
    # [1, x, y, p, q, r, s]
    witness = np.array([1, x, y, p, q, r, s])
    result = (np.multiply(np.matmul(L, witness), np.matmul(R, witness)) - np.matmul(O, witness)) == np.matrix([0, 0, 0, 0, 0, 0, 0])
    return result.all()

# Wrong solutions
assert validateScalar(0, 1) == False
assert validateScalar(1, 4) == False
assert validateScalar(1, 1) == False
assert validateScalar(2, 2) == False
assert validateScalar(3, 3) == False
# Valid solutions
assert validateScalar(1, 2)
assert validateScalar(2, 3)
assert validateScalar(3, 1)


# Problem 3

from py_ecc.bn128 import G1, G2, curve_order, multiply, pairing, neg, add, FQ12, eq

def getScalarVector(x, y):
    p = (x - 1) * (x - 2)
    q = (y - 1) * (y - 2)
    r = x * y
    s = (r - 2) * (r - 3)
    return [1, x, y, p, q, r, s]

def toG1(x):
    result = []
    for xi in x:
        result.append(multiply(G1, xi))
    return result

def toG2(x):
    result = []
    for xi in x:
        result.append(multiply(G2, xi))
    return result

def validateG12(x, y):
    v = getScalarVector(x, y)
    vG1 = toG1(v)
    vG2 = toG2(v)
    # validate discrete log first
    for i in range(len(vG1)):
        a = pairing(G2, vG1[i])
        b = pairing(vG2[i], G1)
        if eq(a, b) != True:
            return False
    numberOfRows = O.shape[0]

    def sumRow(row, rowG, G):
        row = np.array(row).flatten()
        result = neg(multiply(G, -1 * row[0])) if row[0] < 0 else multiply(G, row[0])
        for i in range(len(row)):
            if i == 0:
                continue
            if (row[i] < 0):
                result = add(result, neg(multiply(rowG[i], row[i] * -1)))
            else:
                result = add(result, multiply(rowG[i], row[i]))
        return result
                
    for i in range(numberOfRows):
        lG1 = sumRow(L[i], vG1, G1)
        rG2 = sumRow(R[i], vG2, G2)
        oG1 = sumRow(O[i], vG1, G1)
        isEqual = eq(pairing(rG2, lG1), pairing(G2, oG1))
        if isEqual == False:
            return False

    return True

# Wrong solutions
assert validateG12(0, 1) == False
assert validateG12(1, 4) == False
assert validateG12(1, 1) == False
assert validateG12(2, 2) == False
assert validateG12(3, 3) == False

# Valid solutions
assert validateG12(1, 2)
assert validateG12(2, 3)
assert validateG12(3, 1)



# **Problem 4**
# Why does an R1CS require exactly one multiplication per row?
# How does this relate to bilinear pairings?

# Answer:
# Pairing which resembles multiplication can be done only once using
# G1 and G2 giving G12.
# Once we have G12 we cannot "multiply" aka pair G12 with G12.
# For that reason we need to provide witness vector encoded in G1 and G2 so that
# we could do pairing per constraint.