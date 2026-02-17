from expression import Expression


class Bank():

    def reduce(self, source: Expression, to: str):
        return source.reduce(to)
