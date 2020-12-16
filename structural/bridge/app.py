import argparse

from src.paint import PaintType
from src.shape import AbstractShapeCollection, ShapeCollection


class App:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--type', '-t',
            required=True,
            help='svg and canvas product type are available.',
            choices=[PaintType.SVG, PaintType.CANVAS]
        )
        self.args = parser.parse_args()
        self.shape_collection: AbstractShapeCollection = ShapeCollection(self.args.type)

    def run(self):
        self.shape_collection.draw_triangle()
        self.shape_collection.draw_square()


if __name__ == '__main__':
    app = App()
    app.run()
