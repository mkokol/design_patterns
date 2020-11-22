import argparse

from src.creator import AbstractCreator, Creator
from src.product import AbstractProduct


class App:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--type', '-t',
            required=True,
            help='a and b product type are available.',
            choices=['a', 'b']
        )
        self.args = parser.parse_args()
        self.creator: AbstractCreator = Creator()

    def run(self):
        product: AbstractProduct = self.creator.create(self.args.type)
        print(product.get_name())


if __name__ == '__main__':
    app = App()
    app.run()
