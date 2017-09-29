import random
from blackjack.card import Card


class Deck:
    index = 0
    size = 52

    def __init__(self):
        self.cards = self.create_deck()

    def create_deck(self):
        cards = []
        values = ['2', '3', '4', '5', '6', '7', '8',
                  '9', '10', 'J', 'Q', 'K', 'A']
        for value in values:
            for x in range(0, 4):
                cards.append(Card(value))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        card = self.cards[self.index]
        self.index += 1
        if self.index == self.size:
            self.index = 0
        return card
