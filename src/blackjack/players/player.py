import abc
from blackjack.logger import logger
from blackjack.hand import Hand


class Player(metaclass=abc.ABCMeta):
    def __init__(self):
        self.hand = Hand()
        self.money = 100

    @abc.abstractmethod
    def will_hit(self):
        pass

    def give_money_to(self, player, bet):
        logger.info('[BET] {0} gave {1} chips to {2}.'.format(
            self, bet, player))
        self.money -= bet
        player.money += bet

    def __str__(self):
        return self.__class__.__name__
