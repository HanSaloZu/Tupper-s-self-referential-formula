from decimal import Decimal, getcontext
from math import floor


class TupperFormula:
    def __init__(self, k):
        getcontext().prec = 10000
        self.k = k

    def should_pixel_be_drawn(self, x, y):
        y += self.k

        power_of_two = Decimal(-17 * x - y % 17)
        return 0.5 < floor((Decimal(y) // 17 * (2 ** power_of_two)) % 2)
