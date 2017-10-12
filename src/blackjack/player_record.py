class PlayerRecord:
    def __init__(self, player):
        self.player = player
        self.reset()

    def has_natural(self):
        return self.player.hand.get_score() == 21

    def is_player_active(self):
        return self.in_game and not self.is_standing

    def reset(self):
        self.is_standing = False
        self.in_game = True
        self.player.reset()
