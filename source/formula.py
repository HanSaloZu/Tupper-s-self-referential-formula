import math
from decimal import Decimal, getcontext


def is_pixel_black(x, y, k):
    getcontext().prec = 10000
    y += k

    power_of_two = (-17 * math.floor(x)) - (math.floor(Decimal(y)) % 17)
    formula = math.floor((math.floor(Decimal(y)/17) * (2 ** Decimal(power_of_two))) % 2)

    return formula > 0.5
