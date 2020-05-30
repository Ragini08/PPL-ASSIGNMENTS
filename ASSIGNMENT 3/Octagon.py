import turtle
import time

class Octagon:
    def __init__(self, s = 0):
        self.__side = s
    def set_side(self, s):
        self.side = s
    def get_side(self):
        return self.side
    def draw(self):
        t = turtle.Turtle()
        for i in range(8):
            t.forward(self.side)
            t.right(45)

turtle.clearscreen()
o = Octagon()
o.set_side(100)
turtle.penup()
turtle.setposition(-300,50)
turtle.write(' OCTAGON ', font = ('Times New Roman', 36, 'bold'))
turtle.setposition(-300,0)
turtle.write(' Interior angles = 135 degree ', font = ('Times New Roman', 20))
turtle.home()
turtle.pendown()
o.draw()
time.sleep(0.8)

import Nanogon
exec('Nanogon')
