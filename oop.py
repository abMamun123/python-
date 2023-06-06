# class Car:
#     wheals = 5
#     def __init__(self):
#         self.mile = 10
#         self.com = 'bmw'

# c1 = Car()
# c2 = Car()
# c1.com = 'totyota'
# # c1.wheals = 4
# Car.wheals = 22
# print(c1.com,c1.mile,c1.wheals)
# print(c2.com,c2.mile,c2.wheals)

from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("in laptop class")
# com = Computer() can't create obj in abstruct class
com1 = Laptop()
com1.process()   