from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    @abstractmethod
    def get_name(self):
        raise NotImplementedError


class ProductA1(AbstractProductA):
    def get_name(self):
        return 'Product Name A1'


class ProductA2(AbstractProductA):
    def get_name(self):
        return 'Product Name A2'
