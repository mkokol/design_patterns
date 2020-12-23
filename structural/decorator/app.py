from src.component import AbstractComponent, TextComponent
from src.decorator import BorderDecorator


class App:
    @classmethod
    def run(cls):
        component: AbstractComponent = BorderDecorator(
            TextComponent('Decorator Design Pattern.')
        )
        component.render()


if __name__ == '__main__':
    app = App()
    app.run()
