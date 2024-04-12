# Decorator Pattern

# Component interface
class Component:
    def operation(self):
        pass

# Concrete Component
class ConcreteComponent(Component):
    def operation(self):
        print("ConcreteComponent operation")

# Decorator
class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        self.component.operation()

# Concrete Decorator
class ConcreteDecorator(Decorator):
    def operation(self):
        super().operation()
        self.added_behavior()

    def added_behavior(self):
        print("Added behavior")

# Client
component = ConcreteComponent()
decorator = ConcreteDecorator(component)
decorator.operation()
