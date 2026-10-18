import pytest

from src.di.container import Container
from src.domain.transport import Scooter
from src.domain.item import Helmet
from src.services.fleet import Fleet
from src.services.service_center import ServiceCenter, InspectionRule

class FakeRule(InspectionRule):
    """тестовое правило: отклоняет всё"""
    def accepts(self, device) -> bool:
        return False


def test_container_register_and_resolve():
    c = Container()
    c.register(str, lambda: "тест")
    assert c.resolve(str) == "тест"


def test_container_unregistered():
    c = Container()
    with pytest.raises(KeyError):
        c.resolve(int)


def test_di_substitution():
    sc = ServiceCenter(FakeRule())
    fleet = Fleet()
    scooter = Scooter("1", 7, 1.5)
    helmet = Helmet("2")

    assert sc.inspect(scooter) is False
    assert sc.inspect(helmet) is False

    if sc.inspect(scooter):
        fleet.add(scooter)
    assert len(fleet.all()) == 0