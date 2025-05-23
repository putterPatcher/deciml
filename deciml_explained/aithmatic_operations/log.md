## the *"log"* function

```python
def log(cls,__a:float|int|str|Decimal,__b=constant.e(),__pr=getpr())->Decimal:
```

```python
p=__pr+2
a=Decimal(str(__a));b=Decimal(str(__b));c=0;
```

```python
if b>=1:
    if a>=1:
        while a>b:a=cls.div(a,b,p);c+=1;
        return deciml(str(c)+"."+str(a.ln()/b.ln())[2:],__pr);
    if a<1:
        while a<1:a=cls.mul(a,b,pr=p);c+=1;
        return deciml(str(-c)+"."+str(a.ln()/b.ln())[2:],__pr);
if b<1:
    if a>=b:
        while a>b:a=cls.mul(a,b,pr=p);c+=1;
        return deciml(str(-c)+"."+str(a.ln()/b.ln())[2:],__pr);
    if a<b:
        while a<b:a=cls.div(a,b,p);c+=1;
        return deciml(str(c)+"."+str(a.ln()/b.ln())[2:],__pr);
```

This is a very complex problem. We need to decide the precision after division of log values. So we just need to find the values of the integer part after the division. So what is a log value. We know that log(1) is 0, and log(10) is 1. Also log(0) tends to negative infinity and log(1) is 0. Also when numbers are divided, if the numerator is greater than the denominator we get a value between (0, 1) and if the denominator is greater than the numerator we get a value greater than 1.

### conditions 1:
1. if (a > 1) and (b > 1) => the log will be positive
2. if (a > 1) and (b < 1) => the log will be negative
3. if (a < 1) and (b > 1) => the log will be negative
4. if (a < 1) and (b < 1) => the log will be positive

### conditions 2:
1. if (log(a) > log(b)) => the log is greater than 1
2. if (log(a) < log(b)) => the log is less than 1

So to calculate the decimal part we need to have a number in the numerator that is less than log(b). The remaining part of the numerator should be a constant. For the remaining part of the numerator to be a constant it should be divisible by log(b).

### conditions 3:
1. if (a > b) => if (a > 1), then the number will be negative. if (a < 1), then the number will be positive.
2. if (b > a) => if (a > 1), then the number will be positive. if (a < 1), then the number will be negative or positive.
So, this approach of a > b and b > a cannot be used.

So we need to use the conditions 1 and conditions 2.

Also we can ignore the condition where b = 1. This can be handled later if necessary.

If (b > 1) and (a > 1) we know that the number will be positive. So now we need a way to figure out weather the number will be greater than 1 or less than 1.
For number to be less than 1, we know that the numerator should be less than the denominator. So log(a) < log(b).
For number to be greater than 1, we know that the denominator should be less than the numerator. So log(a) > log(b).

We need to find a case such that the result should be greater than 1 to visualize that the number is a sum of a decimal and integer part.
That case is (1 > b > 10) and a > 10. If we do this then we will get a number that has an integer part and an decimal part.

The code can be explained as by using the expression,
#### log((b^c)*n)/log(b) = c + log(n)/log(b)

Here we can understand that we need to perform some multiplication or division operation.

As from the equation, I saw that "b" is being used. So I decided to start from using "b". From here we need to find c.
To find "c" we need to evaluate all the conditions.

A. First let us consider the condition b < 1. Because I think it is convinient. 

1. For the condition, a < b.

    a < b, log(a) < log(b) as log is a continiously increasing function.
    Also as b < 1. log(b) is negative. Therefore log(a) is also negative. But log(a) is more negative than log(b). Therefore, log(a)/log(b) will be greater than 1.

    '''
    
    -0.5/-0.012 = 41.666666666666664

    -10/-3 = 3.3333333333333335

    '''

    So now if we divide a by b,

    '''

    0.05/0.13 = 0.38461538461538464

    0.38461538461538464/0.13 = 2.9585798816568047

    '''

    We can see that the number is increasing.

    The other case where we multiply a and b. We see that the number is decreasing.
    So we can work with the increasing method. If we keep on increasing the number we reach a point where the number becomes greater than b. From that point the number will keep on increasing as b < 1. So we have found a "c". We know that a number divided by itself is 1. And a number less than 1 divided by a number "less than 1 but also more than the first number, and close to the first number will be less than 1" because then the denominator **"log(b)"** will tend to zero. This number being greater than b.

    So now we have two numbers, "n" which is greater than "b" and less than 1 and "b" which is less than 1. So log(n) will be more close to 0 than log(b). And log(n)/log(b) will be less than 1 and positive. So we can use this to calculate log(a)/log(b) to the given precision value. We use the natural log at it is more inherent. And the decimal precision takes care of the precision as the number has only a decimal part.

2. For the condition a >= b,

    We know that if we multiply a number more than 1 with a number less than 1. We get a smaller number. Also if we multiply a number less than 1 but greater than the other number we get a number less than 1.
    So we can use this by multiplying the "a" to "b". To find a number less than "b". This is the same as dividing "a" by "b^-1". So the "c" will be the negative of the number of multiplications. But log(n)/log(b) can be greater than 1.
    So we'll consider the cases separately.

    The first case, a > 1.

    We can multiply a and b until we get a number less than 1. And if we multiply a number by 1, we get the same number. So, we know that the number obtained after multiplication will be less than 1 and greater than "b". So, considering the number of multiplication steps to be "c" and the number obtained to be "n". We will get the result as "-c + log(n)/log(b)".
    The second case, a < 1.
    We know that for a < 1 and b < 1, where a is greater than b. We will obtain a number less than 1. So we can directly get the value with the desired precision i.e. log(a)/log(b)

    This can be summarized into one equation. Because here we have considered the constraint on the multiplied value to be greater than "b". If we condider the multiplied value to be the new "a". We get the second case to be "c = 0".

B. Now consider the condition b > 1.

We have now understood that the number obtained should be such that log(n)/log(b) should be less than 1.

1. For the condition a > b.
    If we keep on dividing "a" by "b" we at some point obtain a number less than b. We know that a number divided by itself is 1. So a number greater number divided by a smaller number will be more than 1. We konw that log is a increasing function. The number "n" will be greater than 1 but less than "b". Since log(1) is 0, log(n)/log(b) will be less than 1. Following the same logic the result will be "c + log(n)/log(b)".

2. For condition a < b.
    There are two condition,

    The first case a < 1.
    We know that log(a) will be negative. Similarly, log(b) is positive. So we multiply "a" and "b". Then at some point we get a value greater than 1. We know that if a number is multiplied by 1, we get the same value, so multipying a number less than 1, "a", will return a number less than "b". So we get the "c" i.e. the number of multiplication steps and "n" that is the number obtained. Since we multiplied the result will be "-c + log(n)/log(b)".

    The second case a > 1.
    We can divide "a" by "b", until we obtain a number less than "b". After that we get the result as "c + log(n)/log(b)".

    We can see that the code can be summerized by just two conditions. i. a < 1 and ii. a > 1.