"""
OBJECT ORIENTED PROGRAMMING NOTES

Concepts:
-Class: is a set of instructions for how to make an instance.
-Inheritance: attributes and methods from parent class can be used in child class.
-Attribute: variables that are accessible through instances.

Attribute’s value can be changed in three ways:
-Changing the value directly through an instance.
-Setting the value through a method.
-Incrementing the value (add a certain amount to it) through a method.

Attributes can take parameters required when you create an object or can be defined to take a value.
    self.attribute = parameter --> attribute is linked to a parameter with an attribute for the object.
    def __init__(self, name):
        self.name = name
    self.attribute = value --> we define a value for the attribute. For example:
    def __init__(self):
        self.name = "Dealer"

Self:
-Self is a reference to the instance itself.
-Every method call associated with an instance automatically passes self.
-It gives the individual instance access to the attributes and methods in the class
-Any variable prefixed with self is available to every method in the class.

Inheritance:
-Parent class must be part of the current file and must appear before the child class in the file.
-The name of the parent class must be included in parentheses in the definition of a child class.
-Super() function is a special function that allows you to call a method from the parent class.
-Methods in the parent class can be overridden
"""


import random

# CLASSES:
class Table:
    def __init__(self, hand, score=0, name="Dealer"):
        self.name = name
        self.hand = hand
        self.score = score

    def deal_card(self):
        deck = [('Ace', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8),
                ('9', 9), ('10', 10), ('Jack', 10), ('Queen', 10), ('King', 10)] * 4
        self.hand.append(random.choice(deck))

    # Method to calculate score.
    # Since Player inherits from Table, we can use this method for both dealer and player
    def calculate_score(self):
        self.score = sum(x[1] for x in self.hand)

    def __str__(self):
        # Override to print a readable string presentation of your object
        # below is a dynamic way of doing this without explicity constructing the string manually
        return self.name+"'s score: "+str(self.score)

class Player(Table):
    # Child class inherits construct and attributes from parent class
    # We can create an construct for the child class (optional). In this case, we need to add super()
    def __init__(self, name, funds, hand, score=0, bet=0):
        # super() allows us to access attributes from the construct of the parents class
        # In a way, super() is an alias for the parent classes
        super().__init__(hand, score)
        self.name = name
        self.funds = funds
        self.hand = hand
        self.score = score
        self.bet = bet

    def input_data(self):
        self.name = str(input("Please, type your name, sir: ")).capitalize()
        self.funds = int(input("Please, introduce your funds, sir: "))
        while self.funds <= 0:
            print("Funds can't be 0 or less")
            self.funds = int(input("Please, introduce your funds, sir: "))

        # If we want to select two different integers in one line, we can do as follows:
        # self.funds, self.bet = [int(x) for x in input("Please, introduce your funds and bet, sir: ").split()]

    def ace_choice(self):
        for i in self.hand:
            if i[0] == 'Ace':
                choice = int(input("Choose ace's score: "))
                if choice == 1:
                    pass
                elif choice == 11:
                    self.score += 10

class Game:
    def __init__(self, status=0):
        self.status = status
        # default status = 0, tie
        # player wins = 1, player loses = -1

    def victory_status(self, score_dealer, score_player):
        if score_player == 21:
            if score_dealer == 21:
                pass
            else:
                self.status = 1
        elif score_dealer < score_player < 21:
            self.status = 1
        else:
            self.status = -1

