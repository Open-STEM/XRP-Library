
import rotaryio

class Encoder:

    def __init__(self, pinA, pinB, ticksPerRev, doFlip=False):
        self.ticksPerRev = ticksPerRev
        self.reverse = doFlip
        self.encoder = rotaryio.IncrementalEncoder(pinA, pinB)

    def getPos(self) -> float:
        """
        Retrieves the position of the encoder in revolutions

        :return: The position of the encoder
        :rtype: float
        """
        r = self.encoder.position / self.ticksPerRev
        if self.reverse:
            return -r
        else:
            return r


    def setPos(self, pos: float = 0):
        """
        Recalibrates the encoder to the specified position
        :param pos: The number of rotations to set encoder to
        :type pos: float
        :return: void
        """
        self.encoder.position = round(pos * self.ticksPerRev)

    def _set_encoder_ticks_per_rev(self, ticks_per_revolution: int):
        self.ticksPerRev = ticks_per_revolution
