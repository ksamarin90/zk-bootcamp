# Find a homomorphism for the following pairs of algebraic data structures. 

1) Real numbers under addition to polynomials with real coefficients under addition.

Function phi would be - convert real number to polynomial with exactly that real number coefficients 
(multiply by x2 + x + 1)

Y: {... -1.3, 0, ..., 2...}
B: ax^2 + bx + c

phi(y1 + y2) = phi(y1) + phi(y2)

(y1 + y2)(x2 + x + 1) = y1(x2 + x + 1) + y2(x2 + x + 1)
y1x2 + y1x + y1 + y2x2 + y2x + y2 = y1x2 + y1x + y1 + y2x2 + y2x + y2

2) Polynomials with real coefficients to real numbers under addition. 
Hint: even though this look similar to problem 1, the function will be
completely unrelated to the answer for the previous problem.

Function: apply arbitrary number (say only 2) to the polynomial to get real number

phi(y1 + y2) = phi(y1) + phi(y2)
y1 = 2x2 + 3x + 4
y2 = 3x2 + 2x + 5

5x2 + 5x + 9 = (2) => 20 + 10 + 9 = 39
or
2x2 + 3x + 4 = (2) => 8 + 6 + 4 = 18
3x2 + 2x + 5 = (2) => 12 + 4 + 5 = 21
and sum them together => 18 + 21 = 39


3) Positive real numbers greater than zero under multiplication to all real numbers under addition.

Function: take a logarithm - log_a(bc) = log_a(b) + log_a(c)

phi(y1 * y2) = phi(y1) + phi(y2)

log_6(4) + log_6(9) = log_6(36) = 2
