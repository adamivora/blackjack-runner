from blackjack.blackjack import Blackjack
from blackjack.logger import logger


class Runner:
    def __init__(self, players):
        self.players = players
        self.game = Blackjack(players)

    def run(self, rounds):
        game = self.game
        player_results = dict()
        for i in range(rounds):
            logger.info('[GAME] Round {0} start'.format(i))
            results = game.start_round()
            if i == 0:
                for player_result in results:
                    player_results[player_result.player] = [player_result]
            else:
                for player_result in results:
                    player_results[player_result.player].append(player_result)
            logger.info('[GAME] Round {0} end'.format(i))
        return player_results
