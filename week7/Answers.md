1. Create an arithmetic circuit that is satisfied if all of the signals $x_1$, $x_2$,... $x_n$ are equal to one. Constrain each signal to be 0 or 1.

$$
\begin{align*}
x_1(x_1 - 1) &= 0 \\
x_2(x_2 - 1) &= 0 \\
&\ldots \\
x_n(x_n - 1) &= 0 \\
x_1 \cdot x_2 \cdot \ldots \cdot x_n &= 1 \\
\end{align*}
$$


2. Create an arithmetic circuit that is satisfied if all of the signals $x_1$, $x_2$,... $x_n$ are equal to zero. Constrain each signal to be 0 or 1.

$$
\begin{align*}
x_1(x_1 - 1) &= 0 \\
x_2(x_2 - 1) &= 0 \\
&\ldots \\
x_n(x_n - 1) &= 0 \\
x_1 + x_2 + \ldots + x_n &= 0 \\
\end{align*}
$$


3. Create an arithmetic circuit that is satisfied if at least one of the signals $x_1$, $x_2$,... $x_n$ equals zero. Constrain each signal to be 0 or 1. Hint: what if you multiply all the signals together?

$$
\begin{align*}
x_1(x_1 - 1) &= 0 \\
x_2(x_2 - 1) &= 0 \\
&\ldots \\
x_n(x_n - 1) &= 0 \\
x_1 \cdot x_2 \cdot \ldots \cdot x_n &= 0 \\
\end{align*}
$$


4. Create an arithmetic circuit that is satisfied if at least one of the signals $x_1$, $x_2$,... $x_n$ equals one. Constrain each signal to be 0 or 1. 

$$
\begin{align*}
x_1(x_1 - 1) &= 0 \\
x_2(x_2 - 1) &= 0 \\
&\ldots \\
x_n(x_n - 1) &= 0 \\
(1 - x_1) \cdot (1 - x_2) \cdot \ldots \cdot (1 - x_n) &= 0 \\
\end{align*}
$$

5. Create an arithmetic circuit that is satisfied if $k$ equals at least one of the signals $x_1$, $x_2$, ..., $x_n$.

$$
\begin{align*}
x_1(x_1 - 1) &= 0 \\
x_2(x_2 - 1) &= 0 \\
&\ldots \\
x_n(x_n - 1) &= 0 \\
(k - x_1) \cdot (k - x_2) \cdot \ldots \cdot (k - x_n) &= 0 \\
\end{align*}
$$


6. Create an arithmetic circuit that is satisfied if the signal $k$ is a power of 2.

1 = 2⁰ = 1  
2 = 2¹ = 10  
4 = 2² = 100  
8 = 2³ = 1000

Ask prover to provide bits of $k$: $k_1$, $k_2$,..., $k_n$.

Then check that:
$$
\begin{align*}
k_1(k_1 - 1) &= 0 \\
k_2(k_2 - 1) &= 0 \\
&\ldots \\
k_n(k_n - 1) &= 0 \\
k_1 + k_2 + \ldots + k_n &= 1 \\
\end{align*}
$$



7. Create an arithmetic circuit that is satisfied if a graph is bipartite. You need a signal to represent each node and constrain the signal to be one of two colors. Then you must constrain neighboring nodes to have different colors.

So $x_1$, $x_2$, ... $x_n$ will be my nodes,
and pairs of $y_{i1}$, $y_{i2}$, ... $y_{in}$ 
along with $z_{i1}$, $z_{i2}$, ... $z_{in}$ 
will be the mask for accessing nodes of the edge. ($y_i$, $z_i$) represent the edge. 1 < i < m where m is the number of edges.

$$
\begin{align*}
x_1(x_1 - 1) &= 0 \\
x_2(x_2 - 1) &= 0 \\
&\ldots \\
x_n(x_n - 1) &= 0 \\
y_{11}(y_{11} - 1) &= 0 \\
y_{12}(y_{12} - 1) &= 0 \\
&\ldots \\
y_{in}(y_{in} - 1) &= 0 \\
z_{11}(z_{11} - 1) &= 0 \\
z_{12}(z_{12} - 1) &= 0 \\
&\ldots \\
z_{in}(z_{in} - 1) &= 0 \\
(x_1 \cdot y_{11} + x_2 \cdot y_{12} + \ldots + x_n \cdot y_{1n} ) + (x_1 \cdot z_{11} + x_2 \cdot z_{12} + \ldots + x_n \cdot z_{1n} ) &= 1 \\
(x_1 \cdot y_{21} + x_2 \cdot y_{22} + \ldots + x_n \cdot y_{2n} ) + (x_1 \cdot z_{21} + x_2 \cdot z_{22} + \ldots + x_n \cdot z_{2n} ) &= 1 \\
&\ldots \\
(x_1 \cdot y_{m1} + x_2 \cdot y_{m2} + \ldots + x_n \cdot y_{mn} ) + (x_1 \cdot z_{m1} + x_2 \cdot z_{m2} + \ldots + x_n \cdot z_{mn} ) &= 1 \\
\end{align*}
$$


8. Create an arithmetic circuit that is satisfied if someone provides a solution to the subset sum problem. The subset sum asks "Given a set $S$ of numbers $e_1$, $e_2$,..., $e_n$, does there exist a subset that adds up to exactly $k$?"

Along with $k$ I expect from prover $k_1$, $k_2$,..., $k_n$ which are constraint to 1 or 0 indicating which elements of set are used in subset sum.

$$
\begin{align*}
k_1(k_1 - 1) &= 0 \\
k_2(k_2 - 1) &= 0 \\
&\ldots \\
k_n(k_n - 1) &= 0 \\
e_1 \cdot k_1 + e_2 \cdot k_2 + \ldots + e_n \cdot k_n &= k \\
\end{align*}
$$



9. Create an arithmetic circuit that is equivalent to `z = !(x && y)`. Assume that `x`, `y`, and `z` are boolean, but you should constrain them to be either 0 or 1.

"!" should be 1 - z = 1;
"&&" should be xy = 1;

$$
\begin{align*}
x(x - 1) &= 0 \\
y(y - 1) &= 0 \\
z(z - 1) &= 0 \\
z &= 1 - x \cdot y 
\end{align*}
$$


10. Create an arithmetic circuit that is equivalent to `z = !(x || y)`. Assume that `x`, `y`, and `z` are boolean, but you should constrain them to be either 0 or 1.

"||" should be x + y - xy = 1


$$
\begin{align*}
x(x - 1) &= 0 \\
y(y - 1) &= 0 \\
z(z - 1) &= 0 \\
z &= 1 - x - y + x \cdot y 
\end{align*}
$$


11. Create an arithmetic circuit that is equivalent to `z = !(x || y) && z`. Assume that `x`, `y`, and `z` are boolean, but you should constrain them to be either 0 or 1.

$$
\begin{align*}
x(x - 1) &= 0 \\
y(y - 1) &= 0 \\
z(z - 1) &= 0 \\
z &= z - x \cdot z - y \cdot z + x \cdot y \cdot z
\end{align*}
$$

12. Create an arithmetic circuit that is equivalent to `a = b & c;` Assume that `a`, `b`, and `c` are unisgned integers with value less than 16, but you should constrain them to be less that 16 using the same techniques discussed in this chapter.

$$
\begin{align*}
a_1(a_1 - 1) &= 0 \\
a_2(a_2 - 1) &= 0 \\
a_3(a_3 - 1) &= 0 \\
a_4(a_4 - 1) &= 0 \\
b_1(b_1 - 1) &= 0 \\
b_2(b_2 - 1) &= 0 \\
b_3(b_3 - 1) &= 0 \\
b_4(b_4 - 1) &= 0 \\
c_1(c_1 - 1) &= 0 \\
c_2(c_2 - 1) &= 0 \\
c_3(c_3 - 1) &= 0 \\
c_4(c_4 - 1) &= 0 \\
a_1 &= b_1 \cdot c_1 \\
a_2 &= b_2 \cdot c_2 \\
a_3 &= b_3 \cdot c_3 \\
a_4 &= b_4 \cdot c_4 \\
\end{align*}
$$