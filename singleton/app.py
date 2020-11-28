from src.singleton import Document


class App:
    @classmethod
    def run(cls):
        document1 = Document.get_instance()
        document1.title = 'Title 1'
        document1.body = 'Body 1'
        print('document1')
        print(document1)

        document2 = Document.get_instance()
        document2.title = 'Title 2'
        document2.body = 'Body 2'
        print('document2')
        print(document2)
        print('document1:')
        print(document1)


if __name__ == '__main__':
    app = App()
    app.run()
