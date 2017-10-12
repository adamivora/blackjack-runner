from blackjack.players.player import Player


class Counter(Player):
    """
    Counter counts cards.
    """

    def __init__(self, balance=100, name=None):
        super(Counter, self).__init__(balance, name)
        self.score = 0
        self.dealer_card = None

    def on_card_dealt(self, card, is_dealer):
        if is_dealer:
            self.dealer_card = card
        value = card.get_numeric_value()

        if value <= 6:
            self.score += 1
        elif value >= 10:
            self.score -= 1

    def on_shuffle(self):
        self.score = 0

    def will_hit(self):
        score = self.hand.get_score()
        dc = self.dealer_card.get_numeric_value()
        aces = self.hand.aces

        if aces == 0:
            if score >= 17:
                return False
            if score >= 13:
                return dc not in range(2, 7)
            if score == 12:
                return dc not in range(4, 7)
        else:
            if score >= 19:
                return False
            if score == 18:
                return dc not in range(2, 9)
        return True

    def reset(self):
        super(Counter, self).reset()
        self.dealer_card = None

    def get_bet(self):
        if self.score > 6:
            return 6
        if self.score > 0:
            return self.score
        return 0
