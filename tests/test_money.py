from money import Money
from bank import Bank
from sum import Sum

class TestMoney():

    def test_dollar_multiplication(self):
        five = Money.dollar(5)
        assert Money.dollar(10) == five.times(2)
        assert Money.dollar(15) == five.times(3)

    def test_simple_addtion(self):
        sum = Money.dollar(5).plus(Money.dollar(5))
        reduced = Bank().reduce(sum, "USD")
        assert Money.dollar(10) == reduced

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        assert five == sum.augend
        assert five == sum.addend

    def test_reduce_sum(self):
        sum = Sum(Money.dollar(3), Money.dollar(4))
        reduced = Bank().reduce(sum, "USD")
        assert Money.dollar(7) == reduced

    def test_reduce_money(self):
        reduced = Bank().reduce(Money.dollar(1), "USD")
        assert Money.dollar(1) == reduced

    def test_equality(self):
        assert Money.dollar(5) == Money.dollar(5)
        assert not Money.dollar(5) == Money.dollar(6)
        assert not Money.dollar(5) == Money.franc(5)

    def test_currenry(self):
        assert "USD" == Money.dollar(1).currency
        assert "CHF" == Money.franc(1).currency

    def test_amount(self):
        assert 10 is Money.dollar(10).amount
