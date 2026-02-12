from money import Money


class Franc(Money):

    def times(self, multiplier: int) -> 'Money':
        return Money.franc(self._amount * multiplier)
