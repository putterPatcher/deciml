# the "div" function

```python
def div(__a:float|int|str|Decimal,__b:float|int|str|Decimal,__pr=getpr())->Decimal:
```

The ***"div"*** function has arguments ***"__a"*** i.e the numerator, ***"__b"*** i.e. the denominator and ***"__pr"*** i.e. the precision for the returned Decimal value.

```python
def __exp(__a)->list:
		match len(a1:=__a.split('E')):
    		case 1:
      			match len(a2:=__a.split('e')):
            		case 1:return a2+['0',];
                case 2:return a2;
                case _:return None;
        case 2:return a1;
        case _:return None;
```

Here we split the string into a non exponential part and exponential part.

```python
p=__pr+2
a,b=map(__exp,(str(__a),str(__b)))
if a is None or b is None:raise Exception
an=str(int(a[0].lstrip('-').split('.')[0]));bn=str(int(b[0].lstrip('-').split('.')[0]));
if (p1:=int(a[1])-int(b[1])+len(an)-len(bn))>0:getcontext().prec=p1+p;
else:getcontext().prec=p;
return deciml(Decimal(__a)/Decimal(__b),__pr)
```

We calculate the decimal digits. And then we return the Decimal object using the deciml function with the desired precision.
