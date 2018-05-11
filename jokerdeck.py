#!/usr/bin/env python

from carddeck import CardDeck, Card

class Dog():
    def bark(self):
        print("Woof! Woof!")

class JokerDeck(CardDeck, Dog):


    def _create_deck(self):
        super()._create_deck()
        self._cards.append(Card("Joker", 1))
        self._cards.append(Card("Joker", 2))


    @property
    def wombat(self):
        return 
    
    @wombat.setter
    def wombat(self, value):
        pass
