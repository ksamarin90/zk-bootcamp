import numpy as np

# Define the matrices
A = np.array([[0,0,3,0,0,0],
               [0,0,0,0,1,0],
               [0,0,1,0,0,0]])

B = np.array([[0,0,1,0,0,0],
               [0,0,0,1,0,0],
               [0,0,0,5,0,0]])

C = np.array([[0,0,0,0,1,0],
               [0,0,0,0,0,1],
               [-3,1,1,2,0,-1]])

# pick values for x and y
x = 1000
y = 1000

# this is our orignal formula
out = 3 * x * x * y + 5 * x * y - x- 2*y + 3 # the witness vector with the intermediate variables inside
v1 = 3*x*x
v2 = v1 * y
witness = np.array([1, out, x, y, v1, v2], dtype=object)