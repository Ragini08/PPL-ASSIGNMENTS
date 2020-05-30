import turtle
import time

class Heptagon:
    def __init__(self, s = 0):
        self.__side = s
    def set_side(self, s):
        self.side = s
    def get_side(self):
        return self.side
    def draw(self):
        t = turtle.Turtle()
        for i in range(7):
            t.forward(self.side)
            t.right(51.42)

turtle.clearscreen()
h = Heptagon()
h.set_side(100)
turtle.penup()
turtle.setposition(-300,50)
turtle.write(' HEPTAGON ', font = ('Times New Roman', 36, 'bold'))
turtle.setposition(-300,0)
turtle.write(' Interior angles = 128.57 degree ', font = ('Times New Roman', 20))
turtle.home()
turtle.pendown()
h.draw()
time.sleep(0.8)
import Octagon
exec('Octagon')
