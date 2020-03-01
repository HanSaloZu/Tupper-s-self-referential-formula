from turtle import Screen, Turtle


def get_turtle():
    turtle = Turtle()
    turtle.shape("square")
    turtle.shapesize(0.6, 0.6)
    turtle.pensize(1)
    turtle.hideturtle()

    return turtle


def get_customized_screen():
    screen = Screen()
    screen.title("Tupper's self-referential formula")
    screen.setup(width=1600, height=450)
    screen.tracer(0)

    return screen


def draw_pixel(turtle, x, y):
    turtle.goto(x, y)
    turtle.stamp()
