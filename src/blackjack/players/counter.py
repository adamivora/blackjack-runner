from blackjack.players.player import Player


class Counter(Player):
    """
    Counter counts cards.
    """

    def __init__(self, balance=100, name=None):
        super(Counter, self).__init__(balance, name)

    def will_hit(self):
        return False

    def on_card_dealt(self, card, is_dealer):
        if is_dealer:
            self.dealer_card = card
