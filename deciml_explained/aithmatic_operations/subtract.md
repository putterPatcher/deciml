
## The *"sub"* function

```python
def sub(*__a:float|int|str|Decimal,pr=getpr())->Decimal:
```

```python
p=pr+2
r=str(__a[0]);
for i in __a[1:]:
		r=str(__sub(r,str(i)))
    if r=='None':raise Exception;
    return deciml(r,pr)
```

This loops over the values and subtracts.

***Note - All the next numbers are subtracted from the first number.***

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

Split the number into non exponential and exponential part and returns the list.

```python
a,b=map(__exp,(__a,__b))
if a is None or b is None:raise Exception
an=str(int(a[0].lstrip('-').split('.')[0]));bn=str(int(b[0].lstrip('-').split('.')[0]));d1=len(an)+int(a[1]);d2=len(bn)+int(b[1]);
if d1>d2:
		if d1>0:getcontext().prec=p+d1;
    else:getcontext().prec=p;
else:
  	if d2>0:getcontext().prec=p+d2;
    else:getcontext().prec=p;
return str(Decimal(__a)-Decimal(__b))
```

This works the same as "add" function but subtracts in the end. The precision assumption is still the same.
