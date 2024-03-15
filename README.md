# AutoStencilPy

This package provides an algorithmic method for calculating the form of [higher order derivative approximations](https://en.wikipedia.org/wiki/Finite_difference#Higher-order_differences) for use in numerically solving [ordinary and partial differential equations](https://en.wikipedia.org/wiki/Finite_difference). It is inspired by Cameron Taylor's ["Finite Difference Coefficients Calculator"](http://web.media.mit.edu/~crtaylor/calculator.html).

## Approach

Given a single variable function $`f`$ in $`x`$, the aim is to take $`N`$ sample, or stencil points, in $`f(x)`$, to approximate the derivative of order $`d`$, where $`d < N`$. This problem can be reduced to solving a set of $`N`$ simultaneous equations,


$`s_1^nc_1 + \ldots + s_N^nc_N = \frac{d!}{h^d}\delta(n-d) \mbox{ for } 0 \leq n \leq N-1,`$

where we seek to find the coefficients $`c_i`$. This set of equations can be written in matrix form as

$`\begin{bmatrix}
    s_1^0 &  \ldots & s_N^0 \\
    \vdots &  \ddots & \vdots \\
    s_1^{N-1} &   \ldots & s_N^{N-1} \\
\end{bmatrix}
\begin{bmatrix}
		c_1 \\ \vdots \\ c_N
\end{bmatrix}
		=
		\frac{1}{h^d}
\begin{bmatrix}
		0 \\ \vdots \\ d! \\ \vdots \\ 0
\end{bmatrix},`$

where the $`d!`$ element on the LHS is in the $`d`$th row. By finding the inverse of the matrix, one can arrive at the coefficients $`c_i`$ of the stencil

$`\begin{bmatrix}
		c_1 \\ \vdots \\ c_N
\end{bmatrix}
		=
		\frac{1}{h^d}
\begin{bmatrix}
		s_1^0 &  \ldots & s_N^0 \\
		\vdots &  \ddots & \vdots \\
		s_1^{N-1} &   \ldots & s_N^{N-1} \\
\end{bmatrix}^{-1}
\begin{bmatrix}
		0 \\ \vdots \\ d! \\ \vdots \\ 0
\end{bmatrix}.`$
