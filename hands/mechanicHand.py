from fingers.fingerContract import FingerContract
from hands.abstractHand import AbstractHand
from hands.mechanicHandContract import MechanicHandContract


class MechanicHand(MechanicHandContract, AbstractHand):
    def getTouch(self) -> str:
        result = super().getTouch()
        return result + f"\n{self.getSide()} hand gacırdadı"
