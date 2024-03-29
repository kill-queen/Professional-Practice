def main():
    # 单例模式示例
    singleton1 = Singleton()
    singleton2 = Singleton()
    print("Is singleton1 the same instance as singleton2?", singleton1 is singleton2)

    # 工厂模式示例
    factory_a = ConcreteFactoryA()
    product_a = factory_a.create_product()
    product_a.operation()

    # 观察者模式示例
    subject = Subject()
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()
    subject.add_observer(observer_a)
    subject.add_observer(observer_b)
    subject.notify_observers("Hello observers!")

    # 装饰器模式示例
    operation()

if __name__ == "__main__":
    main()
