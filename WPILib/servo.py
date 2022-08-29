from adafruit_motor import servo

class Servo:

    def __init__(self, servoPin, actuationRange: int):

        pwm = pwmio.PWMOut(servoPin, actuationRange = actuationRange, duty_cycle=2 ** 15, frequency=50)
        self._servo = servo.Servo(pwm)
        self._range = actuationRange
        self._servo.actuation_range = self.range # Bound servo motor between [0, actuationRange] degrees

    def setDegrees(self, degrees):
        self._servo.angle = max(0, min(self._range, degrees))
