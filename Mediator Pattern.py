# Mediator Pattern

# Mediator interface
class Mediator:
    def notify(self, colleague, event):
        pass

# Colleague interface
class Colleague:
    def __init__(self, mediator):
        self.mediator = mediator

    def notify(self, event):
        self.mediator.notify(self, event)

# Concrete Mediator
class ConcreteMediator(Mediator):
    def __init__(self):
        self.colleague1 = None
        self.colleague2 = None

    def set_colleague1(self, colleague):
        self.colleague1 = colleague

    def set_colleague2(self, colleague):
        self.colleague2 = colleague

    def notify(self, colleague, event):
        if colleague == self.colleague1:
            self.colleague2.notify(event)
        else:
            self.colleague1.notify(event)

# Concrete Colleague
class ConcreteColleague1(Colleague):
    def __init__(self, mediator):
        super().__init__(mediator)

    def do_something(self):
        print("Colleague1 does something")

# Concrete Colleague
class ConcreteColleague2(Colleague):
    def __init__(self, mediator):
        super().__init__(mediator)

    def do_something_else(self):
        print("Colleague2 does something else")

# Client
mediator = ConcreteMediator()
colleague1 = ConcreteColleague1(mediator)
colleague2 = ConcreteColleague2(mediator)
mediator.set_colleague1(colleague1)
mediator.set_colleague2(colleague2)
colleague1.do_something()
colleague2.do_something_else()
