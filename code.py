import time
import board
import pwmio
import rotaryio
from adafruit_motor import motor
import Encoder as enc
from simple_pid import PID
import encodedMotor as em

# Motor Right
encR = enc.encoder(a=board.GP26, b=board.GP27, ticks=144)
mR = em.EncodedMotor(encR, board.GP8, board.GP9, "Motor Right", False)

# Motor Left
encL = enc.encoder(a=board.GP16, b=board.GP17, ticks=144)
mL = em.EncodedMotor(encL, board.GP10, board.GP11, "Motor Left", True)

mL.setEffort(1)
mR.setEffort(1)

turns = 4
straight = 5
rotationsToTurn = .78
while turns > 0:
    print(turns)
    turns -= 1

    ## Straight
    while ((mL.getPos() + mR.getPos())/2) < straight:
        if mL.getPos() > mR.getPos():
            mL.setEffort(0)
            mR.setEffort(1)
        else:
            mL.setEffort(1)
            mR.setEffort(0)
    mL.setPos()
    mR.setPos()

    ## Turn
    while ((- mL.getPos() + mR.getPos())/2) < rotationsToTurn:
        if -mL.getPos() > mR.getPos():
            mL.setEffort(0)
            mR.setEffort(1)
        else:
            mL.setEffort(-1)
            mR.setEffort(0)
    mL.setPos()
    mR.setPos()
