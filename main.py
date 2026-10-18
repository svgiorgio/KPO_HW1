from src.di.container import Container
from src.services.fleet import Fleet
from src.services.service_center import ServiceCenter, EnergyLimitRule
from src.ui.console import ConsoleApp


def main():
    container = Container()
    container.register(Fleet, lambda: Fleet())
    container.register(ServiceCenter, lambda: ServiceCenter(EnergyLimitRule()))
    container.register(
        ConsoleApp,
        lambda: ConsoleApp(
            fleet=container.resolve(Fleet),
            service_center=container.resolve(ServiceCenter)
        )
    )

    app = container.resolve(ConsoleApp)
    app.run()


if __name__ == "__main__":
    main()