import math


def square(x):
    d = x ** 2
    print(locals())
    return d


a = 5
b = square(2)
print(a)
print(math.sqrt(a))
print(b)
print(math.pow(a, 2))
print(globals())


