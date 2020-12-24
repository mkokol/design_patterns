from src.facade import Facade


class App:
    @classmethod
    def run(cls):
        facade = Facade()
        facade.operate()


if __name__ == '__main__':
    app = App()
    app.run()
