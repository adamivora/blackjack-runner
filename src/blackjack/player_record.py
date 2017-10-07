class PlayerRecord:
    default_bet = 1

    def __init__(self, player):
        self.reset()
        self.player = player
        self.bet = self.default_bet

    def has_natural(self):
        return self.player.hand.get_score() == 21

    def is_player_active(self):
        return self.in_game and not self.is_standing

    def reset(self):
        self.is_standing = False
        self.in_game = True
        self.result = None
