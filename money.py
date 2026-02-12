from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from dollar import Dollar
    from franc import Franc


class Money(ABC):

    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    @abstractmethod
    def times(self, multiplier: int):
        pass

    def currency(self) -> str:
        return self._currency

    def __eq__(self, money: 'Money') -> bool:
        return self._amount == money._amount and type(self) == type(money)

    @staticmethod
    def dollar(amount: int) -> 'Dollar':
        from dollar import Dollar
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int) -> 'Franc':
        from franc import Franc
        return Franc(amount, "CHF")
