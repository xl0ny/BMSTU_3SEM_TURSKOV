from abc import ABC, abstractmethod


class GeometricalFigure(ABC):
    @abstractmethod
    def GetArea(self):
        pass
    