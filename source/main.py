import mathematics
import display
from decimal import Decimal, getcontext


if __name__ == "__main__":
    screen = display.get_customized_screen()

    turtle = display.get_turtle()
    turtle.up()

    getcontext().prec = 10000

    with open("k.txt", "r") as txt_k:
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
