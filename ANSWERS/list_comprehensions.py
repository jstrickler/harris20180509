#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print(f0, '\n')

f1 =[f.upper() for f in fruits]
print(f1, '\n')

# new_list = [EXPR for VAR ... in ITERABLE if COND ...]

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print(f3, '\n')

nums = [800,80,1000,32,255,400,5,5000]

bignums = [n for n in nums if n > 300]
print(bignums, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

last_names = [p[1] for p in people]
print(last_names, '\n')

x = [p[:2] for p in people]
print(x, '\n')

x = [(i, i**2, i**3) for i in range(10)]
print(x)


g1 =(f.upper() for f in fruits)
print(g1, '\n')


last_names_gen = (p[1] for p in people)

for last_name in last_names_gen:
    print(last_name)
print()


values = ['a', 'b', 'c', 'd', 'e', 'f']

i = len(values) - 1
for v in reversed(values):
    print(i, v, values)
    values.insert(0, 'x')
    i -= 1
print()

