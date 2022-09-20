import pwmio
from adafruit_motor import servo
import time

class Servo:

    def __init__(self, servoPin, actuationRange: int):

        pwm = pwmio.PWMOut(servoPin, duty_cycle=2 ** 15, frequency=50)
        self._servo = servo.Servo(pwm)
        self._range = actuationRange
        self._servo.actuation_range = self._range # Bound servo motor between [0, actuationRange] degrees

    def set_degrees(self, degrees: int):
        """
            Tells the servo to move to the specified position

            :param degrees: The angle for the servo to move to, bound in [0,135]
            :type degrees: int
        """
        self._servo.angle = max(0, min(self._range, degrees))
