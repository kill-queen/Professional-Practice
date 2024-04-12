# Template Method Pattern

# Abstract Class
class AbstractClass:
    def template_method(self):
        self.base_operation1()
        self.required_operation()
        self.base_operation2()

    def required_operation(self):
        pass

    def base_operation1(self):
        print("AbstractClass: base_operation1")

    def base_operation2(self):
        print("AbstractClass: base_operation2")

# Concrete Class
class ConcreteClass(AbstractClass):
    def required_operation(self):
        print("ConcreteClass: required_operation")

# Client
concrete = ConcreteClass()
concrete.template_method()
