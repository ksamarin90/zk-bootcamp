from py_ecc.bn128 import G1, add, multiply

# we have 3 EC points:
p = 12
q = 33
r = 21
P = multiply(G1, p)
Q = multiply(G1, q)
R = multiply(G1, r)
# vector of EC points - s
s = [P, Q, R]

# print(s)

# matrix
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# multiply matrix M by s
def ec_matmul(M, s):
    result = []
    for row in M:
        acc = None
        for coeff, point in zip(row, s):
            term = multiply(point, coeff)
            acc = term if acc is None else add(acc, term)
        result.append(acc)
    return result

output_points = ec_matmul(M, s)

for i, pt in enumerate(output_points):
    print(f"Output {i+1}: x={pt[0]}, y={pt[1]}")

# multiply matrix M by scalars and only then convert to EC points
def scalar_matmul_to_ec(M, scalars):
    result = []
    for row in M:
        val = sum(m * s for m, s in zip(row, scalars))
        # print(val)
        point = multiply(G1, val)
        result.append(point)
    return result

ec_points = scalar_matmul_to_ec(M, [p, q, r])

# for i, pt in enumerate(ec_points):
#     print(f"EC Output {i+1}: x={pt[0]}, y={pt[1]}")

for i, (pt1, pt2) in enumerate(zip(output_points, ec_points)):
    same = pt1 == pt2
    print(f"Row {i+1} match: {same}")