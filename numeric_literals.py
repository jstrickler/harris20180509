#!/usr/bin/env python

i1 = 1000
i2 = 0b1000
i3 = 0x1000
i4 = 0o1000

f1 = 1.234
f2 = 1.
f3 = .234
f4 = 1.23456e27

i = 25
j = 8


print(i + j)
print(i - j)
print(i * j)
print(i / j)
print(i // j)
print(i ** j)
print(i % j)


print(-i // j)

i = 5
i += 15   #  i = i + 15
i *= 5
i /= 10
print("i is", i)

#  i++

import math


x = 1.000000000000000000000001
y = 1.0000000000000000000000011

print(math.isclose(x, y))

x = '123'
y = 456


print(int(x) + y)
print(x + str(y))

n = 'DeadBeef'

print(int(n, 16))


b = '10010100101001'
print(int(b, 2))

x = '12.34566e99'

print(float(x))

x = 2.3920930293
y = 1.2930239
print(x/y)


x = [1, 2, 3]
y = [1, 2, 3]


print(id(x), id(y))

print(x == y)
print(x is y)   #  id(x) == id(y)

class Foo():
    def __add__(self, other):
        return 42

    def __eq__(self, other):
        return True


f1 = Foo()    #    Java: Foo f1 = new Foo()
f2 = Foo()
print(f1 + f2)
print(f1 == f2)
f3 = f1

print(f1 == f3)



