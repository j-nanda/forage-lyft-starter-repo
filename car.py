from serviceable import Serviceable
from engine import Engine
from battery import Battery

class Car:
    def __init__(self, engineType, batteryType):
        self.engineType = Engine()
        self.batteryType = Battery()

    
    def needs_service(self):
        self.engineType.needs_service()
        self.batteryType.needs_service()
