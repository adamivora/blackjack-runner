import abc
from blackjack.logger import logger
from blackjack.hand import Hand


class Player(metaclass=abc.ABCMeta):
    def __init__(self, money, name=None):
        self.hand = Hand()
        self.money = money
        self.name = name

    @abc.abstractmethod
    def will_hit(self):
        pass

    def give_money_to(self, player, bet):
        logger.info('[BET] {0} gave {1} chips to {2}.'.format(
            self, bet, player))
        self.money -= bet
        player.money += bet

    def __str__(self):
        if self.name:
            return self.name
        return self.__class__.__name__
