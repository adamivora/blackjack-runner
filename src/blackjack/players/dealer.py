from blackjack.players.player import Player


class Dealer(Player):
    """
    Dealer plays against other players.
    Obeying Blackjack rules he has to hit until he has 17 or more.
    Has exactly the same hitting behavior as Hitter(17)
    but different win conditions.
    """

    def __init__(self):
        super(Dealer, self).__init__()

    def will_hit(self):
        return self.hand.score() < 17
