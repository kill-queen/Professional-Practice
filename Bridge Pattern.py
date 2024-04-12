# Bridge Pattern

# Implementor interface
class Implementor:
    def operation_implementation(self):
        pass

# Concrete Implementor A
class ConcreteImplementorA(Implementor):
    def operation_implementation(self):
        print("Concrete Implementor A operation implementation")

# Concrete Implementor B
class ConcreteImplementorB(Implementor):
    def operation_implementation(self):
        print("Concrete Implementor B operation implementation")

# Abstraction
class Abstraction:
    def __init__(self, implementor):
        self.implementor = implementor

    def operation(self):
        self.implementor.operation_implementation()

# Refined Abstraction
class RefinedAbstraction(Abstraction):
    pass

# Client
implementor_a = ConcreteImplementorA()
abstraction = Abstraction(implementor_a)
abstraction.operation()

implementor_b = ConcreteImplementorB()
refined_abstraction = RefinedAbstraction(implementor_b)
refined_abstraction.operation()
