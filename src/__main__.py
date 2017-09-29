from blackjack.blackjack import Blackjack
from blackjack.players.hitter import Hitter

blackjack = Blackjack()
player = Hitter(10)

blackjack.start_game(player)
