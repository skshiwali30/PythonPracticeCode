class Vehical:
    def __init__(self, color, cost):
        self.color = color
        self.cost = cost

    def showDetails(self):
        print("Vehical is cool")
        print("Color of vehical is", self.color)
        print("Cost of Vehical is", self.cost)

# v = Vehical("Purple",70000)
# v.showDetails()

# class Car(Vehical):
#     def showCarDetails(self):
#         print("I m a car...")
#
# c = Car("White", 90000)
# c.showCarDetails()
# c.showDetails()

class Car(Vehical):
    def __init__(self, color, cost, tyres):
        super().__init__(color, cost)
        self.tyres =tyres

    def showCarDetails(self):
        print("I m a car...")
        print("No of tyres", self.tyres)

c = Car("White", 90000, 4)
c.showCarDetails()
c.showDetails()