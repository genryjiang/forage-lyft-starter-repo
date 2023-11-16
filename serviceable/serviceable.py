# New abstract class serviceable that the car class will implement
from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass
