# Command Pattern

# Command interface
class Command:
    def execute(self):
        pass

# Receiver
class Receiver:
    def action(self):
        print("Receiver action")

# Concrete Command
class ConcreteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.action()

# Invoker
class Invoker:
    def __init__(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()

# Client
receiver = Receiver()
command = ConcreteCommand(receiver)
invoker = Invoker(command)
invoker.invoke()
