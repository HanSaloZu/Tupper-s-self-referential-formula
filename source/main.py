import formula
import display
import config as cfg


def main():
    with open(cfg.BASE_DIR + "/source/k.txt", "r") as k_txt:
        k = int(k_txt.read())

    screen = display.create_screen(
        cfg.SCREEN_TITLE, cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT)

    _NUMBER_OF_BITMAP_COLUMNS = 106
    _NUMBER_OF_BITMAP_ROWS = 17
    START_X = -(_NUMBER_OF_BITMAP_COLUMNS * cfg.PIXEL_SIZE) / 2
    START_Y = -(_NUMBER_OF_BITMAP_ROWS * cfg.PIXEL_SIZE) / 2

    x = START_X
    y = START_Y
    turtle = display.create_turtle(cfg.PIXEL_SIZE)

    for column in range(_NUMBER_OF_BITMAP_COLUMNS):
        for row in range(_NUMBER_OF_BITMAP_ROWS):
            if formula.should_pixel_be_drawn(column, row + k):
                display.draw_pixel(turtle, x, y)

            y += cfg.PIXEL_SIZE

        screen.update()
        y = START_Y
        x += cfg.PIXEL_SIZE

    screen.mainloop()


if __name__ == "__main__":
    main()
