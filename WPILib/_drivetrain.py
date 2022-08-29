import math
import time
from . import _encoded_motor

# Encapsulates the left and right motor objects and provides high-level functionality to manipulate robot locomotion.

class Drivetrain:

    def __init__(self, leftEncodedMotor, rightEncodedMotor, wheelDiameter, wheelSpacing): # wheelDiameter and wheelSpacing in cm

        self.leftMotor = leftEncodedMotor
        self.rightMotor = rightEncodedMotor
        
        self.wheelDiameter = wheelDiameter
        self.wheelSpacing = wheelSpacing

        self.setEncoderPosition(0, 0)

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
        startingLeft = self.leftMotor.getPos()
        startingRight = self.rightMotor.getPos()

        KP = 1

        rotationsToDo = distance  / (self.wheelDiameter * math.pi)

        while abs((self.leftMotor.getPos() - startingLeft) + (self.rightMotor.getPos())-startingRight) < rotationsToDo and (timeout is None or time.time() < startTime+timeout):

            error = KP * (self.leftMotor.getPos() - self.rightMotor.getPos()) # positive if bearing right
            print("Error:", error, self.leftMotor.getPos())

            self.setEffort(speed - error, speed + error)

        self.stop()

        return time.time() < startTime+timeout

    def goTurn(self, turnDegrees: float, speed: float = 0.5, timeout: float = None) -> bool:
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

        # ensure distance is always positive while speed could be either positive or negative
        if turnDegrees < 0:
            speed *= -1
            turnDegrees *= -1

        rotationsToDo = (turnDegrees/360) * (math.pi * self.wheelSpacing) / (self.wheelDiameter * math.pi)

        startTime = time.time()
        startingLeft = self.leftMotor.getPos()
        startingRight = self.rightMotor.getPos()

        KP = 1

        while abs((self.leftMotor.getPos() - startingLeft) + (self.rightMotor.getPos())-startingRight) < rotationsToDo and (timeout is None or time.time() < startTime+timeout):

            error = KP * (self.leftMotor.getPos() + self.rightMotor.getPos())

            self.setEffort(speed - error, -speed - error)

        self.stop()

        return time.time() < startTime+timeout

    def setEffort(self, leftEffort: float, rightEffort: float) -> None:
        """
        Set the raw effort of both motors individually

        : param leftEffort: The power (Bounded from -1 to 1) to set the left motor to.
        : type leftEffort: float
        : param rightEffort: The power (Bounded from -1 to 1) to set the right motor to.
        : type rightEffort: float
        """

        self.leftMotor.setEffort(leftEffort)
        self.rightMotor.setEffort(rightEffort)

    def stop(self) -> None:
        """
        Stops both drivetrain motors
        """
        self.setEffort(0,0)

    def setEncoderPosition(self, leftDegrees: float, rightDegrees: float) -> None:
        """
        Set the position of the motors' encoders in degrees. Note that this does not actually move the motor but just recalibrates the stored encoder value.
        If only one encoder position is specified, the encoders for each motor will be set to that position.

        : param leftDegrees: The distance to recalibrate the left encoder to.
        : type leftDegrees: float
        : param rightDegrees: The distance to recalibrate the left encoder to.
        : type rightDegrees: float
        """

        self.leftMotor.setPos(leftDegrees)
        self.rightMotor.setPos(rightDegrees)

    def getEncoderPosition(self) -> tuple:
        """
        Return the current position of left and right motors' encoders in degrees as a tuple.
        """
        return self.leftMotor.getPos(),self.rightMotor.getPos()

    def setBrakeType(self, brakeType: bool) -> None:
        """
        Sets the motor controller recirculation current decay mode, which controls whether the motor coasts or brakes.

        :param brakeType: false sets the motor controller to the default fast recirculation current decay mode (coast), while true sets it to slow decay mode (brake)
        :type inTicks: BrakeType
        :param roundTo: The number of decimal places to round the encoder position to
        :type roundTo: int
        """
        self.leftMotor.setBrakeType(brakeType)
        self.rightMotor.setBrakeType(brakeType)


