import math
from decimal import Decimal, getcontext


getcontext().prec = 10000


def is_pixel_black(x, y):
    power_of_two = -17 * math.floor(x) - math.floor(y) % 17
    formula = math.floor((math.floor(Decimal(y)/17) *
                         (2 ** Decimal(power_of_two))) % 2)

    return formula > 0.5
