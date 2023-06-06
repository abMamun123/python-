from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self,name,food) -> None:
        self.animal_name = name
        self.animal_food = food

    @abstractmethod 
    def eat(self):
        print (f'{self.animal_name} eat {self.animal_food}')    

class Monkey(Animal):
    def __init__(self, name, food) -> None:
        super().__init__(name, food)
    def eat(self):
        return super().eat()

a = Monkey('moneky','banana')
a1 = Monkey('Tiger','meat')

a1.eat()        