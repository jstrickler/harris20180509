#!/usr/bin/env python


def get_message():
    return "Hello, world"

def say_message():
    message = get_message()
    print(message)

say_message()

m = get_message()


def add(x, y):
    return x + y

print(add(10, 5))

print(add(10, 20))


def spam(a, b, *c):
    print(a)
    print(b)
    print(c)
    print()


spam(1, 2)
spam(1, 2, 3, 4)
print()

def ham(*a):
    print(a, '\n')


ham()
ham(1)
ham(1, 2, 3, 4, 5, 6, 7, 8, 9)


def eggs(*,  file_name, user_name):
    print('file_name:', file_name)
    print('user_name:', user_name)
    print()


eggs(file_name='foo.txt', user_name='bob')

# eggs('foo.txt', 'bob')

eggs(user_name='alice', file_name='bar.txt')


def config(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
    print()

config(folder='DATA', user='Paul', location='Melbourne', state='FL')


def wacky(p1, p2, *p3, p4, p5, **p6):
    print("p1:", p1)
    print("p2:", p2)
    print("p3:", p3)
    print("p4:", p4)
    print("p5:", p5)
    print("p6:", p6)
    print("=" * 10)

wacky('a', 1, "eeny", "meeny", "minie", p4="apple", p5=42, animal='wombat', drink='mojito')


def doit(username='root'):
    print("{} is doing the thing".format(username))

doit('bob')
doit('alice')
doit()
