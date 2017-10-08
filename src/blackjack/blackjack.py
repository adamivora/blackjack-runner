from blackjack.logger import logger
from blackjack.deck import Deck
from blackjack.players.dealer import Dealer
from blackjack.player_record import PlayerRecord
from blackjack.result import Result


class Blackjack:
    def __init__(self, players):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Dealer()
        self.players = players
        self.player_records = {player: PlayerRecord(
            player) for player in players}

    def start_round(self):
        logger.info('[START]')
        logger.info('[CARDS] {0}'.format(
            list(card.value for card in self.deck.cards)))

        self.deal_starting_hands()
        self.pay_out_naturals()
        self.run_main_loop()
        results = self.generate_round_results()
        self.reset_records()
        return results

    def deal_starting_hands(self):
        for i in range(2):
            for player in self.players + [self.dealer]:
                self.deal_card(player)

    def pay_out_naturals(self):
        dealer = self.dealer
        players = self.players
        players_with_naturals = [
            player for player in players if player.has_natural()]

        if dealer.has_natural():
            for player in players:
                if player not in players_with_naturals:
                    self.end_player_turn(player, 'L')
                else:
                    self.end_player_turn(player, 'D')
        else:
            for player in players_with_naturals:
                self.end_player_turn(player, 'W', True)

    def run_main_loop(self):
        active_players = self.get_active_players()
        dealer = self.dealer
        while len(active_players) > 0:
            for player in active_players:
                if player.will_hit():
                    self.deal_card(player)
                    if player.hand.get_score() > 21:
                        self.end_player_turn(player, 'L')
                else:
                    self.stand(player)
            active_players = self.get_active_players()
            logger.info('[ROUND] {0} active players left'.format(
                len(active_players)))

        while dealer.will_hit():
            self.deal_card(dealer)
        dealer_score = dealer.hand.get_score()

        for player in self.get_standing_players():
            player_score = player.hand.get_score()
            if dealer_score > 21:
                result = 'W'
            else:
                if player_score == dealer_score:
                    result = 'D'
                elif player_score > dealer_score:
                    result = 'W'
                else:
                    result = 'L'
            self.end_player_turn(player, result)

    def generate_round_results(self):
        results = []
        for player in self.players:
            record = self.player_records[player]
            player_score = player.hand.get_score()
            dealer_score = self.dealer.hand.get_score()
            bet = record.bet
            balance = player.balance
            result = record.result
            results.append(Result(
                player, player_score, dealer_score, bet, balance, result))
        return results

    def reset_records(self):
        for player in self.players:
            self.player_records[player].reset()
        self.dealer.reset()

    def get_active_players(self):
        return [player for player in self.players
                if self.player_records[player].is_player_active()]

    def get_standing_players(self):
        return [player for player in self.players
                if self.player_records[player].is_standing]

    def set_player_finished(self, player, result):
        record = self.player_records[player]
        record.in_game = False
        record.result = result

    def end_player_turn(self, player, result, natural=False):
        """
        End turn with provided result and split bets accordingly.

        Arguments:
        player  -- Currently playing
        result  -- ['W', 'L', 'D'] for win, loss or draw
        natural -- Indicates if the player has a natural 21
        """
        logger.info('[RESULT] {0}: {1}'.format(player, result))
        bet = self.player_records[player].bet
        if result == 'W':
            if natural:
                bet = bet * 1.5
            self.dealer.pay(player, bet)
        elif result == 'L':
            player.pay(self.dealer, bet)

        self.set_player_finished(player, result)

    def notify_players(self, card, is_dealer):
        for player in self.players:
            player.on_card_dealt(card, is_dealer)

    def deal_card(self, player, face_up=True):
        card = self.deck.deal()
        logger.info('[HIT] ({0}) {1}'.format(player, card))
        player.hand.add_card(card)
        if face_up:
            self.notify_players(card, player == self.dealer)

    def stand(self, player):
        self.player_records[player].is_standing = True
        logger.info('[STAND] ({0})'.format(player))
