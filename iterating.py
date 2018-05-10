#!/usr/bin/env python
from functools import reduce

nums = [800,80,1000,32,255,400,5,5000]

for num in nums:
    print(num)
print()

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

for fruit in fruits:
    print(fruit.upper())
print()

print('-' * 60)

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux', 'git'),
]

for first_name, last_name, *product in people:
    print(first_name, last_name, product)


values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z, '\n')

x, *y, z = values
print(x, y, z, '\n')

*x, y, z = values
print(x, y, z, '\n')


print('-' * 60)

for _, _, *product in people:
    print(product)

print('-' * 60)

for p in people:
    print(p)


# print(max(len(x) for x in people))
# print([len(x) for x in people])


print(values)

values[3] = 'm'
print(values)

values[3:6] = ['q', 'r', 's']
print(values)


print(len(values))
print(max(values), min(values))
print(sum(nums))

print(sorted(nums))
print(sorted(people))

print(reversed(values))

for v in reversed(values):
    print(v)
print()


nums += [8, 50, 42, 98]

print(values)
print(nums)
print()

z = zip(values, nums)

print(list(z))
print('-' * 60)


fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]


def natacha(element):
    return len(element), element.lower()



fruits_by_len = sorted(fruits, key=natacha)

print(fruits_by_len)
print('-' * 60)

for f in fruits:
    print(natacha(f))















