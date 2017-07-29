class Spot:
    f = 100000
    g = 100000
    previous = None
    blocked = False
    def __init__(self, i, j, rect):
        self.i = i
        self.j = j
        self.rectangle = rect

    def color(self, co):
        self.rectangle.set_facecolor(co)

    def __eq__(self, other):
        if isinstance(other, Spot):
            return self.i == other.i and self.j == other.j
        return False

    def neighbours(self, spots):
        if self.i < len(spots) - 1 and not spots[self.i + 1][self.j].blocked:
            yield spots[self.i + 1][self.j]

        if self.j < len(spots[0]) - 1 and not spots[self.i][self.j + 1].blocked:
            yield spots[self.i][self.j + 1]

        if self.i > 0 and not spots[self.i - 1][self.j].blocked:
            yield spots[self.i - 1][self.j]

        if self.j > 0 and not spots[self.i][self.j - 1].blocked:
            yield spots[self.i][self.j - 1]

        if self.i > 0 and self.j > 0 and not spots[self.i - 1][self.j - 1].blocked:
            yield spots[self.i - 1][self.j - 1]

        if self.i > 0 and self.j < (len(spots[0]) - 1) and not spots[self.i - 1][self.j + 1].blocked:
            yield spots[self.i - 1][self.j + 1]

        if self.i < len(spots) - 1 and self.j > 0 and not spots[self.i + 1][self.j - 1].blocked:
            yield spots[self.i + 1][self.j - 1]

        if self.i < len(spots) - 1 and self.j < len(spots[0]) - 1 and not spots[self.i + 1][self.j + 1].blocked:
            yield spots[self.i + 1][self.j + 1]

    def __repr__(self):
        return '({0.i},{0.j}->f={0.f},g={0.g})'.format(self)
