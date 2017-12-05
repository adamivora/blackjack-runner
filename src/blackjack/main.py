import numpy as np
from blackjack.runner import Runner
from blackjack.players.hitter import Hitter
from blackjack.players.professional import Professional
from blackjack.players.counter import Counter
from blackjack.graph import Graph


class Main:
    hitters = [Hitter(13), Hitter(14), Hitter(15), Hitter(16), Hitter(17),
               Hitter(18), Hitter(19), Hitter(20), Hitter(21)]
    hitter_and_professional = [Professional(), Hitter(16)]
    betting_strategies = [
        Professional(), Counter('Hi-Lo'), Counter('K-O'), Counter('Hi-Opt I'),
        Counter('Hi-Opt II'), Counter('Halves'), Counter('Omega II'),
        Counter('Zen')]
    all_players = hitters + betting_strategies

    def __init__(self, rounds=200, iterations=50):
        self.rounds = rounds
        self.iterations = iterations

    def run(self, players):
        results, balances = self.get_results(players)
        self.print_balances(balances)
        self.show_graph(results)

    def print_balances(self, balances):
        for player, balance in balances.items():
            # 100 is always the starting balance
            win_rate_percent = (1 - ((100 - balance) / self.rounds)) * 100
            print('{}: {:.2f}'.format(player, win_rate_percent))

    def show_graph(self, graph_results):
        graph = Graph('Rounds', 'Balance')
        graph.add_graph(graph_results, self.rounds)
        graph.draw()

    def get_results(self, players):
        runner = Runner(players)
        results = []
        balances = {}
        mean_balances = {}

        for player in players:
            mean_balances[player] = 0

        for i in range(self.iterations):
            results.append(runner.run(self.rounds))
            for player in players:
                mean_balances[player] += player.balance
                player.reset_balance()

        # Get mean from total balance sum
        for player in players:
            mean_balances[player] /= self.iterations

        for i, result in enumerate(results):
            for player in result:
                if i == 0:
                    balances[player] = []
                balances[player].append([round_result.balance for round_result
                                         in result[player]])
        graph_results = {player: np.mean(player_result, axis=0)
                         for player, player_result in balances.items()}

        return graph_results, mean_balances
