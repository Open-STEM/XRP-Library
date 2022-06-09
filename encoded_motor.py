# Write your code here :-)
from adafruit_motor import motor
import pwmio
import time
import encoder
from simple_pid import PID

class encoded_motor():
    def __init__(self, Encoder, MotorPin1, MotorPin2, Name="Motor Unnamed", doFlip=False):
        self.name = Name
        self.enc = Encoder
        self.flip = doFlip
        MA = pwmio.PWMOut(MotorPin1, frequency=10000)
        MB = pwmio.PWMOut(MotorPin2, frequency=10000)
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

    def setEffort(self, effort = 0):
        self.effort = effort
        if effort is None:
            pass
        elif effort < -1.0:
            print(self.name + " effort " + str(effort) + " is too low.")
        elif 1.0 < effort:
            print(self.name + " effort " + str(effort) + " is too big.")
        else:
            self.motor.throttle = effort

    def getPos(self):
        return self.enc.getPos()

    def setPos(self, pos=0):
        self.enc.setPos(pos)
