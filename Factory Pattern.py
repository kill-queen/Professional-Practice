from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class ShapeFactory:
    def get_shape(self, shape_type):
        if shape_type == "Circle":
            return Circle()
        elif shape_type == "Rectangle":
            return Rectangle()

# 使用示例
factory = ShapeFactory()
circle = factory.get_shape("Circle")
rectangle = factory.get_shape("Rectangle")
circle.draw()  # 输出：Drawing a circle
rectangle.draw()  # 输出：Drawing a rectangle
