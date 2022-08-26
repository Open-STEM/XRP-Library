import math
import time

# Encapsulates the left and right motor objects and provides high-level functionality to manipulate robot locomotion.

class Drivetrain():

    def __init__(self, leftEncodedMotor, rightEncodedMotor, wheelDiameter, wheelSpacing): # wheelDiameter and wheelSpacing in mm

        self.leftMotor = leftEncodedMotor
        self.rightMotor = rightEncodedMotor
        
        self.wDiam = wheelDiameter
        self.wSpacing = wheelSpacing

        self.setEncoderPosition(0)

    # Go forward the specified distance in centimeters, and exit function when distance has been reached.
    # Speed is bounded from -1 (reverse at full speed) to 1 (forward at full speed)
    def goForward(self, distanceCm, speed = 0.5):

        # ensure distance is always positive while speed could be either positive or negative
        if distanceCm < 0:
            speed *= -1
            distanceCm *= -1

        KP = 1

        distanceMm = 10 * distanceCm
        rotationsToDo = distanceMm  / (self.wDiam * math.pi)

        while abs(self.leftMotor.getPos() + self.rightMotor.getPos()) < rotationsToDo:

            error = KP * (self.leftMotor.getPos() - self.rightMotor.getPos()) # positive if bearing right

            self.setEffort(speed - error, speed + error)



        self.stop()

    # Turn the robot some relative heading given in turnDegrees, and exit function when the robot has reached that heading.
    # Speed is bounded from -1 (turn counterclockwise the relative heading at full speed) to 1 (turn clockwise the relative heading at full speed)
    def goTurn(self, turnDegrees, speed = 0.5):

        rotationsToDo = (degrees/360) * (math.pi * self.wSpacing) / (self.wDiam * math.pi)

    # Set the raw effort of both motors. If only one effort is specified, both motors will be set at that effort.
    def setEffort(self, effort, rightEffort = None):
        leftEffort = effort
        rightEffort = effort if rightEffort is None else rightEffort

        self.leftMotor.setEffort(leftEffort)
        self.rightMotor.setEffort(rightEffort)

    # Stop both motors.
    def stop(self):
        self.setEffort(0)

    # Set the speed of both motors. The encoded motors will attempt to maintain their speeds with proportional control.
    # If only one speed is specified, both motors will be set at that speed.
    def setSpeed(self, speed, rightSpeed = None):
        leftSpeed = speed
        rightSpeed = speed if rightSpeed is None else rightSpeed

    # Set the position of the motors' encoders in degrees. Note that this does not actually move the motor but just recalibrates the stored encoder value.
    # If only one encoder position is specified, the encoders for each motor will be set to that position.
    def setEncoderPosition(self, degrees, degreesRight = None)

        degLeft = degrees
        degRight = degrees if degreesRight is None else degreesRight

        self.leftMotor.setPos(degLeft)
        self.rightMotor.setPos(degRight)

    # Return the current position of left and right motors' encoders in degrees as a tuple.
    def getEncoderPosition(self):
        return leftMotor.getPos(),rightMotor.getPos()


