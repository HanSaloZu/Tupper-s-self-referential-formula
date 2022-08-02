from turtle import Screen, Turtle


class CustomScreen:
    def __init__(self, title, width, height, pixel_size):
        self._screen = Screen()
        self._screen.title(title)
        self._screen.setup(width=width, height=height)
        self._screen.tracer(0)

        self._turtle = Turtle(shape="square")
        self._turtle.shapesize(pixel_size / 20, pixel_size / 20)
        self._turtle.hideturtle()
        self._turtle.up()

    def draw_pixel(self, x, y):
        self._turtle.goto(x, y)
        self._turtle.stamp()

    def mainloop(self):
        self._screen.mainloop()

    def update(self):
        self._screen.update()
