from arms.abstractArm import AbstractArm
from arms.mechanicArmContract import MechanicArmContract
from hands.handContract import HandContract


class MechanicArm(AbstractArm, MechanicArmContract):
    def __init__(self, side: str, hand: HandContract, armType: str):
        super().__init__(side, hand)
        self._armType = armType

    def getArmMaterial(self) -> str:
        return self._armType
