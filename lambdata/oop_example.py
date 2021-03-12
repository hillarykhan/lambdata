"""Object Oriented Programming Examples - Unit 3 Sprint 1 Module 2"""

import pandas as pd


class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]    # number of cells in df


class BareMinimumClass:
    pass


class Complex:
    def __init__(self, real_part, imag_part):
        """
        Constructor for complex numbers.
        Complex numbers have a real and imaginary part.
        """
        self.r = real_part
        self.i = imag_part

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return "({}, {})".format(self.r, self.i)


class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def receive_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes

    def is_popular(self):
        return self.upvotes > 100


class Animal:
    """General Representation of Animals"""
    def __init__(self, name, weight, diet_type):
        self.name = str(name),
        self.weight = float(weight),
        self.diet_type = diet_type

    def run(self):
        return "Vroom, Vroom, I go quick"

    def eat(self, food):
        return "Huge fan of that " + food


class Sloth(Animal):
    """General Representation of Sloth inherited from Animals"""
    def __init__(self, name, weight, diet_type, num_naps=104):
        super().__init__(name, weight, diet_type)
        self.num_naps = num_naps # not in parent class so should define here
    # above line super(), etc. replaces the three lines of code below
    #     self.name = str(name),
    #     self.weight = float(weight),
    #     self.diet_type = diet_type,

    def run(self):
        return "I am a slow guy"

    def eat(self):
        return "I LIKE LEAAVVESSS"

    def say_something(self):
        return "this is a sloth of typing"


if __name__ == '__main__':
    num1 = Complex(3, -5) # num1.r = 3, num1.i = -5
    num2 = Complex(2, 6) # num2.r = 2, num2.i = 6

    num1.add(num2)
    print("num1.r: {}, num1.i: {}".format(num1.r, num1.i))

    user1 = SocialMediaUser("John", "LA", 500)
    user2 = SocialMediaUser("Carl", "Mississippi")
    user3 = SocialMediaUser("George Washington", "Djibouti", 4000)
    user4 = SocialMediaUser("Carlos", "Argentina", 5)

    print(user1.is_popular())
    print(user2.is_popular())
    user2.receive_upvotes(101)
    print('received {} upvotes'.format(user2.upvotes))
    print(user2.is_popular())