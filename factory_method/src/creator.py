from abc import ABC, abstractmethod

from src.product import ProductA, ProductB, ProductType


class AbstractCreator(ABC):
    @abstractmethod
    def create(self, product_type: str):
        pass


class Creator(AbstractCreator):
    def create(self, product_type: str):
        if product_type == ProductType.A:
            return ProductA()
        elif product_type == ProductType.B:
            return ProductB()
        else:
            raise ValueError('Product type "{type}" is not supported'.format(type=product_type))
