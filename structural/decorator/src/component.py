from abc import ABC, abstractmethod


class AbstractComponent(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def get_size(self):
        pass


class TextComponent(AbstractComponent):
    def __init__(self, text):
        self.text = text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

    def render(self):
        print(self.text, end='')

    def get_size(self):
        return len(self.text)
