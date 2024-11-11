from heads.ears.earContract import EarContract
from heads.eyes.eyeContract import EyeContract
from heads.hair.hairContract import HairContract
from heads.mouth.mouthContract import MouthContract
from heads.nose.noseContract import NoseContract


class HeadContract:
    def getEar(self) -> EarContract:
        pass

    def getEye(self) -> EyeContract:
        pass

    def getHair(self) -> HairContract:
        pass

    def getMouth(self) -> MouthContract:
        pass

    def getNose(self) -> NoseContract:
        pass
