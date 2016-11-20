

import turtle
window = turtle.Screen()


ella = turtle.Turtle()

ella.color('#2AFB7E')
ella.pensize(4)
ella.forward(150)
ella.left(90)
ella.forward(75)
ella.left(90)
ella.forward(150)
ella.left(90)
ella.forward(75)


def makeSquare(turtle, size):
    for i in range(4):
        turtle.pensize(5)
        turtle.speed(0)
        turtle.color('#dddd33')
        turtle.forward(size)
        turtle.left(90)
        
makeSquare(turtle, 260)

window.exitonclick()     


