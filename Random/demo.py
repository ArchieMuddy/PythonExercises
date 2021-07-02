from calc import *

a = 4
b = 8

print(add(a,b))
print(sub(a,b))
print(mul(a,b))

def checknumerator(func):
    def innerfunc(a,b):
        if(b>a):
            a,b = b,a
        return func(a,b)
    return innerfunc

div = checknumerator(div)
print(div(a,b))
print(__name__)