import turtle
import time

class Pentagon:
    def __init__(self, n = 0, l = 0):
        self.num = n
        self.length = l
    def set_props(self, n, l):
        self.num = n
        self.length = l
    def draw(self):
        t = turtle.Turtle()
        angle = 360.0 / self.num

        for i in range(self.num):
            t.forward(self.length)
            t.right(angle)

turtle.clearscreen()
p = Pentagon()
p.set_props(5, 150)
turtle.penup()
turtle.setposition(-300,50)
turtle.write(' PENTAGON ', font = ('Times New Roman', 36, 'bold'))
turtle.setposition(-300,0)
turtle.write(' Interior angles = 108 degree ', font = ('Times New Roman', 20))
turtle.home()
turtle.pendown()
p.draw()
time.sleep(0.8)
import Hexagon
exec('Hexagon')