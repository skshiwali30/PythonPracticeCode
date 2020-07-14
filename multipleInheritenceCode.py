class Shape:
    def showDetails1(self):
        print("This is of round shape")

class Color:
    def showDetails2(self):
        print("This is Orange in color")

class Thing(Shape, Color):
    def showDetails3(self):
        print("This is Orange")

t = Thing()
t.showDetails1()
t.showDetails2()
t.showDetails3()