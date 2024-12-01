from .rectangle import Rectangle
from .color_figure import ColorFigure


class Square(Rectangle):
    def __init__(self, side, color):
        self.side = side
        self.color = ColorFigure(color)
        self.name = "Квадрат"

    def __repr__(self):
        return f"{self.name} cо стороной {self.side}, цветом {self.color.color} и площадью {self.GetArea()})"

    def GetArea(self):
        return self.side ** 2
