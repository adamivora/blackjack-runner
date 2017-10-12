import abc
from blackjack.logger import logger
from blackjack.hand import Hand
from blackjack.strategies.bet_strategy import no_strategy


class Player(metaclass=abc.ABCMeta):
    default_bet = 1

    def __init__(self, balance, name=None, strategy=no_strategy):
        self.hand = Hand()
        self.starting_balance = balance
        self.balance = balance
        self.name = name
        self.strategy = strategy
        self.score = 0
        self.dealer_card = None

    def __str__(self):
        if self.name:
            return self.name
        return self.__class__.__name__

    @abc.abstractmethod
    def will_hit(self):
        pass

    def on_card_dealt(self, card, is_dealer):
        if is_dealer:
            self.dealer_card = card
        self.score += self.strategy.get_count(card)

    def on_shuffle(self):
        self.score = 0

    def get_bet(self):
        return self.strategy.get_bet(self.score)

    def has_natural(self):
        return self.hand.get_score() == 21

    def pay(self, player, bet):
        logger.info('[BET] {0} gave {1} chips to {2}.'.format(
            self, bet, player))
        self.balance -= bet
        player.balance += bet

    def reset(self):
        self.hand = Hand()

    def reset_balance(self):
        self.balance = self.starting_balance
