# Write your code here :-)
from adafruit_motor import motor
import pwmio
import time
from . import _encoder

class EncodedMotor:
    def __init__(self, encoderPinA, encoderPinB , motorPin1, motorPin2, Name="Motor Unnamed", doFlip=False):
        
        self.name = Name
        self.encoder = _encoder.Encoder(pinA=encoderPinA, pinB=encoderPinB, ticksPerRev=144, doFlip=doFlip)
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
        print("Position " + str(self.encoder.getPos()))
        print("Flipped  " + str(self.flip))
        pass

    # set motor throttle (effort) betwen [-1, 1]
    def setEffort(self, effort: float) -> None:
        if effort is None:
            self.motor.throttle = None
        else:
            self.motor.throttle = min(1, max(-1, effort)) # bound effort between [-1, 1]

    # Set brake type of motor. False = coast, true = brake
    def setBrakeType(self, brakeType: bool) -> None:
        if brakeType:
            self.motor.decay_mode = motor.SLOW_DECAY # brake
        else:
            self.motor.decay_mode = motor.FAST_DECAY


    def getPos(self) -> float:
        encoderValue = self.encoder.getPos()
        assert(encoderValue is not None)
        return encoderValue

    def setPos(self, pos: float = 0):
        self.encoder.setPos(pos)
