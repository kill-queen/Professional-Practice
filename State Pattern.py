# State Pattern

# Context
class Context:
    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()

# State
class State:
    def handle(self):
        pass

# Concrete State
class ConcreteState(State):
    def handle(self):
        print("ConcreteState handles request")

# Client
state = ConcreteState()
context = Context(state)
context.request()
