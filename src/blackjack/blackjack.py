from blackjack.logger import logger
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.card import Card
from blackjack.players.dealer import Dealer
from blackjack.game_record import GameRecord


class Blackjack:
    inProgress = False

    def __init__(self, players):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Dealer()
        self.players = players
        self.player_records = {player: GameRecord() for player in players}

    def start_round(self):
        self.inProgress = True
        logger.info('[START]')
        logger.info('[CARDS] {0}'.format(
            list(card.value for card in self.deck.cards)))

        self.deal_starting_hands()
        self.pay_out_naturals()
        self.run_main_loop()

    def get_active_players(self):
        return [record.player for record in self.player_records
                if record.is_player_active()]

    def get_standing_players(self):
        return [record.player for record in self.player_records
                if record.standing]

    def set_player_finished(self, player):
        self.player_records[player].in_game = False

    def pay_out_naturals(self):
        dealer = self.dealer
        players = self.players

        players_with_naturals = filter(lambda e: e.has_natural(), players)

        if dealer.has_natural():
            for player in players:
                if player not in players_with_naturals:
                    self.end_player_turn(player)
        else:
            for player in players_with_naturals:
                self.end_player_turn(player, True)

    def run_main_loop(self):
        while len(self.get_active_players()) > 0:
            for player in players:
                if player.will_hit():
                    self.deal_card(player)
                    if player.hand.get_score() > 21:
                        self.end_player_turn(player, 'L')
                else:
                    self.player_records[player].standing = True
        dealer_score = self.dealer.get_score()

        for player in self.get_standing_players():
            player_score = player.hand.get_score()
            if player_score == dealer_score:
                result = 'D'
            elif player_score > dealer_score:
                result = 'W'
            else:
                result = 'L'
            self.end_player_turn(player, result)

    def end_player_turn(self,
                        player: Player, result: str, natural: bool=False):
        """
        End turn with provided result and split bets accordingly.

        Arguments:
        player  -- Currently playing
        result  -- ['W', 'L', 'D'] for win, loss or draw
        natural -- Indicates if the player has natural 21
        """

        bet = self.player_records[player]
        if result == 'W':
            if natural:
                bet = int(bet * 1.5)
            self.dealer.pay(player, bet)
        elif result == 'L':
            player.pay(self.dealer, bet)

        self.set_player_finished(player)

    def deal_starting_hands(self):
        for i in range(0, 2):
            for player in self.players + self.dealer:
                self.deal_card(player)

    def notify_players(self, card):
        for player in players:
            player.on_card_shown(card)

    def deal_card(self, player, face_up=True):
        card = self.deck.deal()
        logger.info('[HIT] ({0}) {1}'.format(player, card))
        player.hand.add_card(card)
        if face_up:
            self.notify_players(card)

    def stand(self):
        logger.info('[STAND]')
