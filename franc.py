class Franc():

    def __init__(self, amount: int):
        self._amount = amount

    def times(self, multiplier: int) -> 'Franc':
        return Franc(self._amount * multiplier)

    def __eq__(self, obj: object) -> bool:
        return self._amount == obj._amount