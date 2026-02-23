from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from money import Money
    from bank import Bank


class Expression(ABC):

    @abstractmethod
    def times(self, multiplier: int) -> 'Expression':
        ...

    @abstractmethod
    def plus(self, addend: 'Expression'):
        ...

    @abstractmethod
    def reduce(self, bank: Bank, to: str) -> Money:
        ...
