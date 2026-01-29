import turtle
from turtle import *
t = Turtle()

t.speed(10)


def square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)


def circle(d):
    length = d*3.14/360
    for i in range(360):
        t.forward(length)
        t.right(1)

def mondala(size, circles):
    for i in range(circles):
        circle(size)
        t.right(360/circles)

def spiral(squares):
    for i in range(squares):
        square(375/squares * i)
        t.right(300/squares)


spiral(50)

turtle.done()