# 组件接口
class Component:
    def operation(self) -> str:
        pass

# 具体组件类
class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent: operation"

# 装饰器基类
class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    def operation(self) -> str:
        return self._component.operation()

# 具体装饰器类
class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA: operation + {self._component.operation()}"

# 具体装饰器类
class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB: operation + {self._component.operation()}"

# 使用示例
if __name__ == "__main__":
    # 创建一个具体组件对象
    component = ConcreteComponent()

    # 创建具体装饰器对象，并将具体组件对象作为参数传递给它
    decorator_a = ConcreteDecoratorA(component)
    decorator_b = ConcreteDecoratorB(component)

    # 调用装饰器对象的操作方法
    print(decorator_a.operation())
    print(decorator_b.operation())
