from deck import Deck
from hand import Hand
from card import Card
import logger


class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand()

    def start_game(self):
        self.deck.shuffle()
        print(list(card.value for card in self.deck.cards))

    def hit(self):
        hand = self.hand
        card = self.deck.deal()
        hand.hit(card)

    def stand(self):
        print("Score: ", self.hand.score())


hand = Hand()
