from abc import ABC, abstractmethod

# 抽象产品接口
class AbstractProductA(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# 具体产品 A1
class ConcreteProductA1(AbstractProductA):
    def operation(self) -> str:
        return "ConcreteProductA1 operation"

# 具体产品 A2
class ConcreteProductA2(AbstractProductA):
    def operation(self) -> str:
        return "ConcreteProductA2 operation"

# 抽象产品接口
class AbstractProductB(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# 具体产品 B1
class ConcreteProductB1(AbstractProductB):
    def operation(self) -> str:
        return "ConcreteProductB1 operation"

# 具体产品 B2
class ConcreteProductB2(AbstractProductB):
    def operation(self) -> str:
        return "ConcreteProductB2 operation"

# 抽象工厂接口
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_A(self) -> AbstractProductA:
        pass
    
    @abstractmethod
    def create_product_B(self) -> AbstractProductB:
        pass

# 具体工厂 1
class ConcreteFactory1(AbstractFactory):
    def create_product_A(self) -> AbstractProductA:
        return ConcreteProductA1()
    
    def create_product_B(self) -> AbstractProductB:
        return ConcreteProductB1()

# 具体工厂 2
class ConcreteFactory2(AbstractFactory):
    def create_product_A(self) -> AbstractProductA:
        return ConcreteProductA2()
    
    def create_product_B(self) -> AbstractProductB:
        return ConcreteProductB2()

# 客户端代码
def client_code(factory: AbstractFactory) -> None:
    product_A = factory.create_product_A()
    product_B = factory.create_product_B()
    print(product_A.operation())
    print(product_B.operation())

# 使用
if __name__ == "__main__":
    client_code(ConcreteFactory1())
    client_code(ConcreteFactory2())
