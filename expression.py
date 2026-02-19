from abc import ABC
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from money import Money
    from bank import Bank


class Expression(ABC):
    def reduce(self, bank: Bank, to: str) -> Money:
        pass
