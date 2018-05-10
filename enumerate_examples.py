#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]

e = enumerate(fruits)

fruits.append('durian')

for i, fruit in e:
    del fruits[i]
    print(i, fruit)

print('after deletion:', fruits)

print(enumerate(fruits))
print(list(enumerate(fruits)))
print()



x = ['a', 'b', 'c']
y = ['x', 'y', 'z']

m = x + y
print(m)

print(x * 10)

print([False] * 25)


print('-' * 60)

print("Python is the BEST! " * 10)
print('-' * 60)

for i in range(10):
    print("Python is the BEST! ")


#  range(STOP)
#  range(START, STOP)
#  range(START, STOP, STEP)


for i in range(5, 101, 5):
    print(i, end=' ')
print('\n')





