import matplotlib.pyplot as plt
import math


class Graph:
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    def __init__(self):
        x = [1, 2, 3, 4]
        y = [[100, 75, 20, 30],
             [1, 2, 3, 4], [5, 6, 7, 8], [100, 65, 44, 12]]
        for i in range(1, 4):
            plt.plot(x, y[i], self.colors[i])

        plt.axis([1, 4, 0, 100])
        plt.xlabel('Rounds')
        plt.ylabel('Money')

    def draw(self):
        plt.show()


graph = Graph()
graph.draw()
