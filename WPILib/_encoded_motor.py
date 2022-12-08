from adafruit_motor import motor
import pwmio
import time
from . import _encoder

class EncodedMotor:
    def __init__(self, encoderPinA, encoderPinB , motorPin1, motorPin2, Name="Motor Unnamed", doFlip=False, ticksPerRev=288):
        
        self.name = Name
        self.encoder = _encoder.Encoder(pinA=encoderPinA, pinB=encoderPinB, ticksPerRev=ticksPerRev, doFlip=doFlip)
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

    def getPos(self) -> float:
        return self.encoder.getPos()

    def setPos(self, pos: float = 0) -> None:
        self.encoder.setPos(pos)

    def _set_encoder_ticks_per_rev(self, ticks_per_revolution: int):
        self.encoder._set_encoder_ticks_per_rev(ticks_per_revolution)