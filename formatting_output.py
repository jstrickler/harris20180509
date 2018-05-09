#!/usr/bin/env python

result = 123.234 / 18.2930923

print("result is", result)
print("result is {:.3f}".format(result))
print(f"result is {result:.3f}")

cave_man = "Barney Rubble"
city = 'Bedrock'

print(cave_man, "lives in", city)
print("{0} lives in {1}".format(cave_man, city))
print("{1} lives in {0}".format(cave_man, city))
print(f"{cave_man} lives in {city}")


x = 57005

print("{:x}".format(x))
print("{:X}".format(x))
print("{:8X}".format(x))
print("{:08X}".format(x))
print()

print("{:o}".format(x))
print("{:8o}".format(x))
print("{:08o}".format(x))

print()

print("{:b}".format(x))
print("{:24b}".format(x))
print(f"{x:024b}")


print(hex(x), oct(x), bin(x))

print(int(hex(x), 16))

print(f"{2 + 2} {5 * 2.33}")
