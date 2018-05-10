#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

with open('fruitlist.txt', 'w') as fruitlist_out:
    for fruit in fruits:
        fruitlist_out.write(f"{fruit[0]}|{fruit}|{len(fruit)}\n")
