## Problem 1

import galois
import numpy as np
import random

p = 71

GF = galois.GF(p)

def vector_to_poly(vector):
    mask = []
    for i in range(1, len(vector) + 1):
        mask.append(i)
    xs = GF(np.array(mask))
    ys = GF(np.array(vector))
    return galois.lagrange_poly(xs, ys)

alice_vector = [54,12,43,1]
bob_vector = [54,12,43,1]

alice_poly= vector_to_poly(alice_vector)
bob_poly= vector_to_poly(bob_vector)

rand = random.randint(0, p)

assert alice_poly(rand) == bob_poly(rand)


# Problem 2

import numpy as np

A = np.matrix([
    [9, 4, 5],
    [8, 3, 4],
    [7, 9, 11]
])

B = np.matrix([
    [2, 4, 6],
    [1, 3, 5],
    [7, 9, 11]
])

v = [1, 3, 7]

def matrix_to_poly(matrix, vector):
    assert matrix.shape[1] == len(vector)
    columns = [matrix[:, i] for i in range(matrix.shape[1])]

    result_poly = GF(0);
    for i in range(len(columns)):
        result_poly += vector_to_poly(np.array(columns[i]).flatten()) * GF(vector[i])

    return result_poly

a_poly = matrix_to_poly(A, v)
b_poly= matrix_to_poly(B, v)

assert(a_poly(rand) == b_poly(rand))