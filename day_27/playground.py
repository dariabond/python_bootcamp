def sum(*args):
    sum = 0
    for arg in args:
        sum += int(arg)
    return sum


def calculate(n, **kw):
    print(kw)
    n += kw["add"]
    n *= kw["multiply"]
    return n


class Car:
    def __init__(self, **kw):
        # in case nothing is passed - assigned to NaN
        # use kw.get for the optional parameters
        self.make = kw.get('make')
        self.model = kw.get('model')

print(sum(1, 2, 3))
print(calculate(2, add=3, multiply=4))

my_car = Car(make="Ford")
print(my_car.model)
