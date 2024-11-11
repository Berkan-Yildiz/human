from heads.hair.hairContract import HairContract


class AbstractHair(HairContract):
    def __init__(self, color, style):
        self._color = color
        self._style = style

    def getColor(self) -> str:
        return self._color

    def getStyle(self) -> str:
        return self._style
