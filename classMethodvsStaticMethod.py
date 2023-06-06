class MyClass:
    class_attribute = "Hello, Class!"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    @classmethod
    def class_method(cls):
        # Class methods can access class attributes
        # and perform operations involving the class
        # For example, creating a new instance
        # new_instance = cls("New Instance")
        # return new_instance
        cls.class_attribute = "hello, from method"
        print(cls.class_attribute)

    @staticmethod
    def static_method():
        # Static methods cannot access class attributes
        # They are self-contained and don't rely on instances or the class itself
        print("This is a static method")

    def instance_method(self):
        # Instance methods can access both instance attributes and class attributes
        print(self.instance_attribute)
        print(self.class_attribute)


new_obj = MyClass('testing')
new_obj.class_method()

