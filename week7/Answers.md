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
and $y_1$, $y_2$, ... $y_m$ edges.