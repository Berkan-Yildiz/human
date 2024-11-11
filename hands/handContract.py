from fingers.fingerContract import FingerContract


class HandContract:
    def getFinger(self) -> FingerContract:
        pass

    def getSide(self) -> str:
        pass

    def getTouch(self) -> str:
        pass

    def setArm(self, arm) -> None:
        pass
