from abc import ABC, abstractmethod
from serviceable.serviceable import Serviceable
from car import Car

class baseEngine(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
    def needs_service():
        pass



