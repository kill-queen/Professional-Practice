# Composite Pattern

# Component interface
class Component:
    def operation(self):
        pass

# Leaf
class Leaf(Component):
    def operation(self):
        print("Leaf operation")

# Composite
class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        print("Composite operation")
        for child in self.children:
            child.operation()

# Client
leaf1 = Leaf()
leaf2 = Leaf()
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)
composite.operation()
