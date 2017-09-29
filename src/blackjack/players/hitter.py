from blackjack.players.player import Player


class Hitter(Player):
    """
    Hitter will hit until he has scored his desired maximum score or higher.
    """

    def __init__(self, maxScore):
        super(Hitter, self).__init__()
        self.maxScore = maxScore

    def will_hit(self):
        return self.hand.score() < self.maxScore
