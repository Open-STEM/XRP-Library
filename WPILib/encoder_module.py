# Write your code here :-)
import rotaryio

class Encoder:

    def __init__(self, pinA, pinB, ticksPerRev, doFlip=False):
        self.ticksPerRev = ticksPerRev
        self.reverse = doFlip
        self.encoder = rotaryio.IncrementalEncoder(pinA, pinB)
        print("initialized")

    def getPos(self, inTicks: bool = False, roundTo: int = 3) -> float:
        """
        Retrieves the position of the encoder

        :param inTicks: If true, returns in encoder ticks; If false, returns in rotations
        :type inTicks: bool
        :param roundTo: The number of decimal places to round the encoder position to
        :type roundTo: int

        :return: The position of the encoder
        :rtype: float
        """
        r = self.encoder.position
        if self.reverse:
            r *= -1
        if not inTicks:
            r = r / self.ticksPerRev
        return round(r, roundTo)

    def setPos(self, pos: float = 0):
        """
        Recalibrates the encoder to the specified position
        :param pos: The number of rotations to set encoder to
        :type pos: float
        :return: void
        """
        self.encoder.position = round(pos * self.ticksPerRev)


