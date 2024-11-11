from heads.ears.earContract import EarContract
from heads.eyes.eyeContract import EyeContract
from heads.hair.hairContract import HairContract
from heads.headContract import HeadContract
from heads.mouth.mouthContract import MouthContract
from heads.nose.noseContract import NoseContract


class AbstractHead(HeadContract):
    def __init__(self, ear: EarContract, eye: EyeContract,
                 hair: HairContract, mouth: MouthContract, nose: NoseContract):
        self._ear = ear
        self._eye = eye
        self._hair = hair
        self._mouth = mouth
        self._nose = nose

    def getEar(self) -> EarContract:
        return self._ear

    def getEye(self) -> EyeContract:
        return self._eye

    def getHair(self) -> HairContract:
        return self._hair

    def getMouth(self) -> MouthContract:
        return self._mouth

    def getNose(self) -> NoseContract:
        return self._nose
