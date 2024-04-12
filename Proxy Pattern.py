# Proxy Pattern

# Subject interface
class Subject:
    def request(self):
        pass

# Real Subject
class RealSubject(Subject):
    def request(self):
        print("RealSubject request")

# Proxy
class Proxy(Subject):
    def __init__(self):
        self.real_subject = RealSubject()

    def request(self):
        print("Proxy request")
        self.real_subject.request()

# Client
proxy = Proxy()
proxy.request()
