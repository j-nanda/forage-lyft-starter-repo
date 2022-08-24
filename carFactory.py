from datetime import datetime
from car import Car
from capuletEngine import CapuletEngine
from model.engine import Engine
from nubbinBattery import NubbinBattery
from spindlerBattery import SpindlerBattery
from sternmanEngine import SternmanEngine
from willoughbyEngine import WilloughbyEngine

class CarFactory:
    def __init__(self):
        pass

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine1 = CapuletEngine(current_mileage, last_service_mileage)
        self.battery1 = SpindlerBattery(last_service_date, current_date)
        self.car1 = Car(self.engine1, self.battery1)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine2 = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery2 = SpindlerBattery(last_service_date, current_date)
        self.car2 = Car(self.engine2, self.battery2)

    def create_palindrome(self, current_date, last_service_date, warning_light_is_on):
        self.engine3 = SternmanEngine(warning_light_is_on)
        self.battery3 = SpindlerBattery(last_service_date, current_date)
        self.car3 = Car(self.engine3, self.battery3)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine4 = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery4 = NubbinBattery(last_service_date, current_date)
        self.car4 = Car(self.engine4, self.battery4)

    def thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine5 = CapuletEngine(current_mileage, last_service_mileage)
        self.battery5 = NubbinBattery(last_service_date, current_date)



