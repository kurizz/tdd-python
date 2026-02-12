from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from dollar import Dollar
    from franc import Franc


class Money(ABC):

    def __init__(self, amount: int):
        self._amount = amount

    @abstractmethod
    def times(self, multiplier: int):
        pass

    def __eq__(self, money: 'Money') -> bool:
        return self._amount == money._amount and type(self) == type(money)

    @staticmethod
    def dollar(amount: int) -> 'Dollar':
        from dollar import Dollar
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> 'Franc':
        from franc import Franc
        return Franc(amount)
