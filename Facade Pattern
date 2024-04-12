# Facade Pattern

# Subsystem A
class SubsystemA:
    def operation_a(self):
        print("Subsystem A operation")

# Subsystem B
class SubsystemB:
    def operation_b(self):
        print("Subsystem B operation")

# Facade
class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()

    def operation(self):
        self.subsystem_a.operation_a()
        self.subsystem_b.operation_b()

# Client
facade = Facade()
facade.operation()
