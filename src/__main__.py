import numpy as np
from blackjack.runner import Runner
from blackjack.players.hitter import Hitter
from blackjack.players.professional import Professional
from blackjack.players.counter import Counter
from blackjack.graph import Graph

rounds = 400
graph = Graph('Rounds', 'Balance')

players1 = [
    Hitter(13),
    Hitter(14),
    Hitter(15),
    Hitter(16),
    Hitter(17),
    Hitter(18),
    Hitter(19),
    Hitter(20),
    Hitter(21)
]
players2 = [
    Hitter(17),
    Professional()
]
players3 = [
    Professional(),
    Counter('Hi-Lo'),
    Counter('K-O'),
    Counter('Hi-Opt I'),
    Counter('Hi-Opt II'),
    Counter('Halves'),
    Counter('Omega II'),
    Counter('Zen')
]

players_list = [players1, players2, players3]

for players in players_list:
    runner = Runner(players)
    results = []

    for i in range(50):
        results.append(runner.run(rounds))
        for player in players:
            player.reset_balance()

    x = dict()
    for i, result in enumerate(results):
        for player in result:
            if i == 0:
                x[player] = []
            x[player].append([round_result.balance for round_result
                              in result[player]])
    y = {player: np.mean(player_result, axis=0)
         for player, player_result in x.items()}
    graph.add_graph(y, rounds)

graph.draw()
