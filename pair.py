class Pair(object):

    def __init__(self, frm: str, to: str):
        self.frm = frm
        self.to = to

    def __eq__(self, pair: 'Pair') -> bool:
        return self.frm == pair.frm and self.to == pair.to

    def __hash__(self):
        return 0
