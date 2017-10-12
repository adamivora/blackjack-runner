from blackjack.players.player import Player
from blackjack.strategies.hit_strategy import should_hit


class Professional(Player):
    def __init__(self, name=None, balance=100):
        super(Professional, self).__init__(balance, name)
        self.dealer_card = None

    def will_hit(self):
        return should_hit(self.hand, self.dealer_card)

    def reset(self):
        super(Professional, self).reset()
        self.dealer_card = None
