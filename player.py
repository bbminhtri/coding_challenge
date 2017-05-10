class Player(object):
    def __init__(self, symbol, name):
        self._symbol = symbol
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol
