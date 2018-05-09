#!/usr/bin/env python

print()

x = 5
y = 10
z = 25

print(x, y, z)
print("OK")

print(x, y, z, sep="/")
print(x, y, z, sep="\n\n")
print(x, end=" WOMBAT ")
print(y, end=" KOALA ")
print(z)
print(x, y, z, sep='', end='')
print("WOW")

print(x, y, z, sep=' ', end='\n')  # DEFAULT VALUES
print(x, y, z)

things = ['wombats', 'are', 'cuddly']

t = ' '.join(things)
print(t)

x = 'wombats'
y = 'purr'

print(x + ' ' + y)

print(1, 2, 3)


#  req positional  opt positional   req named opt named

