from blackjack.players.player import Player


class Hitter(Player):
    """
    Hitter will hit until he has scored his desired maximum score or higher.
    """

    def __init__(self, maxScore, balance=100):
        super(Hitter, self).__init__(balance, 'Hitter{0}'.format(maxScore))
        self.maxScore = maxScore

    def will_hit(self):
        return self.hand.get_score() < self.maxScore
