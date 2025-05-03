# The *"cos"* function

```python
def cos(__a:Decimal|int|float|str,__pr=getpr())->Decimal:
```

The ***"cos"*** function returns the cosine with a precision ***__pr*** of the number ***__a***.

```python
pr=__pr+2
if (a:=Decimal(str(__a)))>(p:=algbra.mul(constant.pi(pr),'2',pr=pr)):a='0.'+str(algbra.div(a,p,pr+1)).split('.')[1];a=algbra.mul(a,p,pr=pr);
elif a<algbra.mul('-1',p,pr=pr):a='-0.'+str(algbra.div(a,p,pr+1)).split('.')[1];a=algbra.mul(a,p,pr=pr);
```

Here we calcuate the value for number greater than 2*pi and less than 2*pi.

```python
rp=0;n=1;d=1;c=0;r=1;a1=algbra.pwr(a,'2',pr);
while r!=rp:rp=r;r=algbra.add(r,algbra.div((n:=algbra.mul(n,a1,'-1',pr=pr+2)),(d:=d*(c+1)*((c:=c+2))),pr+1),pr=pr);
return deciml(r,__pr);
```

### $\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \frac{x^8}{8!}$
### $\sum_{i=0}^n \frac{x^{2i}(-1)^{i}}{(2n)!}$

Then we calculate till the required precision by calculating the values in the summation.