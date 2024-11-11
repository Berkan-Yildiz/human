from arms.armContract import ArmContract
from hands.handContract import HandContract


class AbstractArm(ArmContract):
    def __init__(self, side: str, hand: HandContract):
        self._side = side
        self._hand = hand
        self._hand.setArm(self)

    def getSide(self) -> str:
        return self._side

    def getHand(self) -> HandContract:
        return self._hand
