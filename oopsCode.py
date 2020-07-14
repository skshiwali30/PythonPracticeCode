class Mobile:

    def knowRating(self):
        print("3-star rating.")

    def knowBattery(self):
        print("3 days life for 1 time charging")

    def set_Color(self, color):
        self.color = color

    def show_Color(self):
        return self.color

mob = Mobile()
mob.knowBattery()
mob.knowRating()
mob.set_Color("blue")
print(mob.show_Color())

class Employee:

    def __init__(self, name, city, dob):
        self.name = name
        self.city = city
        self.dob = dob

    def description(self):
        print("Name of employee is", self.name)
        print("City of employee is", self.city)
        print("Dob of employee is", self.dob)


emp = Employee("Shiwali", "Noida", "30-01-1993")
emp.description()

