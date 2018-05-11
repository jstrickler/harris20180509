#!/usr/bin/env python
import sys

x = 42,

def print(*args):
#    print(*args)
    __builtins__.print("HA HA HA!!!")

x = 100  # global

y = 'Priscilla'

def ham():
    m = 'mongoose'

    def spam():
    # {
        y = 42   # local
        print("In spam(): x is", x)
        print("In spam(): y is", y)
        print("In spam(): m is", m)
    # }

    spam()

ham()
print("In main(): y is", y)


