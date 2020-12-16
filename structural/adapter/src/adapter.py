from abc import ABC, abstractmethod

from src.document import Document


class Text(ABC):
    @abstractmethod
    def get_text(self):
        pass


class AdapterInheritance(Document, Text):
    def __init__(self, title, body):
        super().__init__()
        self.title = title
        self.body = body

    def get_text(self):
        return self.title + '\n' + self.body + '\n'


class AdapterComposition(Text):
    def __init__(self, title, body):
        self.document = Document()
        self.document.title = title
        self.document.body = body

    def get_text(self):
        return self.document.title + '\n' + self.document.body + '\n'
