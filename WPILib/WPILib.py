import time
import board as _board
import encoded_motor as _encoded_motor
import drivetrain as _drivetrain
import grove_ultrasonic as _grove_ultrasonic
import reflectance as _reflectance

# hidden motor variables
_leftMotor = _encoded_motor.EncodedMotor(encoderPinA=_board.GP4, encoderPinB=_board.GP5,
                                               motorPin1=_board.GP8, motorPin2=_board.GP9, doFlip=True)

_rightMotor = _encoded_motor.EncodedMotor(encoderPinA=_board.GP2, encoderPinB=_board.GP3,
                                               motorPin1=_board.GP10, motorPin2=_board.GP11, doFlip=False)

# Publicly-accessible objects
drivetrain = _drivetrain.Drivetrain(_leftMotor, _rightMotor, wheelDiameter=65, wheelSpacing=160) # units in mm
reflectance = _reflectance.Reflectance(_board.GP27, _board.GP26)
sonar = _grove_ultrasonic.GroveUltrasonicRanger(_board.GP28)
