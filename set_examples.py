#!/usr/bin/env python

set1 = {'schnauzer', 'labrador', 'dachshund', 'sharpei', 'weimaraner'}
set2 = {'labrador', 'sharpei', 'weimaraner', 'corgi', 'husky'}

for i in range(1000):
    set1.add('sharpei')

print(set1)
print(set2)

print("both:", set1 & set2)
print("either:", set1 | set2)
print("just one:", set1 ^ set2)
print("just set 1:", set1 - set2)
print("just set 2:", set2 - set1)

