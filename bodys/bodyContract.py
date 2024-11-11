from arms.armContract import ArmContract
from heads.headContract import HeadContract
from legs.legContract import LegContract


class BodyContract:
    def getHead(self) -> HeadContract:
        pass

    def getArm(self) -> ArmContract:
        pass

    def getLeg(self) -> LegContract:
        pass
