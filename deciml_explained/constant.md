## Constants

The two commonly used constants are "pi" and "e".

```python
_Pi='3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
_EulersNumber='2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274';
```

The file contains the global string variables ***"_Pi"*** and ***"_EulersNumber"***. They are values till 100 decimal places. As I thought it is sufficiently long.

```python
class constant:
    @staticmethod
    def e(pr=getpr())->Decimal|None:
        try:
            if pr>100:raise Exception;
            global _EulersNumber;return Decimal(_EulersNumber[:pr+2]);
        except:print("Invalid argument: pr -> < 100");
    @staticmethod
    def pi(pr=getpr())->Decimal|None:
        try:
            if pr>100:raise Exception;
            global _Pi;return Decimal(_Pi[:pr+2]);
        except:print("Invalid argument: pr -> < 100");
```

The class **"constant"** contains two static methods, namely, ***"e"*** and ***"pi"***. @staticmethod decorator is used to signify that the method does not depend on any other methods in the class. @classmethod is used otherwise.

The function "e" takes the precision ***"pr"*** as an argument and returns the object ***"Decimal"*** for the value if the precision is not greater than 100 (As that is the maximum precision that we decided). Execptions are handled otherwise.

The function "pi" works similarly using the "_Pi" string.

As you can see we select the string up to "pr+2" because we need to count the non decimal part also.
