from money import Money


class Dollar(Money):

    def times(self, multiplier: int) -> 'Money':
        return Dollar(self._amount * multiplier)
