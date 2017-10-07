from blackjack.blackjack import Blackjack
from blackjack.logger import logger


class Runner:
    def __init__(self, players):
        self.players = players
        self.game = Blackjack()
        self.rounds = []

    def run(self, rounds):
        game = self.game
        for i in range(0, rounds):
            logger.info('[GAME] Round {0} start'.format(i))
            game.start_round(self.players)
            logger.info('[GAME] Round {0} end'.format(i))


class RoundResult:
    def __init__(self, bet, dealerMoney, playerMoney, winner):
        self.bet = bet
        self.dealerMoney = dealerMoney
        self.playerMoney = playerMoney
        self.winner = winner
