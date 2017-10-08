class Card:
    values = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11
    }

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '({0})'.format(self.value)

    def get_numeric_value(self):
        return self.values.get(self.value)
