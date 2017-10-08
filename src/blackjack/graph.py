import matplotlib.pyplot as plt


class Graph:
    # Colors taken from https://sashat.me/2017/01/11/list-of-20-simple-distinct-colors/
    colors = ['#e6194b', '#3cb44b', '#ffe119', '#0082c8', '#f58231',
              '#911eb4', '#46f0f0', '#f032e6', '#d2f53c', '#008080',
              '#e6beff', '#aa6e28', '#fffac8', '#800000', '#aaffc3',
              '#808000', '#ffd8b1', '#000080', '#808080', '#000000']
    count = 1

    def __init__(self, x_label='X', y_label='Y'):
        self.x_label = x_label
        self.y_label = y_label

    def add_graph(self, data, x_max):
        i = 0
        plt.figure(self.count)
        self.count += 1
        for name, balances in data.items():
            plt.plot(range(1, x_max + 1), balances, self.colors[i], label=name)
            i += 1

        plt.axis([1, x_max, 0, 200])
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.legend()

    def draw(self):
        plt.show()
