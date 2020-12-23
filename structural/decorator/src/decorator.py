from abc import ABC

from src.component import AbstractComponent


class AbstractDecorator(AbstractComponent, ABC):
    def __init__(self, instance: AbstractComponent):
        self.instance = instance

    @property
    def instance(self) -> AbstractComponent:
        return self.__instance

    @instance.setter
    def instance(self, value: AbstractComponent):
        self.__instance = value


class BorderDecorator(AbstractDecorator):
    def render(self):
        print('-' * self.get_size())
        print('| ', end='')
        self.instance.render()
        print(' |')
        print('-' * self.get_size())

    def get_size(self):
        return self.instance.get_size() + 4
