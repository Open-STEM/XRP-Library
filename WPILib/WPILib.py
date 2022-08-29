import time
import board as _board
import encoded_motor as _encoded_motor
from encoded_motor import BrakeType
import drivetrain as _drivetrain
import grove_ultrasonic as _grove_ultrasonic
import reflectance as _reflectance
import servo as _servo
import buttons as _buttons

# hidden motor variables
_leftMotor = _encoded_motor.EncodedMotor(encoderPinA=_board.GP4, encoderPinB=_board.GP5,
                                               motorPin1=_board.GP8, motorPin2=_board.GP9, doFlip=True)

_rightMotor = _encoded_motor.EncodedMotor(encoderPinA=_board.GP2, encoderPinB=_board.GP3,
                                               motorPin1=_board.GP10, motorPin2=_board.GP11, doFlip=False)

# Publicly-accessible objects
drivetrain = _drivetrain.Drivetrain(_leftMotor, _rightMotor, wheelDiameter=6.5, wheelSpacing=16) # units in cm
reflectance = _reflectance.Reflectance(_board.GP27, _board.GP26)
sonar = _grove_ultrasonic.GroveUltrasonicRanger(_board.GP28)
led = None
buttons = None
servo = _servo.Servo(_board.GP12, actuationRange = 135)
buttons = _buttons.Buttons()

#sphinx docs comments
