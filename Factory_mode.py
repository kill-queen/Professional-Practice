from abc import ABC, abstractmethod

# 产品接口
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

# 具体产品类A
class ConcreteProductA(Product):
    def operation(self):
        print("ConcreteProductA operation")

# 具体产品类B
class ConcreteProductB(Product):
    def operation(self):
        print("ConcreteProductB operation")

# 工厂接口
class Factory(ABC):
    @abstractmethod
    def create_product(self):
        pass

# 具体工厂类A
class ConcreteFactoryA(Factory):
    def create_product(self):
        return ConcreteProductA()

# 具体工厂类B
class ConcreteFactoryB(Factory):
    def create_product(self):
        return ConcreteProductB()

# 客户端代码
if __name__ == "__main__":
    factory_a = ConcreteFactoryA()
    product_a = factory_a.create_product()
    product_a.operation()

    factory_b = ConcreteFactoryB()
    product_b = factory_b.create_product()
    product_b.operation()
