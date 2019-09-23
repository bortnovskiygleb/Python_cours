from math import pi


class Apple():
    def __init__(self):
        self.color = 'green'
        self.weight = 0
        self.form = 'circle'
        self.taste = 'sour'


class Circle():
    def __init__(self, r):
        self.rad = r

    def area(self):
        return pi * self.rad ** 2

circle = Circle(1)
# print(circle.area())


class Person():
    def __init__(self, f, s, q=1):
        self.firstname = f
        self.surname = s
        self.qualification = q

    def info(self):
        return "Firstname: {}, surname: {}, skill: {}".format(self.firstname,
                self.surname, self.qualification)

gleb = Person('Gleb', 'Bortnovskiy')
# print(gleb.info())


class Triangel():
    def __init__(self, h, a):
        self.hight = h
        self.side = a

    def area(self):
        return 0.5 * self.hight * self.side

tr = Triangel(4, 2)
# print(tr.area())


class Rectangle():
    def __init__(self, h, w):
        self.hight = h
        self.width = w

    def area(self):
        return self.hight * self.width


class Square():
    def __init__(self, a):
        self.side = a

    def area(self):
        return self.side ** 2

    def change_size(self, dif):
        self.side = self.side + dif

rec = Rectangle(11, 15)
sq = Square(23)
# print("Area:\n Rectangle: {}\n Square: {}".format(rec.area(), sq.area()))
# sq.change_size(-13)
# print("Area:\n Rectangle: {}\n Square: {}".format(rec.area(), sq.area()))
