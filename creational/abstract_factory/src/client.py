from src.factory import AbstractFactory, ConcreteFactory1, ConcreteFactory2


class Client:
    def __init__(self, type: int):
        if type == 1:
            self.product_factory: AbstractFactory = ConcreteFactory1()
        elif type == 2:
            self.product_factory: AbstractFactory = ConcreteFactory2()
        else:
            raise Exception('Type {} is not supported'.format(type))

    def get_name(self):
        product_a = self.product_factory.create_product_a()

        return product_a.get_name()

    def get_content(self):
        product_a = self.product_factory.create_product_b()

        return product_a.get_content()
