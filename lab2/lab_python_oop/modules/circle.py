from .geometrical_figure import GeometricalFigure
from .color_figure import ColorFigure
from math import pi


class Circle(GeometricalFigure):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = ColorFigure(color)
        self.name = "Круг"

    def __repr__(self):
        return f"{self.name} c радиусом {self.radius}, цветом {self.color.color} и площадью {self.GetArea()})"

    def GetArea(self):
        return pi * self.radius ** 2