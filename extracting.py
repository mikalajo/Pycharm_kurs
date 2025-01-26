# Extract Constant
def calc():
    a = 0
    b = 1
    c = 3
    result = a ** 2 + b ** 2 + c ** 2
    return result


# Extract field or variable
import math
class SolverEquation:
    def demo(self):
        a = 3
        b = 25
        c = 46
        root1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        root2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        print(root1, root2)


# Extract method
from enum import Enum


class Category(Enum):
    A = 1
    B = 2
    C = 3


def calculate_tax(category, income):
    if category == Category.A:
        discount = 10
    elif category == Category.B:
        discount = 5
    else:
        discount = 0
    return income * (100 - discount) / 100

calculate_tax(Category.A, 10000)
print("master")
# Extract Parameter
def print_hello():
    print("Hello World")


# Extract Superclass
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        return "Woof!"

    def info(self):
        return f"Name: {self.name}, Breed: {self.breed}"
