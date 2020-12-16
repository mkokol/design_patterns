from abc import ABC, abstractmethod
from typing import Optional

from src.product import Description, Document, Text, Title


class AbstractBuilder(ABC):
    @abstractmethod
    def build(self) -> Document:
        pass

    @abstractmethod
    def set_title(self, title: str):
        pass

    @abstractmethod
    def set_description(self, description: str):
        pass

    @abstractmethod
    def set_text(self, text: str):
        pass


class DocumentBuilder(AbstractBuilder):
    def __init__(self):
        self._document = Document()

        self.__title: Optional[str] = None
        self.__description: Optional[str] = None
        self.__text: Optional[str] = None

    def build(self) -> Document:
        if self.__title:
            self._document.title = Title(self.__title)

        if self.__description:
            self._document.description = Description(self.__description)

        if self.__text:
            self._document.text = Text(self.__text)

        return self._document

    def set_title(self, title: str):
        self.__title = title

        return self

    def set_description(self, description: str):
        self.__description = description

        return self

    def set_text(self, text: str):
        self.__text = text

        return self
