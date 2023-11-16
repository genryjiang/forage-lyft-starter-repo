from abc import ABC, abstractmethod
from engineBase import baseEngine
from battery.battery import Battery
from serviceable.serviceable import Serviceable


class Car(ABC):
    def __init__(self, last_service_date, baseEngine, Battery):
        self.last_service_date = last_service_date
        self.battery = Battery
        self.engine = baseEngine

    @abstractmethod
    def needs_service(self):
        pass
