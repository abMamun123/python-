

# # class Vehicle:
# #     def __init__(self, brand):
# #         self.brand = brand

# #     def display_brand(self):
# #         print("Brand:", self.brand)


# # class Car(Vehicle):
# #     def __init__(self, brand, model):
# #         super().__init__(brand)
# #         self.model = model

# #     def display_model(self):
# #         print("Model:", self.model)


# # class ElectricCar(Car):
# #     def __init__(self, brand, model, battery_capacity):
# #         super().__init__(brand, model)
# #         self.battery_capacity = battery_capacity

# #     def display_battery_capacity(self):
# #         print("Battery Capacity:", self.battery_capacity)


# # # Creating an instance of ElectricCar
# # my_car = ElectricCar("Tesla", "Model S", "100 kWh")

# # # Accessing methods from different levels of inheritance
# # my_car.display_brand()
# # my_car.display_model()
# # my_car.display_battery_capacity()

# # class Person:
# #     def __init__(self, name, age, height, weight) -> None:
# #         self.name = name
# #         self.age = age
# #         self.height = height
# #         self.weight = weight


# # class Cricketer(Person):
# #     def __init__(self, name, age, height, weight) -> None:
# #         super().__init__(name, age, height, weight)

# #     def __lt__(self, other):
# #         return self.age < other.age


# # Sakib = Cricketer('Sakib', 38, 68, 91)
# # Mushfiq = Cricketer('Mushfiq', 36, 55, 82)
# # Mustafiz = Cricketer('Mustafiz', 27, 69, 86)
# # Riyad = Cricketer('Riyad', 39, 72, 92)

# # youngest_player = min([Sakib,Mushfiq,Mustafiz,Riyad])
# # print(youngest_player.name) #Mustafiz

# N, M = map(int, input().split()) 

# A = list(map(int, input().split())) 

# frequency = {} 

# for num in A: 
#     frequency[num] = frequency.get(num, 0) + 1

# for num in range(1, M+1): 
#     print(frequency.get(num, 0))

 
class Calculator:
    def add(self, a, b):
        def helper(x, y):
            return x + y
        return helper(a, b)

calc = Calculator()
result = calc.add(3,5)
print(result)
