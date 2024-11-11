from fingers.fingerContract import FingerContract


class FootContract:
    def getFinger(self) -> FingerContract:
        pass

    def getSide(self) -> str:
        pass

    def getTakeStep(self) -> str:
        pass

    def setLeg(self, leg) -> None:
        pass

    def getTouch(self):
        pass
