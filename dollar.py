from money import Money

class Dollar(Money):

    def times(self, multiplier: int) -> 'Dollar':
        return Dollar(self._amount * multiplier)
