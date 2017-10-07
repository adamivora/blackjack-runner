class GameRecord:
    default_bet = 1

    def __init__(self, player):
        self.is_standing = False
        self.in_game = True
        self.player = player
        self.bet = self.default_bet

    def is_player_active(self):
        return self.in_game and not self.is_standing
