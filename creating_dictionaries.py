#!/usr/bin/env python
from collections import defaultdict

d1 = dict()
d2 = {'a': 5, 'm': 16, 'e': 42}
d3 = {}
d4 = dict(a=5, m=16, e=42)

keys = ['a', 'm', 'e']
values = [5, 16, 42]

d5 = dict(zip(keys, values))
print(d5)

airports = {
    'EWR': 'Newark',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'MLB': 'Melbourne',
    'IAD': 'Dulles',
}

print(airports['MLB'], '\n')

print(airports.get('MLB'))
print(airports.get('MIA'))
print(airports.get('MIA', "NOT FOUND"))
print()


colors = defaultdict(list)

colors['red'] = [25, 15]

print(colors['blue'])

colors['blue'].append(5)
colors['red'].append(20)
colors['blue'].append(35)
print(colors)


things = defaultdict(lambda: 0)

print(things['spam'])
print(things['ham'])

print(airports.setdefault('MIA', 'Miami'))

print(airports, '\n')

more_airports = {'JFK': "Kennedy", "ELM": "Elmira, NY", "HLN": "Helena, MT",
            'MIA': "Miami International"}

airports.update(more_airports)

print(airports, '\n')


for abbr in 'JFK', 'MLB', 'MCO', 'TPA', 'EWR':
    print(abbr, abbr in airports)
print()

for abbr, name in airports.items():
    print(abbr, name)
print()


for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

for abbr, name in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(abbr, name)
print()


