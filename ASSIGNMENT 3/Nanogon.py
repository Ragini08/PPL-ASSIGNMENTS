import turtle
import time

class Nanogon:
    def __init__(self, s = 0):
        self.__side = s
    def set_side(self, s):
        self.side = s
    def get_side(self):
        return self.side
    def draw(self):
        t = turtle.Turtle()
        for i in range(9):
            t.forward(self.side)
            t.right(40)


turtle.clearscreen()
n = Nanogon()
n.set_side(90)
turtle.penup()
turtle.setposition(-300,50)
turtle.write(' NANOGON ', font = ('Times New Roman', 36, 'bold'))
turtle.setposition(-300,0)
turtle.write(' Interior angles = 140 degree ', font = ('Times New Roman', 20))
turtle.home()
turtle.pendown()
n.draw()
time.sleep(0.8)
turtle.Screen().exitonclick()