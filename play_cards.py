#!/usr/bin/env python

from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Betty")

print(d1)

print(d1.get_dealer_name())

print(d1.dealer)

d1.dealer = 'Fred'  #

try:
    d1.dealer = 0xDeadBeef
except TypeError as err:
    print(err)
else:
    print(d1.dealer)

d1.shuffle()
print(d1.cards, '\n')


hand = []

for i in range(5):
    hand.append(d1.draw())

for card in hand:
    print(card.rank, card.suit)
print()

print(d1.get_suits())
print(CardDeck.get_suits())

print(len(d1))
print(d1, '\n')

j1 = JokerDeck("Albert")
print(j1)
j1.shuffle()
print(j1.cards)

j1.bark()
print(JokerDeck.mro())
print()

d2 = CardDeck("Sue")

d3 = d1 + d2
print(d3)






