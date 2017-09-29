class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def score(self):
        score = 0
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
            'K': 10,
            'A': 11
        }
        for card in self.cards:
            score += values.get(card.value, 0)
            if card.value == 'A':
                aces += 1
        while (score > 21 and aces > 0):
            score -= 10
            aces -= 1
        return score
