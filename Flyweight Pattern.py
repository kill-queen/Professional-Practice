# Flyweight Pattern

# Flyweight Factory
class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, key):
        if key not in self.flyweights:
            self.flyweights[key] = ConcreteFlyweight()
        return self.flyweights[key]

# Flyweight
class Flyweight:
    def operation(self, extrinsic_state):
        pass

# Concrete Flyweight
class ConcreteFlyweight(Flyweight):
    def operation(self, extrinsic_state):
        print("ConcreteFlyweight operation with extrinsic state:", extrinsic_state)

# Client
factory = FlyweightFactory()
flyweight = factory.get_flyweight("key")
flyweight.operation("extrinsic state")
