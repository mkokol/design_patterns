from src.builder import AbstractBuilder, DocumentBuilder
from src.director import Director
from src.product import Document


class App:
    def __init__(self):
        builder: AbstractBuilder = DocumentBuilder()
        self.__director: Director = Director(builder)

    def run(self):
        document: Document = self.__director.construct()
        print(document)


if __name__ == '__main__':
    app = App()
    app.run()
