import time
import board
import encoder as enc
import encoded_motor as em
import drive as drv
import GroveUltrasonicRanger
import pwmio
from adafruit_motor import servo

sonar = GroveUltrasonicRanger.GroveUltrasonicRanger(board.GP28)

driveBase = drv.drive()

class Reflect:
    def __init__(self):
        self.refl = GroveUltrasonicRanger.GroveUltrasonicRanger(board.GP27)
        self.refr = GroveUltrasonicRanger.GroveUltrasonicRanger(board.GP26)
    
    def left(self):
        return self.refl.distance
    
    def right(self):
        return self.refr.distance

refl = Reflect()