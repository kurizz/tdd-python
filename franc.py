from money import Money

class Franc(Money):

    def times(self, multiplier: int) -> 'Franc':
        return Franc(self._amount * multiplier)
