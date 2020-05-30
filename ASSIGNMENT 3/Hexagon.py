import turtle
import time

class Hexagon:
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
h = Hexagon()
h.set_props(6, 150)
turtle.penup()
turtle.setposition(-300,50)
turtle.write(' HEXAGON ', font = ('Times New Roman', 36, 'bold'))
turtle.setposition(-300,0)
turtle.write(' Interior angles = 120 degree ', font = ('Times New Roman', 20))
turtle.home()
turtle.pendown()
h.draw()
time.sleep(0.8)
import Heptagon
exec('Heptagon')