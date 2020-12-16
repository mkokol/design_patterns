from abc import ABC, abstractmethod
from enum import Enum


class PaintType(str, Enum):
    SVG = 'svg'
    CANVAS = 'canvas'


class AbstractPaint(ABC):
    @abstractmethod
    def draw_line(self):
        pass


class SVGPaint(AbstractPaint):
    def draw_line(self):
        print('Draw line in SVG')


class CanvasPaint(AbstractPaint):
    def draw_line(self):
        print('Draw line in Canvas')
