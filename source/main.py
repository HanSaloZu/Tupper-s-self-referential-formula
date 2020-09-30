import os
import mathematics
import display
from decimal import Decimal, getcontext


if __name__ == "__main__":
    screen = display.create_screen()

    turtle = display.create_turtle()
    turtle.up()

    getcontext().prec = 10000
    DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(DIR + "/source/k.txt", "r") as txt_k:
        k = Decimal(txt_k.read())

    x = -700
    y = -128

    pixel_size = 13

    for column in range(106):
        for row in range(17):
            screen.update()

            if mathematics.is_pixel_black(column, row, k):
                display.draw_pixel(turtle, x, y)

            y += pixel_size

        y = -128
        x += pixel_size

    screen.mainloop()
