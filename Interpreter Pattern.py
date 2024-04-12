# Interpreter Pattern

# Context
class Context:
    pass

# Abstract Expression
class AbstractExpression:
    def interpret(self, context):
        pass

# Terminal Expression
class TerminalExpression(AbstractExpression):
    def interpret(self, context):
        print("Terminal expression interpreted")

# Nonterminal Expression
class NonterminalExpression(AbstractExpression):
    def interpret(self, context):
        print("Nonterminal expression interpreted")

# Client
context = Context()
terminal_expression = TerminalExpression()
nonterminal_expression = NonterminalExpression()
terminal_expression.interpret(context)
nonterminal_expression.interpret(context)
