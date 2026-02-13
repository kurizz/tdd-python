from typing import TYPE_CHECKING
from abc import ABC

if TYPE_CHECKING:
    from dollar import Dollar
    from franc import Franc


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
    def dollar(amount: int) -> 'Dollar':
        from dollar import Dollar
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int) -> 'Franc':
        from franc import Franc
        return Franc(amount, "CHF")
