[[python_stuff]]
When it comes to `float` numbers, you can use [format specifiers](https://www.python.org/dev/peps/pep-0498/#format-specifiers):

```python
f'{value:{width}.{precision}}'
```

where:

-   `value` is any expression that evaluates to a number
-   `width` specifies the number of characters used in total to display, but if `value` needs more space than the width specifies then the additional space is used.
-   `precision` indicates the number of characters used after the decimal point

What you are missing is the type specifier for your decimal value. In this [link](https://docs.python.org/3.6/library/string.html#format-specification-mini-language), you an find the available presentation types for floating point and decimal.

Here you have some examples, using the `f` (Fixed point) presentation type:

```python
# notice that it adds spaces to reach the number of characters specified by width
In [1]: f'{1 + 3 * 1.5:10.3f}'
Out[1]: '     5.500'

# notice that it uses more characters than the ones specified in width
In [2]: f'{3000 + 3 ** (1 / 2):2.1f}' 
Out[2]: '3001.7'

In [3]: f'{1.2345 + 4 ** (1 / 2):9.6f}'
Out[3]: ' 3.234500'

# omitting width but providing precision will use the required characters to display the number with the the specified decimal places
In [4]: f'{1.2345 + 3 * 2:.3f}' 
Out[4]: '7.234'

# not specifying the format will display the number with as many digits as Python calculates
In [5]: f'{1.2345 + 3 * 0.5}'
Out[5]: '2.7344999999999997'
```

> - Imiguelvargasf, May 14 2018

