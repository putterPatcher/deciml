## The *"pwr"* function

```python
def pwr(cls,__a:float|int|Decimal|str,__b:float|int|Decimal|str,__pr=getpr())->Decimal:
```

This is the function to find the number for a particular number with a particular power.

```python
a=Decimal(str(__a));c=0;p=__pr+2;
if (b:=Decimal(str(__b)))==(ib:=int(b)):
    r=1
    if b<0:
        for _ in range(-ib):r=cls.mul(r,a,pr=p);
        r=cls.div(1,r,p)
    else:
        for _ in range(ib):r=cls.mul(r,a,pr=p);
    return deciml(r,__pr)
```


First, if both the numbers are integers, the result is in the above way by multiplying the number "b" number of times if b > 0. If b < 0, then we first calculate by multiplying negative of b number of times and then taking the inverse.

```python
elif a<0:raise Exception;
elif b==0:return Decimal('1');
elif a==0:return Decimal('0');
if a>=1:
    if b>=0:
        while a>1:a=cls.div(a,10,p);c+=1;
        getcontext().prec=int((p1:=cls.mul(c, b, pr=p)))+p;return deciml((10**p1)*(a**b),__pr);
    if b<0:getcontext().prec=p;return deciml(a**b,__pr);
if a<1:
    if b>=0:
        getcontext().prec=p;return deciml(a**b,__pr);
    if b<0:
        while a<1:a=cls.mul(a,10,pr=p);c+=1;
        getcontext().prec=int((p1:=cls.mul(-c, b, pr=p)))+p;return deciml((10**p1)*(a**b),__pr);
except:return Decimal('NaN');
```

'''
(a*(10^n)*(10^(-n)))^b
'''

'''
10**10.76 = 57543993733.71567
10**11 = 100000000000
'''

We will use this equation to explain the code.

A. For the condition a >= 1.

1. The condition b < 0.
We know that that the number will be less than 1. So the precision will be the same.

2. The condition b >= 0.
Divide by 10 till a < 1. Therefore, a**b will be less than 1.
(a*(10^n))^b = a^b*10^(n*b)
getcontext().prec=int((p1:=cls.mul(c, b, pr=p)))+p
10**(xyz.abc) = 10**(xyz)*10**(0.abc)
10**(0.abc) is between [1, 10). Therefore the decimal value will not shift.

B. For the condition a < 1.

1. The condition b < 0.
Multiply by 10 till a > 1. Therefore, a**b will be less than 1.
(a*(10^-n))^b = a^b*10^(-n*b)

2. The condition b >= 0.
We know that that the number will be less than 1. So the precision will be the same.