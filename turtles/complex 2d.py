import turtle
import random

wn = turtle.Screen()
seren = turtle.Turtle()
wn.bgcolor ("grey")

colors = ["cyan", "purple", "blue"]

seren.penup()
seren.forward(90)
seren.left(45)
seren.pendown()

def branch() :
  for i in range(3):
      for i in range(3):
          seren.forward(30)
          seren.backward(30)
          seren.right(45)
      seren.left(90)
      seren.backward(30)
      seren.left(45)
  seren.right(90)
  seren.forward(90)

for i in range (8):
   branch()
   seren.left(45)


# seren.color(random.choice(colors))


wn = exitonclick ()