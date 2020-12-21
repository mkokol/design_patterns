from src.abstraction import Composite, CompositeCollection


class Sentence(Composite):
    def __init__(self, message: str):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message

    def get_size(self):
        return len(self.message)

    def get_content(self):
        return self.message

    def print_size(self):
        print('Sentence size: {}'.format(self.get_size()))


class Paragraph(CompositeCollection):
    def print_size(self):
        print('Paragraph size: {}'.format(self.get_size()))

    def get_content(self):
        return '  ' + ' '.join([child.get_content() for child in self.get_children()])


class Page(CompositeCollection):
    def print_size(self):
        print('Paragraph size: {}'.format(self.get_size()))

    def get_content(self):
        return '\n'.join([child.get_content() for child in self.get_children()])
