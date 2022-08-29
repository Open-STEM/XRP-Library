# Write your code here :-)
from adafruit_motor import motor
import pwmio
import time
import encoder
from simple_pid import PID
from enum import Enum

class BrakeType(Enum):
    BRAKE_MODE = 1
    COAST_MODE = 2

class EncodedMotor():
    def __init__(self, encoderPinA, encoderPinB , motorPin1, motorPin2, Name="Motor Unnamed", doFlip=False):
        
        self.name = Name
        self.encoder = encoder.Encoder(pinA=encoderPinA, pinB=encoderPinB, ticksPerRev=144, doFlip=doFlip)
        self.flip = doFlip
        
        MA = pwmio.PWMOut(motorPin1, frequency=10000)
        MB = pwmio.PWMOut(motorPin2, frequency=10000)
        if doFlip:
            self.motor = motor.DCMotor(MB, MA)
        else:
            self.motor = motor.DCMotor(MA, MB)

        self.effort = None

    def __repr__(self):
        print(self.name)
        print("Effort   " + str(self.effort))
        print("Position " + str(self.enc.getPos()))
        print("Flipped  " + str(self.flip))
        pass

    # set motor throttle (effort) betwen [-1, 1]
    def setEffort(self, effort: float):
        if effort is None:
            self.motor.throttle = None
        else:
            self.motor.throttle = min(1, max(-1, effort)) # bound effort between [-1, 1]

<<<<<<< HEAD
    def getSpeed(self):
        firstTime = time.time()
        firstPos = self.getPos()
        speed = (self.getPos()-firstPos)/(time.time()-firstTime)
        return speed
=======
    # Set brake type of motor
    def setBrakeType(self, brakeType: BrakeType) -> None:
        if brakeType == BrakeType.BRAKE_MODE:
            self.motor.decay_mode = motor.SLOW_DECAY
        elif brakeType == BrakeType.COAST_MODE:
            self.motor.decay_motor = motor.FAST_DECAY
        else:
            raise Exception("Unknown brake mode. This motor can only be set to BRAKE_MODE or COAST_MODE.")

>>>>>>> e9a78549d18b51873c591c3e229ed1e0e0dccf66

    def getPos(self):
        return self.enc.getPos()

    def setPos(self, pos=0):
        self.enc.setPos(pos)
