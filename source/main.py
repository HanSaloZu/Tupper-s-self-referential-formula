import config as cfg
from display import CustomScreen
from formula import TupperFormula


def main():
    _NUMBER_OF_BITMAP_COLUMNS = 106
    _NUMBER_OF_BITMAP_ROWS = 17
    START_X = -(_NUMBER_OF_BITMAP_COLUMNS * cfg.PIXEL_SIZE) / 2
    START_Y = -(_NUMBER_OF_BITMAP_ROWS * cfg.PIXEL_SIZE) / 2

    with open(cfg.BASE_DIR + "/source/k.txt", "r") as k_txt:
        k = int(k_txt.read())

    tformula = TupperFormula(k)
    screen = CustomScreen(cfg.SCREEN_TITLE, cfg.SCREEN_WIDTH,
                          cfg.SCREEN_HEIGHT, cfg.PIXEL_SIZE)

    x = START_X
    y = START_Y

    for column in range(_NUMBER_OF_BITMAP_COLUMNS):
        for row in range(_NUMBER_OF_BITMAP_ROWS):
            if tformula.should_pixel_be_drawn(column, row):
                screen.draw_pixel(x, y)

            y += cfg.PIXEL_SIZE

        screen.update()
        y = START_Y
        x += cfg.PIXEL_SIZE

    screen.mainloop()


if __name__ == "__main__":
    main()
