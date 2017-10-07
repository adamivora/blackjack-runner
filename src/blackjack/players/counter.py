from blackjack.players.player import Player


class Counter(Player):
    def __init__(self, maxScore, money=100):
        super(Counter, self).__init__(money)
        self.maxScore = maxScore

    def will_hit(self):
        return self.hand.get_score() < self.maxScore
