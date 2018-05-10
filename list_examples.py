#!/usr/bin/env python

list1 = list()

things = [1, 'apple', None, 12.34, ['another', 'list'], ('a', 'b', 'c')]

list2 = []

colors = 'blue purple mauve red green'.split()
print(colors)

fruits = ['apple', 'mango', 'banana', 'kumquat']

fruits.append('pomegranate')
print(fruits)


fruits.insert(0, 'papaya')
fruits.insert(3, 'peach')
print(fruits)

fruits.insert(99, 'guava')
print(fruits)

# print(fruits[88])

more_fruits = ['lime', 'pineapple', 'lemon']

fruits.extend(more_fruits)

print(fruits)

fruits.append(more_fruits)
print(fruits)

#  L.append(obj)   L.insert(pos, obj)  L.extend(ITERABLE)


print(fruits[11][1])
print(fruits[-1][1])
print(fruits[len(fruits)-1][1])
print(fruits[-3])
print(fruits[-1][-2])

print(fruits[-1][-2])

fruits.insert(-3, 'papaya')

print(fruits)
print(fruits[-3])

fruits.insert(-99, 'tamarind')
print(fruits)


fruits.insert(2, 'persimmon')
print(fruits[2])


del fruits[-1]

print(fruits)

fruits.remove('pomegranate')
print(fruits)

# fruits.remove('tomato')   naughty!!

x = fruits.pop()
print(x)
print(fruits)

y = fruits.pop(0)
print(y)
print(fruits)



