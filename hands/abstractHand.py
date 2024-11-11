from fingers.fingerContract import FingerContract
from hands.handContract import HandContract


class AbstractHand(HandContract):
    def __init__(self, finger: FingerContract):
        self._finger = finger
        self._arm = None

    def getFinger(self) -> FingerContract:
        return self._finger

    def setArm(self, arm) -> None:
        self._arm = arm

    def getSide(self) -> str:
        return self._arm.getSide()

    def getTouch(self) -> str:
        return f"{self.getSide()} hand with finger touched"
