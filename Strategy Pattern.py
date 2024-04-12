# Strategy Pattern

# Strategy
class Strategy:
    def algorithm(self):
        pass

# Concrete Strategy
class ConcreteStrategy(Strategy):
    def algorithm(self):
        print("ConcreteStrategy algorithm")

# Context
class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def context_algorithm(self):
        self._strategy.algorithm()

# Client
strategy = ConcreteStrategy()
context = Context(strategy)
context.context_algorithm()
