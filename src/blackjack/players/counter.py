from blackjack.players.player import Player
from blackjack.strategies.hit_strategy import should_hit
from blackjack.strategies.bet_strategy import BetStrategy


class Counter(Player):
    """
    Counter counts cards with pre-defined betting strategy
    and uses optimal hit strategy.
    """

    def __init__(self, strategy=None, balance=100):
        super(Counter, self).__init__(balance, strategy, BetStrategy(strategy))

    def will_hit(self):
        return should_hit(self.hand, self.dealer_card)

    def reset(self):
        super(Counter, self).reset()
        self.dealer_card = None
