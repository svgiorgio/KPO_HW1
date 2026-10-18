import pytest

from src.domain.transport import Scooter, Bicycle, Ebike, Transport
from src.domain.item import Helmet, ChargingStation, Dock, Item
from src.domain.interfaces import EnergyConsumer


def test_scooter():
    scooter = Scooter("1", 7, 1.5)
    assert scooter.type_name() == "самокат"
    assert scooter.inventory_number() == "1"
    assert scooter.novice_friendliness() == 7
    assert scooter.daily_energy() == 1.5
    assert isinstance(scooter, EnergyConsumer)


def test_bicycle():
    bike = Bicycle("2", 9)
    assert bike.type_name() == "велосипед"
    assert bike.inventory_number() == "2"
    assert bike.novice_friendliness() == 9
    assert not isinstance(bike, EnergyConsumer)


def test_ebike():
    ebike = Ebike("3", 6, 2.0)
    assert ebike.type_name() == "электровелосипед"
    assert ebike.daily_energy() == 2.0
    assert isinstance(ebike, EnergyConsumer)


def test_helmet():
    helmet = Helmet("4")
    assert helmet.type_name() == "шлем"
    assert helmet.inventory_number() == "4"
    assert not isinstance(helmet, EnergyConsumer)


def test_charging_station():
    station = ChargingStation("5", 0.5)
    assert station.type_name() == "зарядная станция"
    assert station.daily_energy() == 0.5
    assert isinstance(station, EnergyConsumer)


def test_dock():
    dock = Dock("6", 0.2)
    assert dock.type_name() == "док-станция"
    assert dock.daily_energy() == 0.2
    assert isinstance(dock, EnergyConsumer)


def test_abstract_classes():
    with pytest.raises(TypeError):
        Transport("7", 5)
    with pytest.raises(TypeError):
        Item("8")