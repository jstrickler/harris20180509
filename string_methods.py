#!/usr/bin/env python

cave_man = 'Barney Rubble'

print(type(cave_man))
print(isinstance(cave_man, str))

c1 = cave_man.upper()

print(c1)
print(cave_man)

print(cave_man.count('b'))
print(cave_man.lower().count('b'))

a = 'rat'
b = 'fink'

person = a + b
print(person)

print(len(cave_man), len(person), len(a))


class Foo():
    def __len__(self):
        return 42

c = Foo()
print(len(c))



x = 'Clubs Diamonds Hearts Spades'
suits = x.split()
print(suits)

path = '/Users/Bob/projects/Alpha'

print(path.split('/'))

x = 'wombat'

print(x.startswith('w'))
print(x.endswith('w'))
print(x.startswith('t'))
print(x.endswith('t'))

print(len(x))
print(x.__len__())




s = "                 Harris Corporation                 "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")

s = "xyyyxxxyxyxyxyyxxExcellent Eel Endeavorsxyxyxxxxyyyxyxyyx"
print("|" + s.lstrip("xy") + "|")
print("|" + s.rstrip("xy") + "|")
print("|" + s.strip("yx") + "|")

s = "this is a test"

print(s.replace(' ', ''))
print(s.replace(' ', 'X'))

print("|" + 'foo'.center(15) + '|'
      )

















