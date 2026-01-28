import turtle
from turtle import *
t = Turtle()

t.speed(10)

def circle(d):
    length = d*3.14/360
    for i in range(360):
        t.forward(length)
        t.right(1)

for i in range(13):
    circle(200)
    t.right(360/13)


turtle.done()