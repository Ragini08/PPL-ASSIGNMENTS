import turtle
import time


class Line:
    def __init__(self, l = 0):
        self.__length  = l
    def get_length(self):
        return  self.length
    def set_length(self, l):
        self.length = l
    def draw(self):
        t = turtle.Turtle()
        t.forward(self.length)

turtle.write(' SHAPES ', font = ('Times New Roman', 36, 'bold'))
time.sleep(0.35)
turtle.clearscreen()
l = Line()
l.set_length(200)
turtle.penup()
turtle.setposition(-300,50)
turtle.write(' LINE ', font = ('Times New Roman', 36, 'bold'))
turtle.setposition(-300,0)
turtle.write(' Straight path with no thickness', font = ('Times New Roman', 20))
turtle.setposition(100,0)
turtle.pendown()
l.draw()

time.sleep(0.8)

import Circle
exec('Circle')