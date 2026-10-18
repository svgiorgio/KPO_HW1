from typing import List

from ..domain.interfaces import Inventorizable, EnergyConsumer


class Fleet:
    """Парк транспорта и вещей"""

    def __init__(self):
        self._items: List[Inventorizable] = []

    def add(self, device: Inventorizable) -> None:
        """Добавить устройство в парк"""
        self._items.append(device)

    def all(self) -> List[Inventorizable]:
        """Вернуть все устройства парка"""
        return list(self._items)

    def total_daily_energy(self) -> float:
        """Суммарное суточное потребление энергии"""
        total = 0.0
        for device in self._items:
            if isinstance(device, EnergyConsumer):
                total += device.daily_energy()
        return total

    def novice_devices(self) -> List[Inventorizable]:
        """Устройства, подходящие новичкам (простота >= 6)"""
        result = []
        for device in self._items:
            if hasattr(device, "novice_friendliness"):
                if device.novice_friendliness() >= 6:
                    result.append(device)
        return result