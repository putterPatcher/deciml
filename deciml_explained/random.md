## Random Numbers

```python
class rdeciml:
```

The object **rdeciml** is used to get random numbers.

```python
def __init__(self,__a:int|float|Decimal|str,__b:int|float|Decimal|str,__pr=getpr())->None:
```

This object accepts ***"__a"*** and ***"__b"*** as the extremities of the range for the random values. And the ***"__pr"*** argument which is the ***"__DecimalPrecision"*** by default. For integer values "__pr" can be set to 0.

```python
__a=str(__a);__b=str(__b);
__a,__b=tuple(map(__exp,(__a,__b)))
def __exp(__a)->list:
		match len(a1:=__a.split('E')):
    		case 1:
    				match len(a2:=__a.split('e')):
          			case 1:return a2+[0,];
                case 2:return a2 if a2[0]!='' else ['1',a2[1]];
            		case _:return None;
        case 2:return a1 if a1[0]!='' else ['1', a1[1]];
        case _:return None;
```

The Decimal object can contain an exponential part which is denoted by starting with "e" or "E", so we have considered to handle it separately.

We divide the string "__a" and "__b" into a list. This is done by splitting the string at the position at "e" or "E". It is assumed that the returned list can have a maximum length of 2. We can also have a condition where the value is entered in only exponential. This is handled by adding a non exponential part to the value.

```python
a1,b1=tuple(map(__dtd,(__a[0],__b[0])));
def __dtd(__a)->list:
		match len(a1:=__a.split('.')):
  			case 1:return a1+['',];
    		case 2:
        		if a1[0]=='':a1[0]='0';
            return a1;
        case _:return None;
```

Then we split the non exponential part obtained from the list at the decimal point. We return the list after required transformations.

```python
__a,__b=tuple(map(__etd,((__a,a1),(__b,b1))))
def __etd(__a)->list:
		__a,a1=__a
    if (i1a:=int(__a[1]))>=0:
    		if (la1:=len(a1[1]))<i1a:
        		z=''
            for _ in range(i1a-la1):z+='0';
            return [a1[0]+a1[1]+z,'0'];
        elif la1>=i1a:
        		return [a1[0]+a1[1][:(da:=i1a-la1)],a1[1][da:]]
        else:return None
    else:
  			if (la0:=len(a1[0]))<=(ni1a:=-i1a):
        		z=''
            for _ in range(ni1a-la0):z+='0';
            return ['0',z+a1[0]+a1[1]]
        elif la0>ni1a:
            return [a1[0][:(da:=la0-ni1a)],a1[0][da:]+a1[1]]
        else:return None
```

After that we transform the values further. We see if the exponential part is greater than or equal to zero.

For the condition greater than or equal to zero.
1. If the length of the decimal part of the non exponential part less than the exponential value, we add zeros to the transformed non exponential part and return a list as decided. 
2. If the length of the decimal part of the non exponential part is greater than or equal to the value of the exponential part, we return a list such that we have transformed the number into a non exponential representation. We decided to do it using negative indices as it is easy to interpret that the decimal point is shifting to the right by a given amount such that the remaining decimal part after shifting is counted from the end.

For the condition that the exponential part is less than zero.
1. If the length of the integer part of the non exponential part is less than the negative of the value of the exponential part, we return a list in which the representation of the decimal part has added zeros at the start. 
2. And if it is not the case then we shift the decimal point (which is just an interpretation) to the left.

```python
self.__oa=__a;self.__ob=__b;del a1,b1;__a,__b=map(self.__dtip,((__a,__pr),
(__b,__pr)));
def __dtip(self,__apr)->int:
		__a,__pr=__apr
    if (la:=len(__a[1]))<__pr:
    		for _ in range(__pr-la):__a[1]+='0';
    return int(__a[0]+__a[1][:__pr]);
```

Here we convert the transformed number for the given decimal precision.

```python
self.__a=__a;self.__b=__b;self.__pr=__pr;del __a,__b,__pr;self.random=lambda __n,__s=None:self.__frandom(self.__pr,__n,__s);
def __frandom(self,__pr,__n,__s)->list:
		def rint(__a,__b,__pr):
    		(z:=[__a,__b]).sort();__a,__b=z;del z;r=str(randint(__a,__b));
      	if (r1:=len(r)-__pr)>0:
        		return r[:r1]+'.'+r[r1:];
        else:
          	z=''
          	for _ in range(-r1):z+='0';
            return '0.'+z+r
    seed(__s);return [Decimal(rint(self.__a,self.__b,__pr)) for _ in range(__n)];
```

We then store the obtained numbers that are the range extremities for the random number and the precision. Then we define a function "random" to get the desired number of random numbers.

```python
def cgpr(self,__pr)->None:
		try:
    		self.__pr=__pr;del __pr;self.__a,self.__b=map(self.__dtip,((self.__oa,self.__pr),(self.__ob,self.__pr)));print("New precision: "+str(self.__pr));
    except Exception as e:print("Invalid command: rdeciml.cgpr\n",e);
```

I have also added a function "cgpr" to change the precision of the random numbers generated.


#### The function below can be used to generate random integers if required.
```python
def rint(__i:int,__j:int,__n=1,s=None)->int|tuple[int,...]:
    try:
        if s is not None:seed(s);
        if __n==1:return randint(__i,__j);
        return tuple(map(lambda _:randint(__i,__j),range(__n)))
    except Exception as e:print("Invalid command: rint\n",e);
```

Here, ***"__i"*** is the lower limit and ***"__j"*** is the upper limit of the range in which the random integers are to be genrated. ***"__n"*** is the number of random integers and ***"s"*** is the seed.
