# $\LaTeX$ tricks
## `align`  sample

```
Therefore, 
$$ \begin{align*} \\
&d_{k+1}^{(k+1)} = a_k d_k^{(k)} \\ \\
&d_{k}^{(k+1)} = a_k d_{k - 1}^{(k)} + b_k d_k^{(k)}\\ \\
& \vdots \\ \\
& d_0^{(k+1)} = b_k d_0^{(k)} + c_k d_0^{(k - 1)} \\
\end{align*} 
$$ 
for any $k > 1$
```

### implementation
Therefore, 
$$ \begin{align*} \\
&d_{k+1}^{(k+1)} = a_k d_k^{(k)} \\ \\
&d_{k}^{(k+1)} = a_k d_{k - 1}^{(k)} + b_k d_k^{(k)}\\ \\
& \vdots \\ \\
& d_0^{(k+1)} = b_k d_0^{(k)} + c_k d_0^{(k - 1)} \\
\end{align*} 
$$ 
for any $k > 1$
