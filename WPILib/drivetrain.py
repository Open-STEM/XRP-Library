import math
import time

# Encapsulates the left and right motor objects and provides high-level functionality to manipulate robot locomotion.

class Drivetrain():

    def __init__(self, leftEncodedMotor, rightEncodedMotor, wDiam, wSpacing): # wheelDiameter and wheelSpacing in cm

        self.leftMotor = leftEncodedMotor
        self.rightMotor = rightEncodedMotor
        
        self.wheelDiameter = wDiam
        self.wheelSpacing = wSpacing

        self.setEncoderPosition(0)

    # Go forward the specified distance in centimeters, and exit function when distance has been reached.
    # Speed is bounded from -1 (reverse at full speed) to 1 (forward at full speed)
    def goStraight(self, distance: float, speed: float = 0.5, timeout: float = None) -> bool:
        """
        Go forward the specified distance in centimeters, and exit function when distance has been reached.
        Speed is bounded from -1 (reverse at full speed) to 1 (forward at full speed)

        : param distance: The distance for the robot to travel (In Centimeters)
        : type distance: float
        : param speed: The speed for which the robot to travel (Bounded from -1 to 1). Default is half speed forward
        : type speed: float
        : param timeout: The amount of time before the robot stops trying to move forward and continues to the next step (In Seconds)
        : type timeout: float
        : return: if the distance was reached before the timeout
        : rtype: bool
        """
        # ensure distance is always positive while speed could be either positive or negative
        if distance < 0:
            speed *= -1
            distance *= -1

        startTime = time.time()
        KP = 1

        rotationsToDo = distance  / (self.wheelDiameter * math.pi)

        while abs(self.leftMotor.getPos() + self.rightMotor.getPos() < rotationsToDo and time.time() < startTime+timeout):

            error = KP * (self.leftMotor.getPos() - self.rightMotor.getPos()) # positive if bearing right

            self.setEffort(speed - error, speed + error)

        self.stop()

        return time.time() < startTime+timeout

    def goTurn(self, turnDegrees: float, speed: float = 0.5, timeout: float = None):
        """
        Turn the robot some relative heading given in turnDegrees, and exit function when the robot has reached that heading.
        Speed is bounded from -1 (turn counterclockwise the relative heading at full speed) to 1 (turn clockwise the relative heading at full speed)

        : param turnDegrees: The number of angle for the robot to turn (In Degrees)
        : type turnDegrees: float
        : param speed: The speed for which the robot to travel (Bounded from -1 to 1). Default is half speed forward.
        : type speed: float
        : param timeout: The amount of time before the robot stops trying to turn and continues to the next step (In Seconds)
        : type timeout: float
        : return: if the distance was reached before the timeout
        : rtype: bool
        """
        rotationsToDo = (turnDegrees/360) * (math.pi * self.wheelSpacing) / (self.wheelDiameter * math.pi)

        startTime = time.time()
        KP = 1

        while abs(self.leftMotor.getPos() - self.rightMotor.getPos() < rotationsToDo and time.time() < startTime+timeout):

            error = KP * (self.leftMotor.getPos() + self.rightMotor.getPos())

            self.setEffort(speed - error, -speed - error)

        self.stop()

        return time.time() < startTime+timeout

    def setEffort(self, leftEffort: float, rightEffort: float):
        """
        Set the raw effort of both motors individually

        : param leftEffort: The power (Bounded from -1 to 1) to set the left motor to.
        : type leftEffort: float
        : param rightEffort: The power (Bounded from -1 to 1) to set the right motor to.
        : type rightEffort: float
        """
        leftEffort = leftEffort
        rightEffort = rightEffort

        self.leftMotor.setEffort(leftEffort)
        self.rightMotor.setEffort(rightEffort)

    def stop(self):
        """
        Stops both drivetrain motors
        """
        self.setEffort(0)

    def setSpeed(self, leftSpeed, rightSpeed):
        """
        Set the speed of both motors. The encoded motors will attempt to maintain their speeds with proportional control.
        If only one speed is specified, both motors will be set at that speed.

        : param leftSpeed: The speed (In centimeters per second) to set the left motor to.
        : type leftSpeed: float
        : param rightSpeed: The speed (In centimeters per second) to set the right motor to.
        : type rightSpeed: float
        """
        leftSpeed = leftSpeed
        rightSpeed = rightSpeed

    def setEncoderPosition(self, leftDegrees: float, rightDegrees: float):
        """
        Set the position of the motors' encoders in degrees. Note that this does not actually move the motor but just recalibrates the stored encoder value.
        If only one encoder position is specified, the encoders for each motor will be set to that position.

        : param leftDegrees: The distance to recalibrate the left encoder to.
        : type leftDegrees: float
        : param rightDegrees: The distance to recalibrate the left encoder to.
        : type rightDegrees: float
        """

        degLeft = leftDegrees
        degRight = rightDegrees

        self.leftMotor.setPos(degLeft)
        self.rightMotor.setPos(degRight)

    def getEncoderPosition(self):
        """
        Return the current position of left and right motors' encoders in degrees as a tuple.
        """
        return self.leftMotor.getPos(),self.rightMotor.getPos()


