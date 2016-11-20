import math
import turtle

def drawCircle(color):

    turtle.begin_fill()
    turtle.shape("circle")
    turtle.shapesize(0.3,0.3)
    turtle.circle(90)
    turtle.color(color)
    turtle.speed(9)
        
    turtle.end_fill()

    t = turtle.Turtle()
    screen = t.getscreen()


def main():
    drawCircle("lightblue")
    turtle.exitonclick()




if __name__ == "__main__":
    main()

