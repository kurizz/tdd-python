from expression import Expression
from sum import Sum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bank import Bank


class Money(Expression):

    def __init__(self, amount: float, currency: str):
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int) -> Expression:
        return Money(self.amount * multiplier, self.currency)

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def reduce(self, bank: Bank, to: str):
        rate = bank.rate(self.currency, to)
        return Money(self.amount / rate, to)

    @property
    def currency(self) -> str:
        return self._currency

    @property
    def amount(self) -> float:
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
