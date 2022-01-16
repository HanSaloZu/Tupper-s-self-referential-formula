from turtle import Screen, Turtle


def create_turtle(pixel_size):
    turtle = Turtle()
    turtle.shape("square")
    turtle.shapesize(pixel_size / 20, pixel_size / 20)
    turtle.hideturtle()
    turtle.up()

    return turtle


def create_screen():
    screen = Screen()
    screen.title("Tupper's self-referential formula")
    screen.setup(width=1300, height=450)
    screen.tracer(0)

    return screen


def draw_pixel(turtle, x, y):
    turtle.goto(x, y)
    turtle.stamp()
