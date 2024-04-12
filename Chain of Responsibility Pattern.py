# Chain of Responsibility Pattern

# Handler interface
class Handler:
    def set_next(self, handler):
        pass

    def handle_request(self, request):
        pass

# Concrete Handler
class ConcreteHandler(Handler):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def handle_request(self, request):
        if self.next_handler:
            self.next_handler.handle_request(request)

# Client
handler1 = ConcreteHandler()
handler2 = ConcreteHandler()
handler1.set_next(handler2)
handler1.handle_request("request")
