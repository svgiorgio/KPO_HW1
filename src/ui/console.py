from src.domain.transport import Scooter, Bicycle, Ebike
from src.domain.item import Helmet, ChargingStation, Dock
from src.services.service_center import ServiceCenter
from src.services.fleet import Fleet


class ConsoleApp:
    """Демонстрация сценариев работы парка"""

    def __init__(self, fleet: Fleet, service_center: ServiceCenter):
        self._fleet = fleet
        self._service_center = service_center

    def _try_add(self, device):
        """Попытка добавления с прохождением техосмотра"""
        if self._service_center.inspect(device):
            self._fleet.add(device)
            print(f"принято: {device.type_name()} {device.inventory_number()}")
        else:
            print(f"отклонено: {device.type_name()} {device.inventory_number()}")

    def run(self):
        print("парк ВышКат\n")

        print("добавление техники:")
        self._try_add(Scooter("1", 7, 1.5))
        self._try_add(Bicycle("2", 9))
        self._try_add(Ebike("3", 6, 2.0))
        self._try_add(Helmet("4"))
        self._try_add(ChargingStation("5", 0.5))
        self._try_add(Dock("6", 0.2))
        self._try_add(Scooter("7", 8, 5.0))  # слишком прожорлив

        print(f"\nсуточное потребление: {self._fleet.total_daily_energy()} кВт·ч")

        print("\nдля новичков:")
        for device in self._fleet.novice_devices():
            print(f" {device.type_name()} {device.inventory_number()}")

        print("\nвесь парк:")
        for device in self._fleet.all():
            print(f" {device.type_name()} {device.inventory_number()}")