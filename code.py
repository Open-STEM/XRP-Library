import time
import board
import pwmio
import rotaryio
from adafruit_motor import motor
import Encoder as enc
from simple_pid import PID
import encodedMotor as em
import drive as drv

# Motor Right
encR = enc.encoder(a=board.GP2, b=board.GP3, ticks=144)
mR = em.EncodedMotor(encR, board.GP8, board.GP9, "Motor Right", False)

# Motor Left
encL = enc.encoder(a=board.GP4, b=board.GP5, ticks=144)
mL = em.EncodedMotor(encL, board.GP10, board.GP11, "Motor Left", True)

# Drive Base
driveBase = drv.drive(mL,mR)

turns = 4
straight = 5

while turns > 0:
    print(turns)
    turns -= 1
    driveBase.straight(500)
    driveBase.turn(-90)
