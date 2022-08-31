import math
import time
from . import _encoded_motor


def _isTimeout(startTime, timeout):

    if timeout is None:
        return False
    return time.time() >= startTime+timeout


# Encapsulates the left and right motor objects and provides high-level functionality to manipulate robot locomotion.

class Drivetrain:

    def __init__(self, left_encoded_motor, right_encoded_motor, wheel_diameter, wheel_spacing): # wheelDiameter and wheelSpacing in cm

        self.leftMotor = left_encoded_motor
        self.rightMotor = right_encoded_motor
        
        self.wheelDiameter = wheel_diameter
        self.wheelSpacing = wheel_spacing

        self.set_encoder_position(0, 0)


    # Go forward the specified distance in centimeters, and exit function when distance has been reached.
    # Speed is bounded from -1 (reverse at full speed) to 1 (forward at full speed)
    def go_straight(self, distance: float, speed: float = 0.5, timeout: float = None) -> bool:
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
        startingLeft, startingRight = self.get_encoder_position()

        KP = 5

        rotationsToDo = distance  / (self.wheelDiameter * math.pi)

        while True:

            leftPosition, rightPosition = self.get_encoder_position()
            leftDelta = leftPosition - startingLeft
            rightDelta = rightPosition - startingRight

            if _isTimeout(startTime, timeout) or abs(leftDelta + rightDelta)/2 >= rotationsToDo:
                break

            error = KP * (leftDelta - rightDelta) # positive if bearing right
            print("Error:", error, leftDelta, rightDelta, speed)

            self.set_effort(speed - error, speed + error)

            time.sleep(0.01)

        self.stop()

        if timeout is None:
            return True
        else:
            return time.time() < startTime+timeout

    def go_turn(self, turn_degrees: float, speed: float = 0.5, timeout: float = None) -> bool:
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
        if turn_degrees < 0:
            speed *= -1
            turn_degrees *= -1

        rotationsToDo = (turn_degrees/360) * (math.pi * self.wheelSpacing) / (self.wheelDiameter * math.pi)

        startTime = time.time()
        startingLeft, startingRight = self.get_encoder_position()

        KP = 5

        while True:

            leftPosition, rightPosition = self.get_encoder_position()
            leftDelta = leftPosition - startingLeft
            rightDelta = rightPosition - startingRight

            if _isTimeout(startTime, timeout) or abs(leftDelta - rightDelta)/2 >= rotationsToDo:
                break
        
            error = KP * (leftDelta + rightDelta)
            print("Error:", error, leftDelta, rightDelta, speed)
            
            self.set_effort(speed - error, -speed - error)

            time.sleep(0.01)

        self.stop()

        if timeout is None:
            return True
        else:
            return time.time() < startTime+timeout

    def set_effort(self, left_effort: float, right_effort: float) -> None:
        """
        Set the raw effort of both motors individually

        : param leftEffort: The power (Bounded from -1 to 1) to set the left motor to.
        : type leftEffort: float
        : param rightEffort: The power (Bounded from -1 to 1) to set the right motor to.
        : type rightEffort: float
        """

        self.leftMotor.setEffort(left_effort)
        self.rightMotor.setEffort(right_effort)

    def stop(self) -> None:
        """
        Stops both drivetrain motors
        """
        self.set_effort(0,0)

    def set_encoder_position(self, left_degrees: float, right_degrees: float) -> None:
        """
        Set the position of the motors' encoders in degrees. Note that this does not actually move the motor but just recalibrates the stored encoder value.
        If only one encoder position is specified, the encoders for each motor will be set to that position.

        : param leftDegrees: The distance to recalibrate the left encoder to.
        : type leftDegrees: float
        : param rightDegrees: The distance to recalibrate the left encoder to.
        : type rightDegrees: float
        """

        self.leftMotor.setPos(left_degrees)
        self.rightMotor.setPos(right_degrees)

    def get_encoder_position(self) -> tuple:
        """
        Return the current position of left and right motors' encoders in degrees as a tuple.
        """
        return self.leftMotor.getPos(),self.rightMotor.getPos()