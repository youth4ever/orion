import turtle  # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]:  # repeat four times
    alex.pensize(5)
    alex.color(aColor)
    alex.forward(250)
    alex.left(90)

wn.exitonclick()
