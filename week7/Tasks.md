
1. Create an arithmetic circuit that is satisfied if all of the signals $x_1$, $x_2$,... $x_n$ are equal to one. Constrain each signal to be 0 or 1.

2. Create an arithmetic circuit that is satisfied if all of the signals $x_1$, $x_2$,... $x_n$ are equal to zero. Constrain each signal to be 0 or 1.

3. Create an arithmetic circuit that is satisfied if at least one of the signals $x_1$, $x_2$,... $x_n$ equals zero. Constrain each signal to be 0 or 1. Hint: what if you multiply all the signals together?

4. Create an arithmetic circuit that is satisfied if at least one of the signals $x_1$, $x_2$,... $x_n$ equals one. Constrain each signal to be 0 or 1. Hint: consider using the gadget $z_i = 1 - x_i$. You can "invert" ones and zeros using that gadget as long as you constrain $x_i$ to be 0 or 1. You a little thought, you can re-use your solution from 3.

5. Create an arithmetic circuit that is satisfied if $k$ equals at least one of the signals $x_1$, $x_2$, ..., $x_n$. Hint: what do you get if you do $k - x_i$?

6. Create an arithmetic circuit that is satisfied if the signal $k$ is a power of 2.

7. Create an arithmetic circuit that is satisfied if a graph is bipartite. You need a signal to represent each node and constrain the signal to be one of two colors. Then you must constrain neighboring nodes to have different colors.

8. Create an arithmetic circuit that is satisfied if someone provides a solution to the subset sum problem. The subset sum asks "Given a set $S$ of numbers $e_1$, $e_2$,..., $e_n$, does there exist a subset that adds up to exactly $k$?" For example, if we have the set $\set{3, 5, 17, 21}$ and $k = 22$, then there does exist a subset that sums up to $k$, which is $\set{5, 17}$. However, if $k$ was 19, there would be no solution. Hint: This is very similar to constraining $k$ to have a binary representation. Remember, your goal is not to find a solution, but to give a set of equations that can be satisfied if someone finds a solution. The person who finds their solution should be able to encode their answer as signals $e_1$, $e_2$,..., $e_n$. An $e_i$ is set to 1 if that element from the set is used and 0 otherwise. In other words, they need a way of expressing that they picked the elements 5 and 17 in the example above. Then the constraints should only be satisfied if the sum of the subset is exactly $k$.

9. Create an arithmetic circuit that is equivalent to `z = !(x && y)`. Assume that `x`, `y`, and `z` are boolean, but you should constrain them to be either 0 or 1.

10. Create an arithmetic circuit that is equivalent to `z = !(x || y)`. Assume that `x`, `y`, and `z` are boolean, but you should constrain them to be either 0 or 1.

11. Create an arithmetic circuit that is equivalent to `z = !(x || y) && z`. Assume that `x`, `y`, and `z` are boolean, but you should constrain them to be either 0 or 1.

12. Create an arithmetic circuit that is equivalent to `a = b & c;` Assume that `a`, `b`, and `c` are unisgned integers with value less than 16, but you should constrain them to be less that 16 using the same techniques discussed in this chapter. Hint: now that you have the binary representation, how can you get the bitwise and result? How can you construct `a` from that?