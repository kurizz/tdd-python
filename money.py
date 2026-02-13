from abc import ABC


class Money(ABC):

    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self.currency)

    @property
    def currency(self) -> str:
        return self._currency

    def __eq__(self, money: 'Money') -> bool:
        return self._amount == money._amount and self.currency == money.currency

    def __repr__(self):
        return str(self._amount) + self.currency

    @staticmethod
    def dollar(amount: int) -> 'Money':
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> 'Money':
        return Money(amount, "CHF")
