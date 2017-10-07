from blackjack.runner import Runner
from blackjack.players.hitter import Hitter

players1 = [Hitter(15, "Hitter15"), Hitter(
    16, "Hitter16"), Hitter(21, "Hitter21")]

runner = Runner(players1)
runner.run(1)
