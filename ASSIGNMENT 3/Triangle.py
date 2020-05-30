import turtle
import time

class Triangle:
    def __init__(self, s1 = 0, s2 = 0, s3 = 0):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
    def set_side(self, s1, s2, s3):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
    def get_side(self):
        return (self.side1, self.side2, self.side3)
    def get_perimeter(self):
        return (self.side1 + self.side2 + self.side3)
    def draw(self):
        t = turtle.Turtle()
        t.forward(self.side1)
        t.left(120)
        t.forward(self.side2)
        t.left(120)
        t.forward(self.side3)


turtle.clearscreen()
t = Triangle()
t.set_side(300, 300, 300)
turtle.penup()
turtle.setposition(-340,50)
turtle.write(' EQUILATERAL', font = ('Times New Roman', 36, 'bold'))
turtle.setposition(-300,0)
turtle.write(' TRIANGLE ', font = ('Times New Roman', 36, 'bold'))
turtle.setposition(-300,-50)
turtle.write(' Interior angles = 60 degree ', font = ('Times New Roman', 20))

turtle.home()
turtle.pendown()
t.draw()
time.sleep(0.8)
import Pentagon
exec('Pentagon')