from abc import ABC, abstractmethod

from ..domain.interfaces import Inventorizable, EnergyConsumer


class InspectionRule(ABC):
    """Правило принятия устройства в парк"""

    @abstractmethod
    def accepts(self, device: Inventorizable) -> bool:
        """Решить, принять ли устройство"""
        ...


class SimpleRule(InspectionRule):
    """Простое правило: инвентарный номер начинается с INV-"""

    def accepts(self, device: Inventorizable) -> bool:
        return device.inventory_number().startswith("INV-")


class ServiceCenter:
    """Сервис техосмотра"""

    def __init__(self, rule: InspectionRule):
        self._rule = rule

    def inspect(self, device: Inventorizable) -> bool:
        """Провести техосмотр"""
        return self._rule.accepts(device)

class EnergyLimitRule(InspectionRule):
    """Не берём устройства с расходом больше 3 кВт·ч"""

    def accepts(self, device) -> bool:
        if isinstance(device, EnergyConsumer):
            return device.daily_energy() <= 3.0
        return True