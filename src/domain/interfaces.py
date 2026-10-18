from abc import ABC, abstractmethod


class Inventorizable(ABC):
    """Объект, который имеет инвентарный номер"""
    @abstractmethod
    def inventory_number(self) -> str:
        ...

    @abstractmethod
    def type_name(self) -> str:
        """Вернуть название типа объекта."""
        ...

class EnergyConsumer(ABC):
    """Устройство, потребляющее энергию"""
    @abstractmethod
    def daily_energy(self) -> float:
        ...