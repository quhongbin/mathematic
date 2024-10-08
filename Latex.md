# 极限



# 数列
$$
s_n=n \cdot a_1+\frac{n(n-1)}{2} \cdot d = \frac{n(a_1+a_n)}{2}
$$
$$
s_n=a_1 \cdot \frac{1-q^n}{1-q}=\frac{a_1-a_n \cdot q}{1-q}
$$



# 连续性和可导性

- 连续性
    1. 双侧极限存在
    2. 函数在 x=a 处有定义，即 f(a) 存在 
    3. $\lim_{x \to a}f(x)=f(a)$
- 可导性
    1. 可导——>连续


# 求解微积分
# 导数
$$
f' \left( x_1 \right)=\lim_{x_1 \to x_2}\frac{f(x_2)-f(x_1)}{x_2-x_1}
$$

> 令  $h=x_2-x_1$,则

$$
\begin{split}
f'\left(x_1\right)&=\lim_{h \to 0}\frac{f(x_1+h)-f(x_1)}{h}即\\
f(x)&=\lim_{h \to 0}\frac{f(x+h)-f(x)}{h}   
\end{split}
$$

定义求导

> 对$1 \over x$求导

$$
\begin{equation}
\begin{split}
\lim_{h \to o}f(x)&=\frac{\frac{1}{x+h}-\frac{1}{x}}{h} \\
&=\frac{-\frac{h}{x(x+h)}} {h} \\
&=-\frac{1}{x(x+h)}\\
&=-\frac{1}{x^2}\\   
\end{split}  
\end{equation}
$$

>对$\sqrt{x}$求导

$$
\begin{equation}
\begin{split}
\lim_{h \to 0}f(x)&=\frac{\sqrt{x+h}-\sqrt{x}}{h} \\
&=\frac{\sqrt{x+h}-\sqrt{x}}{h} \cdot \frac{\sqrt{x+h}+\sqrt{x}}{\sqrt{x+h}+\sqrt{x}} \\
&=\frac{h}{h\cdot(\sqrt{x+h}+\sqrt{x})} \\
&=\frac{1}{\sqrt{x+h}+\sqrt{x}} \\
&\because h \to 0 \\
&=\frac{1}{2\sqrt{x}}
\end{split}
\end{equation}
$$
> 综上所述 $f(x)=x^n$的导数为$f'(x)=n \cdot x^{n-1}$


# 二项式定理
$$
\begin{equation}
\begin{split}
&(a+b)^n=\sum_{r=0}^n C_n^r \cdot a^{n-r} \cdot b^n \\
&二项式展开式的通项公式:T_{r+1}=C_n^r \cdot a^{n-r} \cdot b^n \\
&设 a=b=1,则\\
&2^n=\sum_{r=0}^n C_n^r ,即二项式系数之和为2^n \\
&设 a=-1 \quad b=1,则 \\
&0^n=\sum_{r=0}^n C_n^r\cdot (-1)^{n-r},即(-1)^{n-r} \cdot C_n^r=0
\end{split}
\end{equation}
$$
# 组合数的性质
$$
\begin{equation}
\begin{split}
C_n^m&=C_n^{n-m}\\
C_n^m&=C_{n-1}^m+C_{n-1}^{m-1} \\
C_n^0&=C_n^n=1
\end{split}
\end{equation}
$$

> 现在我们求$f(x)=x^n$的导数

$$
\begin{equation} 
\begin{split}
&f'(x)=\lim_{h \to 0}\frac{(x+h)^n-x^n}{h} \\
&由(3)可知,(x+h)^n的展开式为\\
&C_n^0 \cdot x^n+C_n^1 \cdot x^{n-1} \cdot h +C_n^2 \cdot x^{n-2} \cdot h^2+ \cdots \cdots +C_n^n \cdot x^{n-n} \cdot h^n \\
&\because (4)中组合数的性质可得 \\
&x^n+n \cdot x^{n-1} \cdot h +C_n^2 \cdot x^{n-2} \cdot h^2+ \cdots \cdots +h^n \\
&\therefore f'(x)=\lim_{h \to 0}\frac{x^n+n \cdot x^{n-1} \cdot h +C_n^2 \cdot x^{n-2} \cdot h^2+ \cdots \cdots +h^n-x^n}{h} \\
&则f'(x)=\lim_{h \to 0}\frac{n \cdot x^{n-1} \cdot h +C_n^2 \cdot x^{n-2} \cdot h^2+ \cdots \cdots +h^n}{h} \\
&\Rightarrow f'(x)=\lim_{h \to 0}(n \cdot x^{n-1} +C_n^2 \cdot x^{n-2} \cdot h^1+ \cdots \cdots +h^{n-1}) \\
&\because h \to 0 \\
&\therefore f'(x)=\lim_{h \to 0}(n \cdot x^{n-1}) \\
&即 \frac{\mathrm{d}y}{\mathrm {d}x}=n \cdot x^{n-1},(y=x^n)
\end{split}
\end{equation}
$$


# 三角函数极限和导数
$$
\lim_{x \to \infty}f\left(x\right)=
\frac{sin(x)}{x}
$$
![latex](./Images/Figure_1.svg)

正切函数
$$
\lim_{x \to \infty}f\left(x\right)=
\frac{tan(x)}{x}
$$
![latex](./Images/tan除x.svg)

## 三明治定理

$$
\begin{equation}
\begin{split}
    &\forall {x \in \reals} ,\exists \ {-1\le sin(x) \le 1} \\
    &除以x得-\frac{1}{x} \le \frac{sin(x)}{x} \le \frac{1}{x}
\end{split}
\end{equation}
$$

![latex](./Images/三明治定理.svg)

