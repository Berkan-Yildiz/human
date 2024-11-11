from foots.footContract import FootContract
from legs.abstractLeg import AbstractLeg
from legs.mechanicLegContract import MechanicLegContract


class MechanicLeg(AbstractLeg, MechanicLegContract):
    def __init__(self, side: str, foot: FootContract, legType: str):
        super().__init__(side, foot)
        self._legType = legType

    def getLegMaterial(self) -> str:
        return self._legType
