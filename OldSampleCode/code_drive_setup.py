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

# Test Motor Direction
while False:
    print("Test Left Wheel")
    driveBase.setEffort(1, 0)
    time.sleep(2)
    
    print("Stopped Wheel")
    print()
    driveBase.setEffort(0, 0)
    time.sleep(.5)

    print("Test Right Wheel")
    driveBase.setEffort(0, 1)
    time.sleep(2)
    
    print("Stopped Wheel")
    print()
    driveBase.setEffort(0, 0)
    time.sleep(.5)

# Test Encoder Direction
while True:
    print("Test Encoder Direction")
    driveBase.setEffort(1, 1)
    print()
    print(mL)
    print(mR)
    time.sleep(2)
