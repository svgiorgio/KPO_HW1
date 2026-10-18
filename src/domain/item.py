from abc import ABC, abstractmethod

from .interfaces import Inventorizable, EnergyConsumer


class Item(Inventorizable, ABC):
    """Базовый класс для любой вещи на балансе"""

    def __init__(self, inventory_number: str):
        self._inventory_number = inventory_number

    def inventory_number(self) -> str:
        return self._inventory_number

    @abstractmethod
    def type_name(self) -> str:
        """Название типа вещи"""
        ...


class Helmet(Item):
    """Шлем не потребляет энергию"""

    def type_name(self) -> str:
        return "шлем"


class ChargingStation(Item, EnergyConsumer):
    """Зарядная станция потребляет энергию"""

    def __init__(self, inventory_number: str, daily_energy_kwh: float):
        super().__init__(inventory_number)
        self._daily_energy = daily_energy_kwh

    def daily_energy(self) -> float:
        return self._daily_energy

    def type_name(self) -> str:
        return "зарядная станция"


class Dock(Item, EnergyConsumer):
    """Док-станция потребляет энергию"""

    def __init__(self, inventory_number: str, daily_energy_kwh: float):
        super().__init__(inventory_number)
        self._daily_energy = daily_energy_kwh

    def daily_energy(self) -> float:
        return self._daily_energy

    def type_name(self) -> str:
        return "док-станция"