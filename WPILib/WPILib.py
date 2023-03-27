import board as _board
from . import _drivetrain
from . import _ultrasonic_wrapper
from . import _reflectance_wrapper
from . import _servo
from . import _buttons
from . import _encoded_motor
from . import _led

import time

# hidden motor variables
"""
If you need to change the encoder counts, alter the ticksPerRev values in the following two constructors.
Most robots have either 144 or 288 ticks per revolution, depending on which motors are used.
"""
_leftMotor = _encoded_motor.EncodedMotor(
    encoderPinA=_board.GP4, 
    encoderPinB=_board.GP5,
    motorPin1=_board.GP8, 
    motorPin2=_board.GP9, 
    doFlip=True, 
    ticksPerRev=288)

_rightMotor = _encoded_motor.EncodedMotor(
    encoderPinA=_board.GP2, 
    encoderPinB=_board.GP3,
    motorPin1=_board.GP10, 
    motorPin2=_board.GP11, 
    doFlip=False, 
    ticksPerRev=288)

# Publicly-accessible objects
drivetrain = _drivetrain.Drivetrain(_leftMotor, _rightMotor) # units in cm
reflectance = _reflectance_wrapper.Reflectance()
sonar = _ultrasonic_wrapper.Ultrasonic()
led = _led.RGBLED(_board.GP18)
servo = _servo.Servo(_board.GP12, actuationRange = 135)
buttons = _buttons.Buttons()

def set_legacy_mode(is_legacy: bool = True):
    drivetrain.set_legacy_mode(is_legacy)
    sonar.set_legacy_mode(is_legacy)
    reflectance.set_legacy_mode(is_legacy)