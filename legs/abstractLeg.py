from foots.footContract import FootContract
from legs.legContract import LegContract


class AbstractLeg(LegContract):
    def __init__(self, side: str, foot: FootContract):
        self._side = side
        self._foot = foot
        self._foot.setLeg(self)

    def getSide(self) -> str:
        return self._side

    def getFoot(self) -> FootContract:
        return self._foot
