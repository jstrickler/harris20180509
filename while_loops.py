#!/usr/bin/env python

i = 0
while i < 5:
    print(i)
    i += 1
print()

while True:
    color = input("WHAT.....is your favorite color? ")
    if color == 'q':
        break

    if color == '':
        continue

    print("Your color is {}! OK, off you go!".format(color))

