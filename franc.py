from money import Money


class Franc(Money):

    def times(self, multiplier: int) -> 'Money':
        return Franc(self._amount * multiplier)
