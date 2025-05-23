## Precision

In the python standard library called Decimal the convention of using the whole length (sum of integer and float) is incomplete. It can be made better by using the precision convention of counting the decimal values only. This motivated me to understand the topic and write my own extension for the library. I called it deciml(.py). As I was starting to learn machine learning at the time and thought it as a suitable choice.

```python
__DecimalPrecision=16
getcontext().rounding=ROUND_HALF_UP
```

Here I define a global variable ***"__DecimalPrecision"*** (with a default value of 16). I use the ***"getcontext"*** function from the decimal library to round using the rounding rule ***"ROUND_HALF_UP"*** (as I thought it was suitable). 

```python
def setpr(__p:int)->None:global __DecimalPrecision;__DecimalPrecision=__p;
def getpr()->int:return __DecimalPrecision;
```

Then I define two functions ***"setpr"*** and ***"getpr"***.
The function "setpr" takes ***"__p"*** as an argument, which is an integer and changes the global "__DecimalPrecision" to the value.
The function "getpr" returns the global "__DecimalPrecision" value.

