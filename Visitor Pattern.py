# Visitor Pattern

# Visitor
class Visitor:
    def visit_concrete_element_a(self, element):
        pass

    def visit_concrete_element_b(self, element):
        pass

# Element
class Element:
    def accept(self, visitor):
        pass

# Concrete Element
class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

# Concrete Element
class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

# Concrete Visitor
class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element):
        print("ConcreteVisitor visits ConcreteElementA")

    def visit_concrete_element_b(self, element):
        print("ConcreteVisitor visits ConcreteElementB")

# Client
visitor = ConcreteVisitor()
element_a = ConcreteElementA()
element_b = ConcreteElementB()
element_a.accept(visitor)
element_b.accept(visitor)
