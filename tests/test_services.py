from src.domain.transport import Scooter, Bicycle, Ebike
from src.domain.item import Helmet, ChargingStation
from src.services.fleet import Fleet
from src.services.service_center import ServiceCenter, EnergyLimitRule


def test_inspection_accepts():
    rule = EnergyLimitRule()
    sc = ServiceCenter(rule)
    # энергия 1.5 <= 3, должен принять
    assert sc.inspect(Scooter("1", 7, 1.5)) is True
    # шлем не потребляет энергию, всегда ок
    assert sc.inspect(Helmet("2")) is True


def test_inspection_rejects():
    rule = EnergyLimitRule()
    sc = ServiceCenter(rule)
    # энергия 5 > 3, должен отклонить
    assert sc.inspect(Scooter("3", 8, 5.0)) is False


def test_fleet_total_energy():
    fleet = Fleet()
    fleet.add(Scooter("1", 7, 1.5))
    fleet.add(Bicycle("2", 9))
    fleet.add(Helmet("3"))
    fleet.add(ChargingStation("4", 0.5))
    assert fleet.total_daily_energy() == 2.0


def test_fleet_novice_devices():
    fleet = Fleet()
    fleet.add(Scooter("1", 7, 1.5)) # 7 >= 6, попадет
    fleet.add(Bicycle("2", 5)) # 5 < 6, не попадет
    fleet.add(Ebike("3", 6, 2.0)) # 6 >= 6, попадет
    fleet.add(Helmet("4")) # не транспорт, не попадет

    novice = fleet.novice_devices()
    assert len(novice) == 2
    assert novice[0].inventory_number() == "1"
    assert novice[1].inventory_number() == "3"