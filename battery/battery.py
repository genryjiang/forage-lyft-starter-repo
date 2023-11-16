from abc import ABC, abstractmethod

from serviceable.serviceable import Serviceable


class Battery(Serviceable, ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass