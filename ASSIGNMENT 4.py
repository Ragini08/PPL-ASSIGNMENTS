#ASSIGNMENT 4 INHERITANCE

#Shape-Line,Circle,Polygon
#Polygon-Triangle,Quadrilateral,Pentagon,Hexagon,Heptagon,Octagon,Nanogon,Decagon

#Animal-Herbivore,Carnivore,Omnivore
#Herbivore-Horse,Rabbit,Cow,Deer
#Carnivore-Frog,Lion,Tiger,Eagle
#Omnivore-Raccoon,Pig
class Shape():
    def info(self):
        print("-----------------------------10 SHAPES-----------------------------")

class Line(Shape):
    def info(self):
        print("Line is straight path with no width")
        print("INHERITANCE : Shape > Line")

class Circle(Shape):
    def info(self):
        print("Circle has diameter and radius.")
        print("INHERITANCE : Shape > Circle")
    def ar(self):
        print("Area = pi*r*r AND Circumference = 2*pi*r")

class Polygon(Shape):
    def angle(self):
        pass

class Triangle(Polygon):
    def info(self):
        print("Triangle has 3 sides.")
        print("INHERITANCE : Shape > Polygon > Triangle")
    def angle(self):
        print("Sum of angles = 180 degree")

class Quadrilateral(Polygon):
    def info(self):
        print("Quadrilateral has 4 sides.")
        print("INHERITANCE : Shape > Polygon > Quadrilateral")
    def angle(self):
        print("Sum of angles = 360 degree")

class Pentagon(Polygon):
    def info(self):
        print("Pentagon has 5 sides.")
        print("INHERITANCE : Shape > Polygon > Pentagon")
    def angle(self):
        print("Sum of angles = 540 degree")

class Hexagon(Polygon):
    def info(self):
        print("Hexagon has 6 sides.")
        print("INHERITANCE : Shape > Polygon > Hexagon")
    def angle(self):
        print("Sum of angles = 720 degree")

class Heptagon(Polygon):
    def info(self):
        print("Heptagon has 7 sides.")
        print("INHERITANCE : Shape > Polygon > Heptagon")
    def angle(self):
        print("Sum of angles = 900 degree")

class Octagon(Polygon):
    def info(self):
        print("Octagon has 8 sides.")
        print("INHERITANCE : Shape > Polygon > Octagon")
    def angle(self):
        print("Sum of angles = 1080 degree")

class Nanogon(Polygon):
    def info(self):
        print("Nanogon has 9 sides.")
        print("INHERITANCE : Shape > Polygon > Nanogon")
    def angle(self):
        print("Sum of angles = 1260 degree")

class Decagon(Polygon):
    def info(self):
        print("Decagon has 10 sides.")
        print("INHERITANCE : Shape > Polygon > Decagon")
    def angle(self):
        print("Sum of angles = 1440 degree")

class Animal():
    def info(self):
        print("")
        print("-----------------------------10 ANIMALS-----------------------------")
    def hierarchy(self):
        pass

class Herbivore(Animal):
    def info(self):
        print("Eats plants.")

class Carnivore(Animal):
    def info(self):
        print("Eats meat.")

class Omnivore(Animal):
    def info(self):
        print("Eats plants and meat both.")

class Horse(Herbivore):
    def hierarchy(self):
        print("ANIMAL > HERBIVORE > HORSE")

class Rabbit(Herbivore):
    def hierarchy(self):
        print("ANIMAL > HERBIVORE > RABBIT")


class Cow(Herbivore):
    def hierarchy(self):
        print("ANIMAL > HERBIVORE > COW")

class Deer(Herbivore):
    def hierarchy(self):
        print("ANIMAL > HERBIVORE > DEER")

class Frog(Carnivore):
    def hierarchy(self):
        print("ANIMAL > CARNIVORE > Frog")

class Lion(Carnivore):
    def hierarchy(self):
        print("ANIMAL > CARNIVORE > LION")

class Tiger(Carnivore):
    def hierarchy(self):
        print("ANIMAL > CARNIVORE > Tiger")

class Eagle(Carnivore):
    def hierarchy(self):
        print("ANIMAL > CARNIVORE > EAGLE")

class Pig(Omnivore):
    def hierarchy(self):
        print("ANIMAL > OMNIVORE > Pig")

class Raccoon(Omnivore):
    def hierarchy(self):
        print("ANIMAL > CARNIVORE > RACCOON")

if __name__ == '__main__':
    s = Shape()
    s.info()
    print("-----------------------------1.LINE-----------------------------")
    l = Line()
    l.info()
    print("-----------------------------2.CIRCLE-----------------------------")
    c = Circle()
    c.info()
    c.ar()
    print("-----------------------------3.TRIANGLE-----------------------------")
    t = Triangle()
    t.info()
    t.angle()
    print("-----------------------------4.QUADRILATERAL-----------------------------")
    q = Quadrilateral()
    q.info()
    q.angle()
    print("-----------------------------5.PENTAGON-----------------------------")
    p = Pentagon()
    p.info()
    p.angle()
    print("-----------------------------6.HEXAGON-----------------------------")
    h = Hexagon()
    h.info()
    h.angle()
    print("-----------------------------7.HEPTAGON-----------------------------")
    hp = Heptagon()
    hp.info()
    hp.angle()
    print("-----------------------------8.OCTAGON-----------------------------")
    o = Octagon()
    o.info()
    o.angle()
    print("-----------------------------9.NANOGON-----------------------------")
    n = Nanogon()
    n.info()
    n.angle()
    print("-----------------------------10.DECAGON-----------------------------")
    d = Decagon()
    d.info()
    d.angle()

    a = Animal()
    a.info()
    print("-----------------------------1.HORSE-----------------------------")
    ho = Horse()
    ho.info()
    ho.hierarchy()
    print("-----------------------------2.RABBIT-----------------------------")
    r = Rabbit()
    r.info()
    r.hierarchy()
    print("-----------------------------3.COW-----------------------------")
    cw = Cow()
    cw.info()
    cw.hierarchy()
    print("-----------------------------4.DEER-----------------------------")
    dr = Deer()
    dr.info()
    dr.hierarchy()
    print("-----------------------------5.FROG-----------------------------")
    fg = Frog()
    fg.info()
    fg.hierarchy()
    print("-----------------------------6.LION-----------------------------")
    lo = Lion()
    lo.info()
    lo.hierarchy()
    print("-----------------------------7.TIGER-----------------------------")
    t = Tiger()
    t.info()
    t.hierarchy()
    print("-----------------------------8.EAGLE-----------------------------")
    e = Eagle()
    e.info()
    e.hierarchy()
    print("-----------------------------9.PIG-----------------------------")
    pg = Pig()
    pg.info()
    pg.hierarchy()
    print("-----------------------------10.RACCOON-----------------------------")
    rc = Raccoon()
    rc.info()
    rc.hierarchy()

