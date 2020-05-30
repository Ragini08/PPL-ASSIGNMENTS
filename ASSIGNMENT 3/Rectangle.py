import turtle
import time

class Rectangle:
    def __init__(self, l = 0, w = 0):
        self.__length = l
        self.__width = w
    def set_side(self, l, w):
        self.length = l
        self.width  = w
    def get_area(self):
        return (self.length * self.width)
    def draw(self):
        t = turtle.Turtle()
        t.forward(self.length)
        t.right(90)
        t.forward(self.width)
        t.right(90)
        t.forward(self.length)
        t.right(90)
        t.forward(self.width)
        t.right(90)

turtle.clearscreen()
r = Rectangle()
r.set_side(180, 250)
turtle.penup()
turtle.setposition(-350,50)
turtle.write(' RECTANGLE ', font = ('Times New Roman', 36, 'bold'))
turtle.setposition(-300,0)
turtle.write(' Opposite sides are equal ', font = ('Times New Roman', 20))
turtle.setposition(-300,-50)
turtle.write(' Interior angles = 90 degree ', font = ('Times New Roman', 20))
turtle.home()
turtle.pendown()
r.draw()
time.sleep(2)
import Triangle
exec('Triangle')