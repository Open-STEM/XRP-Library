import board as _board
from . import _drivetrain
from . import _grove_ultrasonic
from . import _reflectance
from . import _servo
from . import _buttons
from . import _encoded_motor
from . import _led

import time

# hidden motor variables
_leftMotor = _drivetrain._encoded_motor.EncodedMotor(encoderPinA=_board.GP4, encoderPinB=_board.GP5,
                                               motorPin1=_board.GP8, motorPin2=_board.GP9, doFlip=True)

_rightMotor = _drivetrain._encoded_motor.EncodedMotor(encoderPinA=_board.GP2, encoderPinB=_board.GP3,
                                               motorPin1=_board.GP10, motorPin2=_board.GP11, doFlip=False)

# Publicly-accessible objects
drivetrain = _drivetrain.Drivetrain(_leftMotor, _rightMotor) # units in cm
reflectance = _reflectance.Reflectance(_board.GP27, _board.GP26)
sonar = _grove_ultrasonic.GroveUltrasonicRanger(_board.GP28)
led = _led.RGBLED(_board.GP18)
servo = _servo.Servo(_board.GP12, actuationRange = 135)
buttons = _buttons.Buttons()