import turtle
import time

class Circle:
    # def __init__(self, r = 0):
    #   self.__radius = r
    def set_radius(self, r):
        self.radius = r

    def get_radius(self):
        return (self.radius)

    def find_area(self):
        pi = 3.14
        return (pi * self.radius * self.radius)

    def draw(self):
        t = turtle.Turtle()
        t.circle(self.radius)


turtle.clearscreen()
c = Circle()
c.set_radius(100)
turtle.penup()
turtle.setposition(-300,50)
turtle.write(' CIRCLE ', font = ('Times New Roman', 36, 'bold'))
turtle.setposition(-300,0)
turtle.write(' D = 2 * r ', font = ('Times New Roman', 20))
turtle.pendown()
c.draw()
time.sleep(0.8)
import Square
exec('Square')