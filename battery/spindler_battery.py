from battery import Battery

class SpindlerBattery(Battery):
    SERVICE_LIFE_DAYS = 2 * 365  # 3 years expressed in days

    def __init__(self, last_service_date: int, current_date: int):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return self.current_date - self.last_service_date > SpindlerBattery.SERVICE_LIFE_DAYS