from fingers.fingerContract import FingerContract
from foots.footContract import FootContract


class AbstractFoot(FootContract):
    def __init__(self, finger: FingerContract):
        self._finger = finger
        self._leg = None

    def getFinger(self) -> FingerContract:
        return self._finger

    def setLeg(self, leg) -> None:
        self._leg = leg

    def getSide(self) -> str:
        return self._leg.getSide()

    def getTakeStep(self) -> str:
        return f"{self.getSide()} foot take a step"
