from expression import Expression
from pair import Pair


class Bank():

    def __init__(self):
        self.rates: dict[Pair, int] = {}

    def reduce(self, source: Expression, to: str) -> Expression:
        return source.reduce(self, to)

    def addRate(self, frm: str, to: str, rate: int):
        self.rates[Pair(frm, to)] = rate

    def rate(self, frm: str, to: str):
        return 1 if frm == to else self.rates.get(Pair(frm, to), 1)
