from heads.eyes.eyeContract import EyeContract


class AbstractEye(EyeContract):
    def __init__(self, color):
        self.color = color

    def getColor(self) -> str:
        return self.color
