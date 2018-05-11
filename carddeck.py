#!/usr/bin/env python
import random
from collections import namedtuple

Card = namedtuple("Card", "rank suit")

class CardDeck():   # object
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):   # self == this
        self._cards = None
        self.dealer = dealer
        self._create_deck()

    def _create_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards


    # getter
    def get_dealer_name(self):
        return self._dealer


    @property
    def dealer(self):
        return self._dealer

    #  dealer = property(dealer)


    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")


    def shuffle(this):
        random.shuffle(this._cards)


    def draw(self):
        return self._cards.pop(0)


    @classmethod
    def get_suits(cls):
        print("get suits")
        print(cls)
        print(repr(cls))
        print(type(cls))
        return cls.SUITS

    def __len__(self):
        return len(self._cards)


    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}-{self.dealer}/{len(self)}"


    def __add__(self, other):
        tmp = CardDeck(self.dealer)
        tmp._cards = self.cards + other.cards
        return tmp
