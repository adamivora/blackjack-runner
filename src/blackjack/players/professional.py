from blackjack.players.player import Player


class Professional(Player):
    """
    Professional uses basic strategy from https://en.wikipedia.org/wiki/Blackjack#Basic_strategy
    """

    def __init__(self, name=None, balance=100):
        super(Professional, self).__init__(balance, name)
        self.dealer_card = None

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

    def on_card_dealt(self, card, is_dealer):
        if is_dealer:
            self.dealer_card = card

    def reset(self):
        super(Professional, self).reset()
        self.dealer_card = None
