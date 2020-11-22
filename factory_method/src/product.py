from abc import ABC, abstractmethod
from enum import Enum


class AbstractProduct(ABC):
    @abstractmethod
    def get_name(self):
        pass


class ProductType(str, Enum):
    A = 'a'
    B = 'b'


class ProductA(AbstractProduct):
    def get_name(self):
        return 'Product A'


class ProductB(AbstractProduct):
    def get_name(self):
        return 'Product B'
