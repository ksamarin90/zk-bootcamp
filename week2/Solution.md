# 1. Let our set be real numbers. Show a binary operator that is not closed

It is a division since dividing by zero doesn't produce the element of the set. 
But division would be fine if we exclude 0 from the set, then it becomes closed.

We could also specify arbitrary operator which does not produce real number.
That could be anything, for instance concatenation of numbers to string (e.g. 1.3 @ 5 = "1.35").

# 2. Find a binary operator that is closed but not associative for real numbers

It is subtraction.

(a - b) - c = a - b - c
while
a - (b - c) = a - b + c
thus 
(a - b) - c != a - (b - c)

# 3. What algebraic structure (group, monoid, semigroup, etc) is all even integers under addition

{... -2, 0, 2, 4, 6 ...} under +

1. Operator is closed (even integers are always produced)
2. Operator is associative (also commutative)
3. Identity element is 0
4. All elements have an inverse

Thus we are speaking about abelian group.

# 4. What algebraic structure is all odd integers under multiplication?

{... -3, -1, 1, 3, 5, 7} under *

1. Operator is closed (odd integers as result)
2. Operator is associative
3. Identity element is 1
4. Not all elements have an inverse (aka 7 should be 1 / 7 to give identity 1)

Thus this is monoid.

# 5. Let our set be 3 x 2 matrices of integers under addition. What algebraic structure is this?

[a, b] + [e, f] = [a + e, b + f]
[c, d]   [g, h]   [c + g, d + h]

1. Operator is closed (if two matrices are added their elements are simply added together)
2. Operator is associative (also commutative)
3. Identity element is zero matrix (all elements are zero)
4. All matrices have an inverse (multiple all elements of matrix by -1)

Thus this is abelian group.

# 6. Suppose our set is all rational numbers Q except 0 and our binary operator is division. What algebraic structure is this?

1. Operator is closed (0.3333..33 can be expressed as 1/3 => rational number)
2. Operator is NOT associative: a / (b / c) != (a / b) / c since: ac / b != a / bc
3. There is NO identity element (1 / a != a / 1, one might think that 1 could be an identity)
4. All elements have an inverse (a / b => b / a) WRONG

Thus this is a magma.

# 7. Suppose our set is A B C
    1. Define a binary operator that makes it a group. You can define the binary operator’s property by constructing a table where the left two columns are the inputs and the right column is the result. Remember you need to allow that the inputs can be the same, for example (A, A) —> ?
    2. Define a binary operator that makes it *not* a group (but it should be closed). Hint: if there is no identity element, then it is not a group

1) 
Operator @:

    A   B   C
A   B   C   A

B   C   A   B

C   A   B   C  

1. @ is closed
2. @ is associative:
    A @ (B @ C) = A @ B = C
    (A @ B) @ C = C @ C = C
and commutative
    A @ B = C
    B @ A = C
3. Identity element is C
4. Each element has an inverse
    A @ B = C
    B @ A = C
    C @ C = C

2) 
Operator @:

    A   B   C
A   B   C   C

B   C   B   A

C   C   A   B  


# 8. What is the size of the smallest possible group? (Remember, a group is a set, so this is asking how large the set is)

One.

0 under + or 1 under *.