
# class Person:
#     def __init__(self, name, age, height, weight) -> None:
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight


# class Cricketer(Person):
#     def __init__(self, name, age, height, weight) -> None:
#         super().__init__(name, age, height, weight)

#     operator overloading..................
#     def __gt__(self, other):
#         print(self.age,other.age)
#         return self.age > other.age


# sakib = Cricketer('Sakib', 38, 68, 91)
# musfiq = Cricketer('Rahim', 36, 68, 88)
# kamal = Cricketer('Kamal', 39, 68, 94)
# jack = Cricketer('Jack', 38, 68, 91)
# kalam = Cricketer('Kalam', 37, 68, 95)
# # print(sakib>musfiq)
# oldest_player = max([sakib, musfiq,kamal,jack,kalam])
# print("oldest player:", oldest_player.name)

# method overriding........
class Add:
    def result(self, x, y):
        print("addition:", x+y)


class Mul(Add):
    def result(self, x, y):
        super().result(x, y)  # calling parent class method
        print("multi:", x*y)


# a = Add()
# a.result(5,8)
m = Mul()
m.result(3, 5)
