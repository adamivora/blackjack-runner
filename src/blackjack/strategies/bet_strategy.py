class BetStrategy:
    """
    Strategies from https://www.blackjackapprenticeship.com/resources/card-counting-systems/
    Score in arrays is ordered from 2 to A (2 3 4 5 6 7 8 9 10/J/Q/K A)
    """
    strategies = {
        None: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'Hi-Lo': [1, 1, 1, 1, 1, 0, 0, 0, -1, -1],
        'K-O': [1, 1, 1, 1, 1, 1, 0, 0, -1, -1],
        'Hi-Opt I': [0, 1, 1, 1, 1, 0, 0, 0, -1, 0],
        'Hi-Opt II': [1, 1, 2, 2, 1, 1, 0, 0, -2, 0],
        'Halves': [0.5, 1, 1, 1.5, 1, 0.5, 0, -0.5, -1, -1],
        'Omega II': [1, 1, 2, 2, 2, 1, 0, -1, -2, 0],
        'Zen': [1, 1, 2, 2, 2, 1, 0, 0, -2, -1]
    }

    def __init__(self, strategy_name=None, min_bet=0):
        self.strategy = self.strategies[strategy_name]
        self.name = strategy_name
        self.min_bet = min_bet

    def __str__(self):
        return self.name

    def get_count(self, card):
        value = card.get_numeric_value()
        count = self.strategy[value - 2]
        return count

    def get_bet(self, score):
        if score > 6:
            return 6
        if score > 0:
            return score
        return self.min_bet


no_strategy = BetStrategy(min_bet=1)
