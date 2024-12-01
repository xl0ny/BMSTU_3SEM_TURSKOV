class ColorFigure:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @color.deleter
    def color(self):
        self._color = None

