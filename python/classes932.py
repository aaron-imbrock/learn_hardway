class MyClass:
    """A simple example class"""

    def __init__(self):
        self.data = []

    i = 12345

    def f(self):
        return 'hello world'

    def add_data(self, dt):
        self.data.append(dt)
        print(f'self.data is now {self.data}')


my_class = MyClass()

print(my_class.i)
f = my_class.f()
print(f)

my_class.add_data('hi')


class Complex(object):
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r)
print(x.i)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2

print(x.counter)
del x.counter
