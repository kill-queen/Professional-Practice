# Memento Pattern

# Memento
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

# Originator
class Originator:
    def __init__(self):
        self._state = ""

    def set_state(self, state):
        print(f"Setting state to: {state}")
        self._state = state

    def save_to_memento(self):
        print("Saving state to memento")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_state()
        print(f"Restoring state from memento: {self._state}")

# Caretaker
class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        print("Adding memento to caretaker")
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]

# Client
originator = Originator()
caretaker = Caretaker()

originator.set_state("State 1")
caretaker.add_memento(originator.save_to_memento())

originator.set_state("State 2")
caretaker.add_memento(originator.save_to_memento())

originator.restore_from_memento(caretaker.get_memento(0))
