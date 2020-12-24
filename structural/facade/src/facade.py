from src.service_a import ServiceA
from src.service_b import ServiceB


class Facade:
    def __init__(self):
        self.service_a = ServiceA()
        self.service_b = ServiceB()

    def operate(self):
        self.service_a.operation_x()
        self.service_b.operation_y()
        self.service_a.operation_z()
