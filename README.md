### A program for calculating the cyclomatic complexity of a Python file ###


# Install packages 

```
pip3 install -r requirements.txt
```

# Run example

```
>> python example.py


"""
Total: 10
--------------  --
Bird.get_speed  10
example.py       0
--------------  --
"""
```


# Usage

```
from cyclo.calculate import calculate

calculate("birds.py")
```