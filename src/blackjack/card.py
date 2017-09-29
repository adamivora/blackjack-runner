class Card:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '({0})'.format(self.value)
