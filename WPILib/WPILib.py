import board as _board
import drivetrain_module as _drivetrain
import grove_ultrasonic as _grove_ultrasonic
import reflectance_module as _reflectance
import servo_module as _servo
import buttons_module as _buttons

import time
from encoded_motor_module import BrakeType

# hidden motor variables
_leftMotor = _drivetrain._encoded_motor.EncodedMotor(encoderPinA=_board.GP4, encoderPinB=_board.GP5,
                                               motorPin1=_board.GP8, motorPin2=_board.GP9, doFlip=True)

_rightMotor = _drivetrain._encoded_motor.EncodedMotor(encoderPinA=_board.GP2, encoderPinB=_board.GP3,
                                               motorPin1=_board.GP10, motorPin2=_board.GP11, doFlip=False)

# Publicly-accessible objects
drivetrain = _drivetrain.Drivetrain(_leftMotor, _rightMotor, wheelDiameter=6.5, wheelSpacing=16) # units in cm
reflectance = _reflectance.Reflectance(_board.GP27, _board.GP26)
sonar = _grove_ultrasonic.GroveUltrasonicRanger(_board.GP28)
led = None
servo = _servo.Servo(_board.GP12, actuationRange = 135)
buttons = _buttons.Buttons()