from .geometrical_figure import GeometricalFigure
from .color_figure import ColorFigure


class Rectangle(GeometricalFigure):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = ColorFigure(color)
        self.name = "Прямоугольник"

    def __repr__(self):
        return f"{self.name} cо сторонами {self.width} * {self.height}, цветом {self.color.color} и площадью {self.GetArea()})"

    def GetArea(self):
        return self.width * self.height
