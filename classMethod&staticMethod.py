# class method.......
class Car:
    base_price = 100000  # class variable

    def __init__(self, windows, door, power) -> None:
        self.windows = windows
        self.door = door
        self.power = power

    def what_base_price(self):
        print(f'base price:{self.base_price}')

    @classmethod
    def revise_base_price(cls, inflation):
        cls.base_price = cls.base_price + cls.base_price*inflation

    #intance method
    def instance_method(self):
        print(f'door:{self.door} window:{self.windows}')

    @staticmethod
    def my_static_method(arg1, arg2):
        # Perform some operations using the passed arguments
        result = arg1 + arg2
        print(result)

c1 = Car(2,3,2000)
#call class metod.........
# c1.what_base_price()
# Car.revise_base_price(.10)
# c1.what_base_price()
# c2 = Car(2,3,2000)
# c2.what_base_price()

#call static method.................
# Car.my_static_method(4,8)
c1.my_static_method(3,6)

#call instance method...........
# c1.instance_method()
#intance method can.t call using class name
#an intance must be created
# Car.instance_method()

