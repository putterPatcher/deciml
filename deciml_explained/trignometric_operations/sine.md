## The *"sin"* function

```python
def sin(__a:Decimal|int|float|str,__pr=getpr())->Decimal:
```

The function ***"sin"*** is given a number ***"__a"*** and a precision ***"__pr"***. It returns the sine value of the number with the given precision.

```python
pr = __pr+2
if (a:=Decimal(str(__a)))>(p:=algbra.mul(constant.pi(pr),'2',pr=pr)):a='0.'+str(algbra.div(a,p,pr+1)).split('.')[1];a=algbra.mul(a,p,pr=pr);
```

Here we check if the number is greater than 2*pi. If it is then we divide the number by 2*pi as the sine function has a period of 2*pi and get the number after the decimal value. Then we multiply the number by 2*pi to get the value to calculate the sine.

```python
elif a<algbra.mul('-1',p,pr=pr):a='-0.'+str(algbra.div(a,p,pr+1)).split('.')[1];a=algbra.mul(a,p,pr=pr);
```

Here we check if the number is less than -2*pi and do the same thing as we did previously. But just for a negative value.

```python
rp=None;n=a;d=1;c=1;a1=algbra.pwr(a,'2',pr+1);r=algbra.div(n,d,pr+1);
while r!=rp:rp=r;r=algbra.add(r,algbra.div((n:=algbra.mul(n,a1,'-1',pr=pr+2)),(d:=d*(c+1)*((c:=c+2))),pr+1),pr=pr);
return deciml(r,__pr);
```

Here we use taylor series to find the sine of the number.
### $\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \frac{x^9}{9!} ...$

### $\sum_{i=0}^n \frac{x(-x)^{2i}}{(2i+1)!}$

Here we set the variables "rp", "n", "d", "c", "a1", and "r". Here "rp" is the previous result after an iteration and "r" is the result of the iteration. a1 is the square of the intial value. And r is the result of the first iteration meaning the first value in the summation. Then we calculate the the values in the summation for the required precision using the summation formula. Here "d" is the factorial of previous value and "c" is the number for factorial value of the next iteration.

