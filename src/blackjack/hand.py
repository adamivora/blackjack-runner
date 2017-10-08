class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.aces = 0
        self.is_latest_score = True

    def add_card(self, card):
        self.cards.append(card)
        self.is_latest_score = False

    def get_score(self):
        if self.is_latest_score:
            return self.score

        score = 0
        aces = 0

        for card in self.cards:
            score += card.get_numeric_value()
            if card.value == 'A':
                aces += 1
        self.aces = aces

        while (score > 21 and aces > 0):
            score -= 10
            aces -= 1
        self.score = score
        self.is_latest_score = True
        return score
