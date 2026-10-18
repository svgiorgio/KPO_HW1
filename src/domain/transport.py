from abc import ABC, abstractmethod

from .interfaces import Inventorizable, EnergyConsumer


class Transport(Inventorizable, ABC):
    """Базовый класс для любого транспорта"""

    def __init__(self, inventory_number: str, novice_friendliness: int):
        self._inventory_number = inventory_number
        self._novice_friendliness = novice_friendliness

    def inventory_number(self) -> str:
        return self._inventory_number

    def novice_friendliness(self) -> int:
        """Оценка простоты для новичка (1–10)"""
        return self._novice_friendliness

    @abstractmethod
    def type_name(self) -> str:
        """Название типа транспорта"""
        ...


class Scooter(Transport, EnergyConsumer):
    """Самокат потребляет энергию"""

    def __init__(self, inventory_number: str, novice_friendliness: int,
                 daily_energy_kwh: float):
        super().__init__(inventory_number, novice_friendliness)
        self._daily_energy = daily_energy_kwh

    def daily_energy(self) -> float:
        return self._daily_energy

    def type_name(self) -> str:
        return "самокат"


class Bicycle(Transport):
    """Обычный велосипед не потребляет энергию"""

    def __init__(self, inventory_number: str, novice_friendliness: int):
        super().__init__(inventory_number, novice_friendliness)

    def type_name(self) -> str:
        return "велосипед"


class Ebike(Transport, EnergyConsumer):
    """Электровелосипед потребляет энергию"""

    def __init__(self, inventory_number: str, novice_friendliness: int,
                 daily_energy_kwh: float):
        super().__init__(inventory_number, novice_friendliness)
        self._daily_energy = daily_energy_kwh

    def daily_energy(self) -> float:
        return self._daily_energy

    def type_name(self) -> str:
        return "электровелосипед"