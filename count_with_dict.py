#!/usr/bin/env python


counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for line in breakfast_in:
        item = line.rstrip()
        counts[item] = counts.get(item, 0) + 1

        # if item in counts:
        #     counts[item] += 1
        # else:
        #     counts[item] = 1

print(counts)
