from blackjack.blackjack import Blackjack
from blackjack.logger import logger


class Runner:
    def __init__(self, players):
        self.players = players
        self.game = Blackjack(players)
        self.rounds = []

    def run(self, rounds):
        game = self.game
        for i in range(0, rounds):
            logger.info('[GAME] Round {0} start'.format(i))
            results = game.start_round()
            logger.info('[GAME] Round {0} end'.format(i))
