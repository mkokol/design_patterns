from abc import ABC, abstractmethod
from typing import List


class Composite(ABC):
    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def print_size(self):
        pass

    @abstractmethod
    def get_content(self):
        pass

    def print_content(self):
        print(self.get_content())


class CompositeCollection(Composite, ABC):
    def __init__(self):
        self.__children: List[Composite] = []

    def add(self, child):
        self.__children.append(child)

    def remove(self, index: int):
        del self.__children[index]

    def get_children(self):
        return self.__children

    def get_size(self):
        return sum([child.get_size() for child in self.__children])
