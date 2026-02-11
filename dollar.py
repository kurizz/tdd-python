class Dollar():

    def __init__(self, amount: int):
        self._amount = amount

    def times(self, multiplier: int):
        return Dollar(self._amount * multiplier)

    def __eq__(self, obj: object):
        return self._amount == obj._amount
