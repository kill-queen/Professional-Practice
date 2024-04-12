# Prototype Pattern

import copy

# Prototype
class Prototype:
    def clone(self):
        pass


# Concrete Prototype
class Sheep(Prototype):
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def clone(self):
        return copy.deepcopy(self)


# Client
original_sheep = Sheep("Jolly", "Merino")
print("Original sheep:", original_sheep.name, original_sheep.category)

# Clone the original sheep
cloned_sheep = original_sheep.clone()
print("Cloned sheep:", cloned_sheep.name, cloned_sheep.category)
