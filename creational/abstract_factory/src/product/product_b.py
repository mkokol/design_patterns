from abc import ABC, abstractmethod


class AbstractProductB(ABC):
    @abstractmethod
    def get_content(self):
        raise NotImplementedError


class ProductB1(AbstractProductB):
    def get_content(self):
        return 'Product Content B1'


class ProductB2(AbstractProductB):
    def get_content(self):
        return 'Product Content B2'
