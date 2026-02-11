class Dollar():

    def __init__(self, amount: int):
        self.amount = amount

    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)

    def __eq__(self, obj: object):
        return self.amount == obj.amount
