# The "add" function


```python
def add(*__a:list[Decimal]|tuple[Decimal,...],pr=getpr())->tuple[Decimal,...]:
		try:return tuple(map(lambda x:algbra.add(*x,pr=pr),zip(*__a)));
    except Exception as e:print("Invalid command: galgra.add\n",e);
```

```python
p=pr+2
r=str(__a[0])
for i in __a[1:]:
		r=str(__add(r,str(i)))
    if r=='None':raise Exception;
    return deciml(r,pr)
```

Here we call the function ***"__add"*** in a loop to add the numbers. And return the Decimal object using the deciml function.

```python
def __add(__a:str,__b:str)->Decimal:
```

The "__add" function takes two strings are arguments and returns a Decimal object. The function is explained below.

```python
a,b=map(__exp,(__a,__b))
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

The ***"__exp"*** function splits the string into a list containing the non exponential part and the exponential part.

```python
an=str(int(a[0].lstrip('-').split('.')[0]));bn=str(int(b[0].lstrip('-').split('.')[0]));d1=len(an)+int(a[1]);d2=len(bn)+int(b[1]);
if d1>d2:
		if d1>0:getcontext().prec=p+d1;
    else:getcontext().prec=p;
else:
  	if d2>0:getcontext().prec=p+d2;
    else:getcontext().prec=p;
return str(Decimal(__a)+Decimal(__b))
```

Here we split the non exponential string into two parts (integer and decimal). Then we calculate the length of the string assuming that the string can be represented as a number having some integer and decimal part. If the length of the assumed number (i.e "assumed length" of the integer part) for "__a" is greater than the length of the assumed number for "__b".
1. If the "assumed length" for "__a" is greater than zero then we add the length to "p" and set it as the precision provided by the decimal library.
2. For the other case, we know that if the Decimal object is initialized with a string as argument it is safely converted to the proper decimal value. So we assume the precision to be "p", from the fact that the number had no integer part because it is being added. The number in the Decimal object is converted to a string having the precision that does not assume the leading zeros with the addition of an exponential part.

We know the addition occurs around the decimal point. Therefore, both the cases should be treated the same. As they will have the same exponential value.

```python
getcontext().prec=5
print(Decimal('12.12345')+Decimal('0.1234'))
getcontext().prec=4
print(Decimal('0.12345')+Decimal('0.1234'))
```

12.247 and 0.2469 do not have the same decimal digits.
