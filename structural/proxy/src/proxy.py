from abc import ABC, abstractmethod


class AbstractDocument(ABC):
    @abstractmethod
    def title(self):
        pass

    @abstractmethod
    def text(self):
        pass


class Document(AbstractDocument):
    def title(self):
        print('Document Title')

    def text(self):
        print('Document Text')


class DocumentProxy(AbstractDocument):
    def __init__(self):
        self._document = Document()

    def title(self):
        print('Proxy Title Message')
        self._document.title()

    def text(self):
        print('Proxy Text Message')
        self._document.text()
