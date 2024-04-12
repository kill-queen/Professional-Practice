# Adapter Pattern

# Target interface
class Target:
    def request(self):
        pass

# Adaptee
class Adaptee:
    def specific_request(self):
        print("Adaptee's specific request")

# Adapter
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.specific_request()

# Client
adaptee = Adaptee()
adapter = Adapter(adaptee)
adapter.request()
