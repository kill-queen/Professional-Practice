class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# 使用示例
instance1 = Singleton()
instance2 = Singleton()

print(instance1 == instance2)  # 输出：True
