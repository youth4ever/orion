

import turtle
wn = turtle.Screen()


jose = turtle.Turtle()
jose.shape("turtle")
jose.penup()

# screen.bgpic()
wn.bgpic("C:/BT_private/SORGN8x.gif")
# wn.bgcolor("orange")

for size in range(10):
    jose.forward(50)
    jose.stamp()
    jose.forward(-50)
    jose.right(36)

wn.exitonclick()
