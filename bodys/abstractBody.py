from arms.armContract import ArmContract
from bodys.bodyContract import BodyContract
from heads.headContract import HeadContract
from legs.legContract import LegContract


class AbstractBody(BodyContract):
    def __init__(self, head: HeadContract, arm: ArmContract, leg: LegContract):
        self._head = head
        self._arm = arm
        self._leg = leg

    def getHead(self) -> HeadContract:
        return self._head

    def getArm(self) -> ArmContract:
        return self._arm

    def getLeg(self) -> LegContract:
        return self._leg
