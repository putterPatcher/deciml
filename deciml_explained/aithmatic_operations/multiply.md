## the *"mul"* function

```python
def mul(*__a:float|int|str|Decimal,pr=getpr())->Decimal:
```

```python
p=pr+2
r=str(__a[0])
for i in __a[1:]:
		r=str(__mul(r,str(i)))
    if r=='None':raise Exception;
return deciml(r,pr)
```

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

```python
a,b=map(__exp,(__a,__b))
if a is None or b is None:raise Exception
an=str(int(a[0].lstrip('-').split('.')[0]));bn=str(int(b[0].lstrip('-').split('.')[0]));
if (p1:=int(a[1])+int(b[1])+len(an)+len(bn))>0:getcontext().prec=p1+p;
else:getcontext().prec=p;
return str(Decimal(__a)*Decimal(__b))
```

Here we use the "__exp" function to split the string into a non exponential part and an exponential part. Then we calculate the number of decimal digits after the multiplication and set the precision accordingly. After that we return the Decimal object.
