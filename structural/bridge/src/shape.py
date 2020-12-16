from abc import ABC, abstractmethod

from src.paint import AbstractPaint, CanvasPaint, PaintType, SVGPaint


class AbstractShapeCollection(ABC):
    @abstractmethod
    def draw_triangle(self):
        pass

    @abstractmethod
    def draw_square(self):
        pass


class ShapeCollection(AbstractShapeCollection):
    def __init__(self, paint_type):
        if paint_type == PaintType.SVG:
            self.paint: AbstractPaint = SVGPaint()
        elif paint_type == PaintType.CANVAS:
            self.paint: AbstractPaint = CanvasPaint()
        else:
            raise NotImplementedError(
                'Support fo type "{}" is not implemented yet.'.format(paint_type)
            )

    def draw_triangle(self):
        print('Draw Triangle:')
        self.paint.draw_line()
        self.paint.draw_line()
        self.paint.draw_line()
        print('')

    def draw_square(self):
        print('Draw Square:')
        self.paint.draw_line()
        self.paint.draw_line()
        self.paint.draw_line()
        self.paint.draw_line()
        print('')
