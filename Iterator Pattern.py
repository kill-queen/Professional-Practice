# Iterator Pattern

# Iterator interface
class Iterator:
    def has_next(self):
        pass

    def next(self):
        pass

# Concrete Iterator
class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection)

    def next(self):
        if self.has_next():
            value = self.collection[self.index]
            self.index += 1
            return value

# Aggregate interface
class Aggregate:
    def create_iterator(self):
        pass

# Concrete Aggregate
class ConcreteAggregate(Aggregate):
    def __init__(self):
        self.collection = []

    def add_item(self, item):
        self.collection.append(item)

    def create_iterator(self):
        return ConcreteIterator(self.collection)

# Client
aggregate = ConcreteAggregate()
aggregate.add_item("item1")
aggregate.add_item("item2")
iterator = aggregate.create_iterator()
while iterator.has_next():
    print(iterator.next())
