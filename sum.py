from expression import Expression
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from money import Money
    from bank import Bank


class Sum(Expression):

    def __init__(self, augend: Expression, addend: Expression):
        self.augend = augend
        self.addend = addend

    def times(self, multiplier: int):
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def reduce(self, bank: Bank, to: str) -> 'Money':
        from money import Money
        amount = self.augend.reduce(bank, to).amount + self.addend.reduce(bank, to).amount
        return Money(amount, to)

