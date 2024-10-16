import math


def square(x):
    d = x ** 2
    def even(x):
        nonlocal d
        d = x * 2
        if d % 2 == 0:
            print('Четное')
        else:
            print('Нечетное')
    even(x)
    print(locals())
    return d


a = 5
b = square(7)
print(a)
print(math.sqrt(a))
print(b)
print(math.pow(a, 2))
print(globals())


