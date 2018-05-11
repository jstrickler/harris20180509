#!/usr/bin/env python
from pprint import pprint

FILE_NAME = 'DATA/knights.txt'

def main():
    data = read_info(FILE_NAME)

    pretty_print_knights(data)
    print()

    print_names_and_titles(data)
    print()

    print_field(data, 'Robin', 2)


def read_info(filename):
    knights = {}

    with open(filename) as knights_in:
        for line in knights_in:
            name, title, color, quest, comment = line.rstrip().split(':')
            knights[name] = title, color, quest, comment

    return knights


def pretty_print_knights(info):
    pprint(info)
    print()

def print_names_and_titles(info):
    for knight_name, knight_data in info.items():
        print(knight_data[0], knight_name)
    print()

def print_field(info, knight, field_number):
    print(info[knight][field_number])


main()
