from blackjack.logger import logger
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.card import Card
from blackjack.players.dealer import Dealer


class Blackjack:
    inProgress = False

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Dealer()

    def start_game(self, player):
        self.inProgress = True
        dealer = self.dealer
        logger.info('[START]')
        logger.info('[CARDS] {0}'.format(
            list(card.value for card in self.deck.cards)))
        while self.inProgress:
            if player.will_hit():
                self.hit(player)
                if (player.hand.score() > 21):
                    self.inProgress = False
            else:
                self.stand()
                self.inProgress = False

        while dealer.will_hit():
            self.hit(dealer)

        self.end_game(player)

    def end_game(self, player):
        dealer = self.dealer

        playerScore = player.hand.score()
        dealerScore = dealer.hand.score()

        logger.info('[SCORE] {0}: {1}, {2}: {3}'.format(
            player, playerScore, dealer, dealerScore))

        if playerScore > 21:
            player.give_money_to(dealer, 1)
        elif dealerScore > 21 or dealerScore < playerScore:
            dealer.give_money_to(player, 1)
        else:
            player.give_money_to(dealer, 1)

    def hit(self, player):
        card = self.deck.deal()
        logger.info('[HIT] ({0}) {1}'.format(player, card))
        player.hand.add_card(card)

    def stand(self):
        logger.info('[STAND]')
