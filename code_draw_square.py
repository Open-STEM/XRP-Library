import time
import board
import encoder as enc
import encoded_motor as em
import drive as drv

"""
    File meant to help student calibrate io.

    By the end of completing this file the student's robot should
    have both motors spinning forward and the encoders counting up.
"""

# Encoders
encL = enc.encoder(a=board.GP4, b=board.GP5, ticksPerRev=144, doFlip=False)
encR = enc.encoder(a=board.GP2, b=board.GP3, ticksPerRev=144, doFlip=True)

# Motors
mL = em.encoded_motor(encL, board.GP8, board.GP9, "Motor Left",     doFlip=True)
mR = em.encoded_motor(encR, board.GP10, board.GP11, "Motor Right",  doFlip=False)

# Drive Base
driveBase = drv.drive(mL, mR)

turns = 4
straight = 4
rotationsToTurn = .66

while turns > 0:
    print(turns)
    turns -= 1

    ## Straight
    while ((mL.getPos() + mR.getPos())/2) < straight:
        if mL.getPos() > mR.getPos():
            driveBase.setEffort(0, 1)
        else:
            driveBase.setEffort(1, 0)
    driveBase.setPos()

    ## Turn
    while ((- mL.getPos() + mR.getPos())/2) < rotationsToTurn:
        if -mL.getPos() > mR.getPos():
            driveBase.setEffort(0, 1)
        else:
            driveBase.setEffort(-1, 0)
    driveBase.setPos()
