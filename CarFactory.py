from car import Car
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from engine.model import calliope, glissade, palindrome, rorschach, thovex
from battery.battery import SpindlerBattery, NubbinBattery

class CarFactory:
    @staticmethod
    def create_calliope(current_date: int, last_service_date: int, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return calliope(engine, battery)

    @staticmethod
    def create_glissade(current_date: int, last_service_date: int, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return glissade(engine, battery)

    @staticmethod
    def create_palindrome(current_date: int, last_service_date: int, warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return palindrome(engine, battery)

    @staticmethod
    def create_rorschach(current_date: int, last_service_date: int, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return rorschach(engine, battery)

    @staticmethod
    def create_thovex(current_date: int, last_service_date: int, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return thovex(engine, battery)