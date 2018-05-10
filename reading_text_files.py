#!/usr/bin/env python
import os
from pprint import pprint

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    print(mary_in)
    print(mary_in.closed)
    all_data = mary_in.read()
    print(repr(all_data))

print(mary_in)
print(mary_in.closed)
print('-' * 60)


with open('DATA/mary.txt') as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print('-' * 60)

with open('empty.txt') as empty_in:
    for line in empty_in:
        print("line:", line)

FILE_NAME = 'empty.txt'

if os.path.exists(FILE_NAME):
    file_size = os.path.getsize(FILE_NAME)
    if file_size > 0:
        with open(FILE_NAME) as empty_in:
            all_contents = empty_in.read()
            print(repr(all_contents))
    else:
        print("EMPTY FILE")

# shutil
# argparse
# fileinput
# glob.glob
# shlex.split
# subprocess.run


with open('DATA/words.txt') as words_in:
    words = [w.rstrip() for w in words_in]

all_knights = []
with open('DATA/knights.txt') as knights_in:
    for line in knights_in:
        fields = line.rstrip().split(':')
        all_knights.append(fields)

pprint(all_knights)

