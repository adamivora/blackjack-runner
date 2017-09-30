from blackjack.blackjack import Blackjack
from blackjack.logger import logger


class Runner:
    def __init__(self, players):
        self.players = players
        self.game = Blackjack()

    def run(self, rounds):
        game = self.game
        for i in range(0, rounds):
            logger.info('[GAME] Round {0} start'.format(i))
            for player in self.players:
                logger.info('[PLAYER] Player {0} round start'.format(player))
                game.start_game(player)
