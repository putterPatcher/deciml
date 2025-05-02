## deciml - Get the Decimal value

```python
def deciml(__a:float|int|str|Decimal,__pr=getpr())->Decimal:
```

The function returns the Decimal object for the given number ***"__a"***, with a precision of ***"__pr"***.

```python
def __exp(__a:str)->list:
		match len(a:=__a.split('e')):
    		case 1:
    				match len(a:=__a.split('E')):
      					case 1:return a+['0',];
        		  	case 2:return a if a[0]!='' else ['1',a[1]];
        				case _:return None;
    		case 2:return a if a[0]!='' else ['1',a[1]];
    		case _:return None;
```

This function splits the string into a list with an non exponential part and an exponential part.

```python
try:
	if (sa:=str(__a))=='NaN' or sa=='Inf' or sa=='-Inf':return __a;
    __a=str(__a)
    if __a[0]=='-':a0=__a[0];__a=__a[1:];
        else:a0='';
        if (a1:=__exp(__a)) is None:raise Exception;
        if len(a2:=a1[0].split('.'))==1:a2+=['0',];
        # for positive exponential
        if (ia1:=int(a1[1])) > 0:
            if (la2:=len(a2[1])) > 0:
                i = la2 - 1
                while a2[1][i] == '0':
                    i-=1
                a2[1] = a2[1][:i+1]
                la2 = len(a2[1])
                a2[0]=a2[0]+a2[1][:ia1 if (dd:=la2 - ia1) > 0 else la2]
                if dd < 0:
                    s = ''
                    for i in range(-dd):
                        s+='0'
                a2[0]=a2[0]+('' if dd > 0 else s);a2[1]='0' if dd <= 0 else a2[1][ia1:];a1[1]='0';
        if Decimal(a1[0])==0:return Decimal('0.0');
        if int(a2[0])==0:
            if a2[1][0]=='0':
                c=1
                for i in a2[1][1:]:
                    if i=='0':c+=1;
                    else:break;
                a2[0]=a2[1][c];a2[1]=a2[1][c+1:];a1[1]=str(int(a1[1])-c-1);
        if __pr > 0:
            if len(a2[1]) > 1:
                if len(a2[1])>__pr:
                    a2[1]=a2[1][:__pr+1];del __pr,__a;
                    if int(a2[1][-1])>=5:
                        a2[1]=a2[1][:-2]+str(int(a2[1][-2])+1);
                    else:a2[1]=a2[1][:-1];
        else:
            if len(a2[1]) > 0:
                a2[1]=a2[1][0];del __pr,__a;
                if int(a2[1][0])>=5:
                    a2[0]=a2[0][:-2]+str(int(a2[0][-2:])+1);
                a2[1]='0';
        return Decimal(a0+a2[0]+'.'+a2[1]+'E'+a1[1]);
    except:return Decimal('NaN');
```

The we separate the negative sign if the number is negative. Then we split the non exponential part. If the exponential is greater than zero, we convert the decimal value such that the exponential is not used (This is done to prevent the Decimal from converting the value which leads to different precision if not done as the precision is the number of digits after the decimal point). We return 0 if the non exponential part is equal to zero. After that we count the number of zeros for the decimal part of the non exponential part if the decimal part has leading zeros. Then we update the list containing the non exponential part such that the integer part has only one value. Then we update the exponential part. After that we round the decimal part of the non exponential part to have a value that has an length equal to the precision. In the end we return the decimal value of the number that was represented in lists.
