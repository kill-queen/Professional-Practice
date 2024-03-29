# 观察者接口
class Observer:
    def update(self, message):
        pass

# 主题类
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

# 具体观察者类
class ConcreteObserver(Observer):
    def update(self, message):
        print("Received message:", message)

# 使用示例
if __name__ == "__main__":
    # 创建主题
    subject = Subject()

    # 创建观察者
    observer1 = ConcreteObserver()
    observer2 = ConcreteObserver()

    # 添加观察者到主题
    subject.attach(observer1)
    subject.attach(observer2)

    # 发送通知给观察者
    subject.notify("Hello, observers!")

    # 移除一个观察者
    subject.detach(observer2)

    # 再次发送通知给观察者
    subject.notify("Goodbye, observer2!")
