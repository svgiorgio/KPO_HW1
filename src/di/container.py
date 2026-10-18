class Container:
    """Простой DI-контейнер"""

    def __init__(self):
        self._factories = {}

    def register(self, key, factory):
        """Зарегистрировать фабрику для типа"""
        self._factories[key] = factory

    def resolve(self, key):
        """Создать объект по типу"""
        if key not in self._factories:
            raise KeyError(f"Тип {key} не зарегистрирован")
        return self._factories[key]()