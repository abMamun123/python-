# inheritance
class Person:
    def __init__(self, name) -> None:
        self.name = name

    def show_name(self):
        print(self.name)


class User(Person):
    pass

# c = User('abc')
# c.show_name()

# composition


class Person:
    def __init__(self, name) -> None:
        self.name = name

    def show_name(self):
        print(self.name)


class User:
    def __init__(self,name) -> None:
        self.obj1 = Person(name)

    def show_name(self):
        self.obj1.show_name()

c = User('abc')
c.show_name()