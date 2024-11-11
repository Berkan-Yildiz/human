from arms.arm import Arm
from bodys.body import Body
from fingers.finger import Finger
from foots.foot import Foot
from hands.hand import Hand
from hands.mechanicHand import MechanicHand
from heads.ears.ear import Ear
from heads.eyes.eye import Eye
from heads.hair.hair import Hair
from heads.head import Head
from heads.mouth.mouth import Mouth
from heads.nose.nose import Nose
from legs.leg import Leg
from arms.mechanicArm import MechanicArm

finger = Finger()
hand = MechanicHand(finger)
arm = Arm("Left", hand)
mechanicArm = MechanicArm("Right", hand, "Touch Bionic")

foot = Foot(finger)
leg = Leg("Right", foot)

eye = Eye("Blue")
hair = Hair("Brown", "Curly")
ear = Ear()
mouth = Mouth()
nose = Nose()
head = Head(ear, eye, hair, mouth, nose)

body = Body(head, arm, leg)

print(f"Eye Color: {head.getEye().getColor()}")
print(f"Hair Color: {head.getHair().getColor()}")
print(f"Hair Style: {head.getHair().getStyle()}")

print(f"Hand Side: {hand.getSide()}")
print(f"Hand Touch: {hand.getTouch()}")

print(f"Leg Side: {leg.getSide()}")
print(f"Foot Touch: {leg.getFoot().getTouch()}")

print(hand.getTouch())
