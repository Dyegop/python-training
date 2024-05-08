# Exercise 1: Fill in the Line class methods to accept coordinates as a pair of tuples and return
# the slope and distance of the line.
import math


class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt(
            abs((self.coor2[0] - self.coor1[0]) ** 2 + (self.coor2[1] - self.coor1[1]) ** 2)
        )

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])

li = Line([8, 2], [10, 9])
li2 = li.distance()
print(li2)
print(li.coor1)


class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return (math.pi * self.radius ** 2) * self.height

    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + (math.pi * self.radius ** 2) * 2

c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for _ in range(no_of_sides)]
        self.name = "name"

    def inputSides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


# For this challenge, create a bank account class that has two attributes: owner and balance
# Two methods: deposit and withdraw
# As an added requirement, withdrawals may not exceed the available balance

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @staticmethod
    def deposit(income):
        print(f"Deposit of {income}accepted")

    def withdraw(self, outcome):
        if outcome > self.balance:
            print(f"Withdraw of {outcome} not accepted")
        else:
            print(f"Withdraw of {outcome} accepted")

    def __str__(self):
        return f"Owner {self.owner} \nBalance {self.balance}"


acct1 = BankAccount("José", 1000)
print(acct1)
acct1.deposit(100)
acct1.withdraw(200)
acct1.withdraw(1200)
