from expression import Expression
from sum import Sum


class Money(Expression):

    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int) -> 'Money':
        return Money(self.amount * multiplier, self.currency)

    def plus(self, addend: int) -> Expression:
        return Sum(self, addend)

    def reduce(self, to: str):
        return self

    @property
    def currency(self) -> str:
        return self._currency

    @property
    def amount(self) -> int:
        return self._amount

    def __eq__(self, money: 'Money') -> bool:
        return self.amount == money.amount and self.currency == money.currency

    def __repr__(self):
        return str(self.amount) + self.currency

    @staticmethod
    def dollar(amount: int) -> 'Money':
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> 'Money':
        return Money(amount, "CHF")
