import turtle
import time
class square():
	def __init__(self,a = 5):
		self.__side = a

	def get_side(self):
		return self.__side

	def find_area(self):
		return (self.__side * self.__side)

	def find_perimeter(self):
		return(4 * self.__side)

	def draw(self):
		t = turtle.Turtle()
		t.forward(self.__side)
		t.left(90)
		t.forward(self.__side)
		t.left(90)
		t.forward(self.__side)
		t.left(90)
		t.forward(self.__side)
		t.left(90)


turtle.clearscreen()
s = square(200)
turtle.penup()
turtle.setposition(-300,50)
turtle.write(' SQUARE ', font = ('Times New Roman', 36, 'bold'))
turtle.setposition(-300,0)
turtle.write(' Equal all 4 sides ', font = ('Times New Roman', 20))
turtle.setposition(-300,-50)
turtle.write(' Interior angles = 90 degree ', font = ('Times New Roman', 20))
turtle.home()
turtle.pendown()
s.draw()
time.sleep(2)
import Rectangle
exec('Rectangle')