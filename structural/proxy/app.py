from src.proxy import AbstractDocument, DocumentProxy


class App:
    @classmethod
    def run(cls):
        document: AbstractDocument = DocumentProxy()
        document.title()
        document.text()


if __name__ == '__main__':
    app = App()
    app.run()
