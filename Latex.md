# 极限

$$
\lim_{x \to \infty}f\left(x\right)=
\frac{sin(x)}{x}
$$
![latex](.//Images/Figure_1.svg)

# 数列
$$
s_n=n \cdot a_1+\frac{n(n-1)}{2} \cdot d = \frac{n(a_1+a_n)}{2}
$$
$$
s_n=a_1 \cdot \frac{1-q^n}{1-q}=\frac{a_1-a_n \cdot q}{1-q}
$$

# 导数
$$
f' \left( x_1 \right)=\lim_{x_1 \to x_2}\frac{f(x_2)-f(x_1)}{x_2-x_1}
$$

> 令  $h=x_2-x_1$,则

$$
f'\left(x_1\right)=\lim_{h \to 0}\frac{f(x_1+h)-f(x_1)}{h}
$$

# 连续性和可导性

- 连续性
    1. 双侧极限存在
    2. 函数在 x=a 处有定义，即 f(a) 存在 
    3. $\lim_{x \to a}f(x)=f(a)$
- 可导性
    1. 可导——>连续