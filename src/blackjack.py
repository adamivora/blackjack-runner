from deck import Deck

class Blackjack:
    """Main class for the game"""
    def start_game(self):
        deck = Deck()
        deck.shuffle()
        print(list(card.value for card in deck.cards))

    def hit(self):
        pass

    def stand(self):
        pass

Blackjack().start_game()

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def hit(self, card):
        self.cards.append(card)

    def stand(self):
        pass

    def score(self):
        aces = 0
        values = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 10,
            'Q': 10,
            'K': 10
        }
        for card in self.cards:
            value = values.get(card.value, 0)
            if value == 'A':
                aces += 1
        