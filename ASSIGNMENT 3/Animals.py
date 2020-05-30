#Assignment 3 Animals 10 classes
import time

class Cat:
    def __init__(self, color="", legs=0):
        self.__color = color
        self.__legs = legs
    def get_color(self):
        return (self.color)
    def get_legs(self):
        return (self.legs)
    def set_color(self, c):
        self.color = c
    def set_legs(self, l):
        self.legs = l
    def set_nature(self, n):
        self.nature = n
    def get_nature(self):
        return (self.nature)
    def set_food(self, f):
        self.food = f
    def get_food(self):
        return (self.food)

class Dog:
    def __init__(self, color="", legs=0):
        self.__color = color
        self.__legs = legs
    def get_color(self):
        return (self.color)
    def get_legs(self):
        return (self.legs)
    def set_color(self, c):
        self.color = c
    def set_legs(self, l):
        self.legs = l
    def set_nature(self, n):
        self.nature = n
    def get_nature(self):
        return (self.nature)
    def set_food(self, f):
        self.food = f
    def get_food(self):
        return (self.food)

class Hippo:
    def __init__(self, color="", legs=0):
        self.__color = color
        self.__legs = legs
    def get_color(self):
        return (self.color)
    def get_legs(self):
        return (self.legs)
    def set_color(self, c):
        self.color = c
    def set_legs(self, l):
        self.legs = l
    def set_nature(self, n):
        self.nature = n
    def get_nature(self):
        return (self.nature)
    def set_food(self, f):
        self.food = f
    def get_food(self):
        return (self.food)

class Flamingo:
    def __init__(self, color="", legs=0):
        self.__color = color
        self.__legs = legs
    def get_color(self):
        return (self.color)
    def get_legs(self):
        return (self.legs)
    def set_color(self, c):
        self.color = c
    def set_legs(self, l):
        self.legs = l
    def set_nature(self, n):
        self.nature = n
    def get_nature(self):
        return (self.nature)
    def set_food(self, f):
        self.food = f
    def get_food(self):
        return (self.food)

class Tiger:
    def __init__(self, color="", legs=0):
        self.__color = color
        self.__legs = legs
    def get_color(self):
        return (self.color)
    def get_legs(self):
        return (self.legs)
    def set_color(self, c):
        self.color = c
    def set_legs(self, l):
        self.legs = l
    def set_nature(self, n):
        self.nature = n
    def get_nature(self):
        return (self.nature)
    def set_food(self, f):
        self.food = f
    def get_food(self):
        return (self.food)

class Peacock:
    def __init__(self, color="", legs=0):
        self.__color = color
        self.__legs = legs
    def get_color(self):
        return (self.color)
    def get_legs(self):
        return (self.legs)
    def set_color(self, c):
        self.color = c
    def set_legs(self, l):
        self.legs = l
    def set_nature(self, n):
        self.nature = n
    def get_nature(self):
        return (self.nature)
    def set_food(self, f):
        self.food = f
    def get_food(self):
        return (self.food)

class Deer:
    def __init__(self, color="", legs=0):
        self.__color = color
        self.__legs = legs
    def get_color(self):
        return (self.color)
    def get_legs(self):
        return (self.legs)
    def set_color(self, c):
        self.color = c
    def set_legs(self, l):
        self.legs = l
    def set_nature(self, n):
        self.nature = n
    def get_nature(self):
        return (self.nature)
    def set_food(self, f):
        self.food = f
    def get_food(self):
        return (self.food)

class Elephant:
    def __init__(self, color="", legs=0):
        self.__color = color
        self.__legs = legs
    def get_color(self):
        return (self.color)
    def get_legs(self):
        return (self.legs)
    def set_color(self, c):
        self.color = c
    def set_legs(self, l):
        self.legs = l
    def set_size(self, n):
        self.size = n
    def get_size(self):
        return (self.size)
    def set_food(self, f):
        self.food = f
    def get_food(self):
        return (self.food)

class Raccoon:
    def __init__(self, color="", legs=0):
        self.__color = color
        self.__legs = legs
    def get_color(self):
        return (self.color)
    def get_legs(self):
        return (self.legs)
    def set_color(self, c):
        self.color = c
    def set_legs(self, l):
        self.legs = l
    def set_nature(self, n):
        self.nature = n
    def get_nature(self):
        return (self.nature)
    def set_food(self, f):
        self.food = f
    def get_food(self):
        return (self.food)

class Snake:
    def __init__(self, color=""):
        self.__color = color
    def get_color(self):
        return (self.color)
    def set_color(self, c):
        self.color = c
    def set_nature(self, n):
        self.nature = n
    def get_nature(self):
        return (self.nature)
    def set_food(self, f):
        self.food = f
    def get_food(self):
        return (self.food)


print('####################ANIMALS####################')
print('--------------------1.CAT--------------------')
c = Cat()
c.set_color("White Black Ginger")
c.set_legs(4)
c.set_nature("Inquisitive")
c.set_food("Fish Milk")
print("Color : ", c.get_color())
print("Legs : ", c.get_legs())
print("Nature : ", c.get_nature())
print("Food : ", c.get_food())

print('--------------------2.RACCOON--------------------')
c = Raccoon()
c.set_color("Grey")
c.set_legs(4)
c.set_nature("Adaptable")
c.set_food("Tiny animals")
print("Color : ", c.get_color())
print("Legs : ", c.get_legs())
print("Nature : ", c.get_nature())
print("Food : ", c.get_food())

print('--------------------3.DOG--------------------')
d = Dog()
d.set_color("Brown White Black")
d.set_legs(4)
d.set_nature("Loyal")
d.set_food("Raw meat Bones")
print("Color : ", d.get_color())
print("Legs : ", d.get_legs())
print("Nature : ", d.get_nature())
print("Food : ", d.get_food())

print('--------------------4.HIPPO--------------------')
h = Hippo()
h.set_color("Purplish-grey")
h.set_legs(4)
h.set_nature("Dangerous")
h.set_food("Plants")
print("Color : ", h.get_color())
print("Legs : ", h.get_legs())
print("Nature : ", h.get_nature())
print("Food : ", h.get_food())

print('--------------------5.FLAMINGO--------------------')
f = Flamingo()
f.set_color("Pink")
f.set_legs(2)
f.set_nature("Agressive")
f.set_food("Algae")
print("Color : ", f.get_color())
print("Legs : ", f.get_legs())
print("Nature : ", f.get_nature())
print("Food : ", f.get_food())

print('--------------------6.TIGER--------------------')
t = Tiger()
t.set_color("Yellow")
t.set_legs(4)
t.set_nature("Hunters")
t.set_food("Animals")
print("Color : ", t.get_color())
print("Legs : ", t.get_legs())
print("Nature : ", t.get_nature())
print("Food : ", t.get_food())

print('--------------------7.PEACOCK--------------------')
p = Peacock()
p.set_color("Iridescent-blue")
p.set_legs(2)
p.set_nature("social")
p.set_food("Insects Snakes")
print("Color : ", p.get_color())
print("Legs : ", p.get_legs())
print("Nature : ", p.get_nature())
print("Food : ", p.get_food())

print('--------------------8.Deer--------------------')
r = Deer()
r.set_color("White-spotted-yellow")
r.set_legs(4)
r.set_nature("Consumer in ecosytem")
r.set_food("Green plants")
print("Color : ", r.get_color())
print("Legs : ", r.get_legs())
print("Role : ", r.get_nature())
print("Food : ", r.get_food())

print('--------------------9.Elephant--------------------')
e = Elephant()
e.set_color("Grey")
e.set_legs(4)
e.set_size("Huge")
e.set_food("Bushes")
print("Color : ", e.get_color())
print("Legs : ", e.get_legs())
print("Size : ", e.get_size())
print("Food : ", e.get_food())

print('--------------------10.Snake--------------------')
s = Snake()
s.set_color("Black Green ")
s.set_food("Insects")
print("Color : ", s.get_color())
print("Food : ", s.get_food())

time.sleep(0.8)

import Line
exec('Line')