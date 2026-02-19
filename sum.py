from expression import Expression
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from money import Money
    from bank import Bank


class Sum(Expression):

    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: Bank, to: str) -> 'Money':
        from money import Money
        amount = self.augend.amount + self.addend.amount
        return Money(amount, to)

