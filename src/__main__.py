from blackjack.runner import Runner
from blackjack.players.hitter import Hitter
from blackjack.players.professional import Professional
from blackjack.graph import Graph

rounds = 400
graph = Graph('Rounds', 'Balance')

players1 = [
    Hitter(13, "Hitter13"),
    Hitter(14, "Hitter14"),
    Hitter(15, "Hitter15"),
    Hitter(16, "Hitter16"),
    Hitter(17, "Hitter17"),
    Hitter(18, "Hitter18"),
    Hitter(19, "Hitter19"),
    Hitter(20, "Hitter20"),
    Hitter(21, "Hitter21")
]
players2 = [
    Hitter(17, "Hitter17"),
    Professional()
]

players_list = [players1, players2]

for players in players_list:
    runner = Runner(players)
    results = runner.run(rounds)
    x = dict()
    for player in results:
        x[player] = [round_result.balance for round_result in results[player]]

    graph.add_graph(x, rounds)
    for player in players1:
        player.reset_balance()

graph.draw()
