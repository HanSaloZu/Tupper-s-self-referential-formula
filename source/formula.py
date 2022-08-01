from math import floor
from decimal import Decimal, getcontext


class TupperFormula:
    def __init__(self, k):
        getcontext().prec = 10000
        self.k = k

    def should_pixel_be_drawn(self, x, y):
        y += self.k

        power_of_two = -17 * floor(x) - floor(y) % 17
        formula = floor(
            (floor(Decimal(y)/17) * (2 ** Decimal(power_of_two))) % 2)

        return formula > 0.5
