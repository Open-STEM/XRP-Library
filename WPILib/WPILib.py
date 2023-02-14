import board as _board
from _drivetrain import Drivetrain
from _encoded_motor import EncodedMotor
from _ultrasonic_wrapper import Ultrasonic
from _reflectance_wrapper import Reflectance
from _servo import Servo
from _buttons import Buttons
from _led import RGBLED

import time

# hidden motor variables
"""
If you need to change the encoder counts, alter the ticksPerRev values in the following two constructors.
Most robots have either 144 or 288 ticks per revolution, depending on which motors are used.
"""
_leftMotor = EncodedMotor(
    encoderPinA=_board.GP4, 
    encoderPinB=_board.GP5,
    motorPin1=_board.GP8, 
    motorPin2=_board.GP9, 
    doFlip=True, 
    ticksPerRev=288)

_rightMotor = EncodedMotor(
    encoderPinA=_board.GP2, 
    encoderPinB=_board.GP3,
    motorPin1=_board.GP10, 
    motorPin2=_board.GP11, 
    doFlip=False, 
    ticksPerRev=288)

# Publicly-accessible objects
drivetrain = Drivetrain(_leftMotor, _rightMotor) # units in cm
reflectance = Reflectance()
sonar = Ultrasonic()
led = RGBLED(_board.GP18)
servo = Servo(_board.GP12, actuationRange = 135)
buttons = Buttons()

def set_legacy_mode(is_legacy: bool = True):
    drivetrain.set_legacy_mode(is_legacy)
    sonar.set_legacy_mode(is_legacy)
    reflectance.set_legacy_mode(is_legacy)