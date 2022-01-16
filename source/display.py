from turtle import Screen, Turtle


def create_turtle(pixel_size):
    turtle = Turtle()
    turtle.shape("square")
    turtle.shapesize(pixel_size / 20, pixel_size / 20)
    turtle.hideturtle()
    turtle.up()

    return turtle


def create_screen(title, width, height):
    screen = Screen()
    screen.title(title)
    screen.setup(width=width, height=height)
    screen.tracer(0)

    return screen


def draw_pixel(turtle, x, y):
    turtle.goto(x, y)
    turtle.stamp()
