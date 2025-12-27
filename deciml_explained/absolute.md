## Absolute value

```python
def abs(__a:float|int|str|Decimal)->Decimal|None:
    a=Decimal(str(__a))
    if (a1:=str(a))=='NaN':return a;
    elif a1=='Infinity' or a1=='-Infinity':return Decimal('Infinity');
    elif a<0:return Decimal(a1[1:]);
    else:return a;
```

The function ***"abs"*** is used to get the absolute value of the number ***"__a"*** which can be a float, int, str or Decimal. The returned values are ***Decimal*** or ***None***. The values are None if the Decimal object contains a value of 'NaN', 'Inf' or '-Inf'.

The logic here is simple. Get the Decimal object. Convert it into a string and select the substring from the second character (i.e. after "-") if the value is less than 0. Then return the Decimal again.
